# Notification

The notification service is responsible for sending emails to users informing them about events that happened. To do this, it hooks into the event system and listens for certain events that the users need to be informed about.

## Email Notification Templates

The `notifications` service has embedded email text and html body templates.

Email templates can use the placeholders `&#123;&#123; .Greeting &#125;&#125;`, `&#123;&#123; .MessageBody &#125;&#125;` and `&#123;&#123; .CallToAction &#125;&#125;` which are replaced with translations when sent, see the [Translations](#translations) section for more details. Though the email subject is also part of translations, it has no placeholder as it is a mandatory email component.

Depending on the email purpose, placeholders will contain different strings. An individual translatable string is available for each purpose, finally resolved by the placeholder. The embedded templates are available for all deployment scenarios.

```text
template
  placeholders
    translated strings &lt;-- source strings &lt;-- purpose
final output
```

In addition, the notifications service supports custom templates. Custom email templates take precedence over the embedded ones. If a custom email template exists, the embedded templates are not used. To configure custom email templates, the `NOTIFICATIONS_EMAIL_TEMPLATE_PATH` environment variable needs to point to a base folder that will contain the email templates and follow the [templates subfolder hierarchy](#templates-subfolder-hierarchy).This path must be available from all instances of the notifications service, a shared storage is recommended.
```text
&#123;NOTIFICATIONS_EMAIL_TEMPLATE_PATH&#125;/templates/text/email.text.tmpl
&#123;NOTIFICATIONS_EMAIL_TEMPLATE_PATH&#125;/templates/html/email.html.tmpl
&#123;NOTIFICATIONS_EMAIL_TEMPLATE_PATH&#125;/templates/html/img/
```
The source templates provided by OpenCloud you can derive from are located in the following base folder [https://github.com/opencloud-eu/opencloud/tree/main/services/notifications/pkg/email/templates](https://github.com/opencloud-eu/opencloud/tree/main/services/notifications/pkg/email/templates) with subfolders `templates/text` and `templates/html`.

-   [text/email.text.tmpl](https://github.com/opencloud-eu/opencloud/blob/main/services/notifications/pkg/email/templates/text/email.text.tmpl)
-   [html/email.html.tmpl](https://github.com/opencloud-eu/opencloud/blob/main/services/notifications/pkg/email/templates/html/email.html.tmpl)

### Templates subfolder hierarchy
```text
templates
│
└───html
│   │   email.html.tmpl
│   │
│   └───img
│       │   logo-mail.gif
│
└───text
    │   email.text.tmpl
```

Custom email templates referenced via `NOTIFICATIONS_EMAIL_TEMPLATE_PATH` must also be located in subfolder `templates/text` and `templates/html` and must have the same names as the embedded templates. It is important that the names of these files and folders match the embedded ones.
The `templates/html` subfolder contains a default HTML template provided by OpenCloud. When using a custom HTML template, hosted images can either be linked with standard HTML code like ```&lt;img src="https://raw.githubusercontent.com/opencloud-eu/opencloud/master/opencloud/img/logo-mail.gif" alt="logo-mail"/&gt;``` or embedded as a CID source ```&lt;img src="cid:logo-mail.gif" alt="logo-mail"/&gt;```. In the latter case, image files must be located in the `templates/html/img` subfolder. Supported embedded image types are png, jpeg, and gif.
Consider that embedding images via a CID resource may not be fully supported in all email web clients.

## Sending Grouped Emails

The `notification` service can initiate sending emails based on events stored in the configured store that are grouped into a `daily` or `weekly` bucket. These groups contain events that get populated e.g. when the user configures `daily` or `weekly` email notifications in his personal settings in the web UI. If a user does not define any of the named groups for notification events, no event is stored.

Grouped events are stored for the TTL defined in `OC_PERSISTENT_STORE_TTL`. This TTL can either be configured globally or individually for the notification service via the `NOTIFICATIONS_STORE_TTL` envvar.

Grouped events that have passed the TTL are removed automatically without further notice or sending!

To initiate sending grouped emails like via a cron job, use the `opencloud notifications send-email` command. Note that the command mandatory requires at least one option which is `--daily` or `--weekly`. Note that both options can be used together.

### Storing

The `notifications` service persists information via the configured store in `NOTIFICATIONS_STORE`. Possible stores are:
-   `memory`: Basic in-memory store. Will not survive a restart. This is not recommended for this service.
-   `redis-sentinel`: Stores data in a configured Redis Sentinel cluster.
-   `nats-js-kv`: Stores data using key-value-store feature of [nats jetstream](https://docs.nats.io/nats-concepts/jetstream/key-value-store). This is the default value.
-   `noop`: Stores nothing. Useful for testing. Not recommended in production environments.

Other store types may work but are not supported currently.

Note: The service can only be scaled if not using `memory` store and the stores are configured identically over all instances!

Note that if you have used one of the deprecated stores, you should reconfigure to one of the supported ones as the deprecated stores will be removed in a later version.

Store specific notes:
-   When using `redis-sentinel`, the Redis master to use is configured via e.g. `OC_CACHE_STORE_NODES` in the form of `&lt;sentinel-host&gt;:&lt;sentinel-port&gt;/&lt;redis-master&gt;` like `10.10.0.200:26379/mymaster`.
-   When using `nats-js-kv` it is recommended to set `OC_CACHE_STORE_NODES` to the same value as `OC_EVENTS_ENDPOINT`. That way the cache uses the same nats instance as the event bus.
-   When using the `nats-js-kv` store, it is possible to set `OC_CACHE_DISABLE_PERSISTENCE` to instruct nats to not persist cache data on disc.

## Translations

The `notifications` service has embedded translations sourced via transifex to provide a basic set of translated languages. These embedded translations are available for all deployment scenarios.

In addition, the service supports custom translations, though it is currently not possible to just add custom translations to embedded ones. If custom translations are configured, the embedded ones are not used. To configure custom translations,
the `NOTIFICATIONS_TRANSLATION_PATH` environment variable needs to point to a base folder that will contain the translation files. This path must be available from all instances of the notifications service, a shared storage is recommended. Translation files must be of type  [.po](https://www.gnu.org/software/gettext/manual/html_node/PO-Files.html#PO-Files) or [.mo](https://www.gnu.org/software/gettext/manual/html_node/Binaries.html). For each language, the filename needs to be `notifications.po` (or `notifications.mo`) and stored in a folder structure defining the language code. In general the path/name pattern for a translation file needs to be:

```text
&#123;NOTIFICATIONS_TRANSLATION_PATH&#125;/&#123;language-code&#125;/LC_MESSAGES/notifications.po
```

The language code pattern is composed of `language[_territory]` where  `language` is the base language and `_territory` is optional and defines a country.

For example, for the language `de`, one needs to place the corresponding translation files to `&#123;NOTIFICATIONS_TRANSLATION_PATH&#125;/de/LC_MESSAGES/notifications.po`.

&lt;!-- also see the userlog readme --&gt;

Important: For the time being, the embedded OpenCloud Web frontend only supports the main language code but does not handle any territory. When strings are available in the language code `language_territory`, the web frontend does not see it as it only requests `language`. In consequence, any translations made must exist in the requested `language` to avoid a fallback to the default.

### Translation Rules

*   If a requested language code is not available, the service tries to fall back to the base language if available. For example, if the requested language-code `de_DE` is not available, the service tries to fall back to translations in the `de` folder.
*   If the base language `de` is also not available, the service falls back to the system's default English (`en`),
which is the source of the texts provided by the code.

## Default Language

The default language can be defined via the `OC_DEFAULT_LANGUAGE` environment variable. See the `settings` service for a detailed description.
