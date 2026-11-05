---
sidebar_position: 125
id: monitoring
title: Monitoring with Prometheus
description: Collect OpenCloud metrics with Prometheus, including classic and native histograms
draft: false
---

# Monitoring with Prometheus

OpenCloud exposes metrics in the Prometheus format: counters for requests and events, gauges for things like the number of requests currently in flight, and histograms that measure how long operations take. You can collect these metrics with [Prometheus](https://prometheus.io/) (or any other system that understands the Prometheus format) and visualize them, for example with Grafana.

This page explains where OpenCloud exposes its metrics, how to configure Prometheus to collect them, and how to work with the duration histograms.

## Where OpenCloud Exposes Its Metrics

Every OpenCloud service has a **debug endpoint**: an additional HTTP endpoint with an address and port of its own, separate from the regular HTTP endpoints that users and clients talk to. It is not a separate process, but part of the OpenCloud process that runs the service.

Among other things, the debug endpoint provides the metrics under the path `/metrics`.

The address the debug endpoint listens on is configured per service with an environment variable that ends in `_DEBUG_ADDR`, for example `PROXY_DEBUG_ADDR` for the proxy service, whose default is `127.0.0.1:9205`.

When OpenCloud runs as a single process, which is the case with the OpenCloud Compose setup and with the `opencloud server` command, all its services share the same set of metrics. Every debug endpoint of that process then returns exactly the same metrics, so **it is sufficient to collect the metrics from a single endpoint**.

Collecting them from several debug endpoints of the same process would only store every metric several times. By convention, use the debug endpoint of the proxy service.

Services that run in a separate process or container have their own metrics. With OpenCloud Compose, this is the case for the collaboration service, whose debug endpoint is configured with `COLLABORATION_DEBUG_ADDR`.

:::note
The default debug address `127.0.0.1:9205` only accepts connections from the same machine, or from the same container. To let Prometheus collect the metrics from another container or another machine, the debug endpoint must listen on an address that is reachable from there, for example `0.0.0.0:9205`.
:::

### Enable the Metrics Endpoints With OpenCloud Compose

OpenCloud Compose comes with the file `monitoring/monitoring.yml`, which makes the debug endpoint of the proxy service listen on port 9205 on all interfaces (`PROXY_DEBUG_ADDR=0.0.0.0:9205`), and connects OpenCloud to an external Docker network called `opencloud-net`. Prometheus can then collect the metrics through that network. If you use the collaboration service, `monitoring/monitoring-collaboration.yml` does the same for the collaboration service on port 9304.

First, create the Docker network:

```bash
docker network create opencloud-net
```

Then add the monitoring file to `COMPOSE_FILE` in your `.env` file, for example:

```bash
COMPOSE_FILE=docker-compose.yml:monitoring/monitoring.yml:traefik/opencloud.yml
```

or, with the collaboration service:

```bash
COMPOSE_FILE=docker-compose.yml:monitoring/monitoring.yml:monitoring/monitoring-collaboration.yml:traefik/opencloud.yml:weboffice/collabora.yml:traefik/collabora.yml
```

and restart OpenCloud:

```bash
docker compose up -d
```

To check that the metrics are available, request them from within the OpenCloud container:

```bash
docker compose exec opencloud curl -s http://localhost:9205/metrics | grep '^opencloud_proxy_requests_total'
```

The output should contain lines like these:

```text
opencloud_proxy_requests_total{method="GET"} 1342
opencloud_proxy_requests_total{method="PROPFIND"} 287
```

### Protect the Metrics Endpoint With a Token

The metrics endpoint does not require any authentication by default. If the debug endpoint is reachable from a network that you don't fully trust, protect it with a token. The token is configured per service with the environment variable that ends in `_DEBUG_TOKEN`, for example `PROXY_DEBUG_TOKEN` for the proxy service:

```yaml
services:
  opencloud:
    environment:
      PROXY_DEBUG_TOKEN: 'a-long-random-secret'
```

Use a long random string as the token. On Linux and macOS, you can generate one with `openssl`:

```bash
openssl rand -hex 32
```

which prints 64 random hexadecimal characters, for example:

```text
3f9c2b7e41d08a5c6e1f97b2d4a03c8e5b6f1a2d9c7e0b4f8a3d6c1e2b9f7a05
```

If `openssl` is not installed, this command works on Linux and macOS as well, and prints 48 random letters and digits:

```bash
LC_ALL=C tr -dc 'A-Za-z0-9' < /dev/urandom | head -c 48; echo
```

Requests to the metrics endpoint must then send the token in the `Authorization` header, as a bearer token:

```bash
curl -H 'Authorization: Bearer a-long-random-secret' http://opencloud:9205/metrics
```

Requests without the token, or with a wrong token, are answered with `401 Unauthorized`.

The Prometheus configuration below shows how to configure the token in Prometheus.

## Configure Prometheus

Prometheus collects metrics by requesting them from the configured targets at a regular interval, which is called _scraping_.

The following example of a `prometheus.yml` collects the metrics of OpenCloud from the debug endpoint of the proxy service, and of the collaboration service if you use it. It assumes that Prometheus runs in a container that is connected to the `opencloud-net` network, so that it can reach the OpenCloud containers by their service names `opencloud` and `collaboration`:

```yaml title="prometheus.yml"
global:
  scrape_interval: 30s

scrape_configs:
  - job_name: opencloud
    static_configs:
      - targets: ['opencloud:9205']

  - job_name: opencloud-collaboration
    static_configs:
      - targets: ['collaboration:9304']
```

If you protected the metrics endpoint with a token, add it to the scrape configuration with `authorization`; Prometheus sends it as a bearer token:

```yaml title="prometheus.yml"
scrape_configs:
  - job_name: opencloud
    authorization:
      credentials: 'a-long-random-secret'
    static_configs:
      - targets: ['opencloud:9205']
```

Once Prometheus is running, open its web interface, go to **Status → Targets**, and check that the state of the `opencloud` target is **UP**.

All OpenCloud metrics start with `opencloud_`, so entering `opencloud_` in the query field of the Prometheus web interface lists them.

## Duration Histograms

Many OpenCloud metrics measure how long something takes: an HTTP request to the Graph API, an LDAP operation, a request going through the proxy, a search, the postprocessing of an upload. These measurements are recorded in **[histograms](https://prometheus.io/docs/concepts/metric_types/#histogram)**.

A histogram doesn't store every single measurement. Instead, it counts how many measurements fell into each of a number of ranges, called _buckets_, and additionally keeps the total number of measurements and their sum. From that, Prometheus can calculate percentiles ("99% of the requests took less than 0.8 seconds"), averages, and the share of measurements below a threshold.

Prometheus knows two kinds of histograms:

- **Classic histograms** have a fixed set of buckets, whose upper bounds are defined by OpenCloud. Each bucket is a separate time series, with the upper bound in the label `le` ("less or equal"), plus a time series for the count and one for the sum. Every Prometheus version understands them.
- **Native histograms** choose their buckets automatically, with a much higher resolution: OpenCloud configures them so that the bucket boundaries are at most about 10% apart, which makes percentiles much more accurate. A native histogram is stored as a single time series, no matter how many buckets it has, which also saves a lot of storage. Native histograms must be enabled in Prometheus explicitly, as described below.

Most of OpenCloud's duration histograms are classic histograms. Only the request durations of the proxy are recorded in a native histogram, see [The Request Durations of the Proxy](#the-request-durations-of-the-proxy) below.

### Classic Histograms

For each classic histogram, Prometheus stores one time series per bucket, with the suffix `_bucket`, plus one with the suffix `_count` (the number of measurements) and one with the suffix `_sum` (the sum of all measured durations, in seconds).

The bucket counters are cumulative: each bucket counts all measurements that are less than or equal to its upper bound, and the last bucket, `le="+Inf"`, counts all measurements.

For the webfinger service, for example, the metrics endpoint returns lines like these:

```text
opencloud_webfinger_webfinger_duration_seconds_bucket{le="0.005"} 340
opencloud_webfinger_webfinger_duration_seconds_bucket{le="0.01"} 1180
opencloud_webfinger_webfinger_duration_seconds_bucket{le="0.025"} 1211
...
opencloud_webfinger_webfinger_duration_seconds_bucket{le="10"} 1214
opencloud_webfinger_webfinger_duration_seconds_bucket{le="+Inf"} 1214
opencloud_webfinger_webfinger_duration_seconds_sum 7.92
opencloud_webfinger_webfinger_duration_seconds_count 1214
```

Here, 1214 webfinger requests were measured, which took 7.92 seconds altogether; 340 of them took at most 5 milliseconds, and 1180 at most 10 milliseconds.

The buckets of a classic histogram are a compromise: more buckets give more accurate percentiles, but every bucket is an additional time series for every combination of label values.

Most OpenCloud histograms use the default buckets of the Prometheus Go client library, with these upper bounds, in seconds:

```text
0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10
```

Everything that takes longer than 10 seconds is only counted in the `+Inf` bucket.

The histograms of the search and postprocessing services have buckets of their own, up to 60 and 1200 seconds.

The [list of duration histograms](#list-of-the-duration-histograms) at the end of this page shows the buckets of each histogram.

### Native Histograms

A native histogram is stored as a single time series with the name of the metric, without a suffix: there is no `_bucket`, `_count` or `_sum` time series. Prometheus provides functions to get these values from a native histogram instead, such as `histogram_count()`, `histogram_sum()`, `histogram_avg()` and `histogram_fraction()`, and `histogram_quantile()` works with native histograms directly. The [section about the proxy](#the-request-durations-of-the-proxy) below shows examples.

Native histograms are transferred with the [Protobuf format](https://protobuf.dev/), not with the text format that you see when you request the metrics endpoint with `curl` or in a browser. The text format therefore only shows the classic part of the histograms; that is expected.

### Enable Native Histograms in Prometheus

How native histograms are enabled depends on the version of Prometheus:

| Prometheus version | How to enable native histograms                                                                              |
| ------------------ | ------------------------------------------------------------------------------------------------------------ |
| 2.39 and older     | Not supported.                                                                                               |
| 2.40 to 3.7        | Start Prometheus with the command line option `--enable-feature=native-histograms`.                          |
| 3.8                | Set `scrape_native_histograms: true` in the configuration (the command line option above still works, too).  |
| 3.9 and newer      | Set `scrape_native_histograms: true` in the configuration. The command line option no longer has any effect. |

With Prometheus 3.8 or newer, set `scrape_native_histograms` in the `global` section, to enable native histograms for all scrape configurations, or only in the scrape configuration of OpenCloud:

```yaml title="prometheus.yml"
scrape_configs:
  - job_name: opencloud
    scrape_native_histograms: true
    static_configs:
      - targets: ['opencloud:9205']
```

After reloading or restarting Prometheus, you can check that it stores native histograms: in the query field of the Prometheus web interface, enter

```promql
histogram_count(opencloud_proxy_request_duration_seconds)
```

If native histograms are enabled, this returns the number of requests that went through the proxy, for each combination of method, service and result. If it returns no data, native histograms are not enabled yet, or Prometheus hasn't scraped OpenCloud since.

### PromQL Examples

The following examples use the histogram of the Graph API requests, `opencloud_graph_http_request_duration_seconds`; they work the same way for every other classic histogram.

**The 99th percentile of the request duration** over the last 5 minutes, i.e. the duration that 99% of the requests didn't exceed:

```promql
histogram_quantile(0.99, sum by (le) (rate(opencloud_graph_http_request_duration_seconds_bucket[5m])))
```

The same, separately for each HTTP method: add the label to the `by` clause:

```promql
histogram_quantile(0.99, sum by (le, method) (rate(opencloud_graph_http_request_duration_seconds_bucket[5m])))
```

**The number of requests per second:**

```promql
sum(rate(opencloud_graph_http_request_duration_seconds_count[5m]))
```

**The average request duration:**

```promql
sum(rate(opencloud_graph_http_request_duration_seconds_sum[5m]))
  / sum(rate(opencloud_graph_http_request_duration_seconds_count[5m]))
```

**The share of requests that took at most 0.5 seconds**, for example for an alert when it drops below 95%. The threshold must be the upper bound of one of the buckets of the histogram:

```promql
sum(rate(opencloud_graph_http_request_duration_seconds_bucket{le="0.5"}[5m]))
  / sum(rate(opencloud_graph_http_request_duration_seconds_count[5m]))
```

### The Request Durations of the Proxy

The proxy service measures the duration of every request that goes through it, with three labels:

- `method`: the HTTP method;
- `service`: the service the request was forwarded to;
- `result`: the result, `success`, `client-error` or `server-error`.

All these combinations would result in a large number of time series as a classic histogram, so this histogram, `opencloud_proxy_request_duration_seconds`, is **only available as a native histogram**.

If native histograms are not enabled in Prometheus, it only stores the count and the sum of this histogram, and percentiles can't be calculated from it. For such setups, the proxy provides two additional metrics with fewer labels:

- `opencloud_proxy_service_duration_seconds`: a classic histogram with only the `service` label, for percentiles per service;
- `opencloud_proxy_service_request_total`: a counter with all three labels, for the number of requests per method, service and result.

For example, the 95th percentile of the request duration per service, with and without native histograms:

```promql
# without native histograms
histogram_quantile(0.95, sum by (le, service) (rate(opencloud_proxy_service_duration_seconds_bucket[5m])))

# with native histograms
histogram_quantile(0.95, sum by (service) (rate(opencloud_proxy_request_duration_seconds[5m])))
```

and the share of requests per service that resulted in a server error:

```promql
# without native histograms
sum by (service) (rate(opencloud_proxy_service_request_total{result="server-error"}[5m]))
  / sum by (service) (rate(opencloud_proxy_service_request_total[5m]))

# with native histograms
sum by (service) (histogram_count(rate(opencloud_proxy_request_duration_seconds{result="server-error"}[5m])))
  / sum by (service) (histogram_count(rate(opencloud_proxy_request_duration_seconds[5m])))
```

Note that the durations measured by the proxy include the transfer of the request and response bodies, so uploads and downloads of large files, and long-lived connections such as the ones for notifications, show up with long durations.

### List of the Duration Histograms

| Histogram                                                | Labels                                                    | Classic buckets | Native |
| -------------------------------------------------------- | --------------------------------------------------------- | --------------- | ------ |
| `opencloud_graph_http_request_duration_seconds`          | `method`, `path`, `version`, `resource`, `code`, `result` | default         | no     |
| `opencloud_graph_identity_backend_api_duration_seconds`  | `operation`, `result`, `type`                             | default         | no     |
| `opencloud_graph_ldap_client_operation_duration_seconds` | `operation`, `result`, `uri`, `write`                     | default         | no     |
| `opencloud_invitations_invitation_duration_seconds`      | none                                                      | default         | no     |
| `opencloud_webfinger_webfinger_duration_seconds`         | none                                                      | default         | no     |
| `opencloud_proxy_request_duration_seconds`               | `method`, `service`, `result`                             | none            | yes    |
| `opencloud_proxy_duration_seconds`                       | `method`                                                  | default         | no     |
| `opencloud_proxy_service_duration_seconds`               | `service`                                                 | default         | no     |
| `opencloud_search_search_duration_seconds`               | `status`                                                  | 0.1 to 60 s     | no     |
| `opencloud_search_index_duration_seconds`                | `status`                                                  | 0.1 to 1200 s   | no     |
| `opencloud_postprocessing_duration_seconds`              | `status`                                                  | 0.1 to 1200 s   | no     |

"default" means the default buckets of the Prometheus Go client library, from 0.005 to 10 seconds, as listed under [Classic Histograms](#classic-histograms).
