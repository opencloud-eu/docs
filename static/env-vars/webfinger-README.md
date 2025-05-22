# Webfinger

The webfinger service provides an RFC7033 WebFinger lookup of OpenCloud instances relevant for a given user account via endpoints a the /.well-known/webfinger implementation.

## OpenID Connect Discovery

Clients can make an unauthenticated `GET https://drive.opencloud.test/.well-known/webfinger?resource=https%3A%2F%2Fdrive.opencloud.test` request to discover the OpenID Connect Issuer in the `http://openid.net/specs/connect/1.0/issuer` relation:

```json
&#123;
    "subject": "https://drive.opencloud.test",
    "links": [
        &#123;
            "rel": "http://openid.net/specs/connect/1.0/issuer",
            "href": "https://sso.example.org/cas/oidc/"
        &#125;
    ]
&#125;
```

Here, the `resource` takes the instance domain URI, but an `acct:` URI works as well. 

## Authenticated Instance Discovery

When using OpenID connect to authenticate requests, clients can look up the opencloud instances a user has access to.

*   Authentication is necessary to prevent leaking information about existing users.
*   Basic auth is not supported.

The default configuration will simply return the `OC_URL` and direct clients to that domain:

```json
&#123;
    "subject": "acct:alan@drive.opencloud.test",
    "links": [
        &#123;
            "rel": "http://openid.net/specs/connect/1.0/issuer",
            "href": "https://sso.example.org/cas/oidc/"
        &#125;,
        &#123;
            "rel": "http://webfinger.opencloud/rel/server-instance",
            "href": "https://abc.drive.example.org",
            "titles": &#123;
                "en": "OpenCloud Instance"
            &#125;
        &#125;
    ]
&#125;
```

## Configure Different Instances Based on OpenidConnect UserInfo Claims

A more complex example for configuring different instances could look like this:

```yaml
webfinger:
  instances:
  -  claim: email
     regex: alan@example\.org
     href: "https://&#123;&#123;.preferred_username&#125;&#125;.cloud.opencloud.test"
     title: 
       "en": "OpenCloud Instance for Alan"
       "de": "OpenCloud Instanz für Alan"
     break: true
  -  claim: "email"
     regex: mary@example\.org
     href: "https://&#123;&#123;.preferred_username&#125;&#125;.cloud.opencloud.test"
     title: 
       "en": "OpenCloud Instance for Mary"
       "de": "OpenCloud Instanz für Mary"
     break: false
  -  claim: "email"
     regex: .+@example\.org
     href: "https://example-org.cloud.opencloud.test"
     title:
       "en": "OpenCloud Instance for example.org"
       "de": "OpenCloud Instanz für example.org"
     break: true
  -  claim: "email"
     regex: .+@example\.com
     href: "https://example-com.cloud.opencloud.test"
     title:
       "en": "OpenCloud Instance for example.com"
       "de": "OpenCloud Instanz für example.com"
     break: true
  -  claim: "email"
     regex: .+@.+\..+
     href: "https://cloud.opencloud.test"
     title:
       "en": "OpenCloud Instance"
       "de": "OpenCloud Instanz"
     break: true
```

Now, an authenticated webfinger request for `acct:me@example.org` (when logged in as mary) would return two instances, based on her `email` claim, the regex matches and break flags:

```json
&#123;
    "subject": "acct:mary@example.org",
    "links": [
        &#123;
            "rel": "http://openid.net/specs/connect/1.0/issuer",
            "href": "https://sso.example.org/cas/oidc/"
        &#125;,
        &#123;
            "rel": "http://webfinger.opencloud/rel/server-instance",
            "href": "https://mary.cloud.opencloud.test",
            "titles": &#123;
                "en": "OpenCloud Instance for Mary",
                "de": "OpenCloud Instanz für Mary"
            &#125;
        &#125;,
        &#123;
            "rel": "http://webfinger.opencloud/rel/server-instance",
            "href": "https://xyz.drive.example.org",
            "titles": &#123;
                "en": "OpenCloud Instance for example.org",
                "de": "OpenCloud Instanz für example.org"
            &#125;
        &#125;
    ]
&#125;
```
