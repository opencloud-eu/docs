---
title: 'Resource indicator extensions'
sidebar_position: 10
id: resource-indicator-extensions
---

## Extension Type ResourceIndicator

Resource indicator extensions add status icons or tags next to the name of a resource, for example in the resource
table. They are useful to show extra state of a file, folder or space, such as a lock or a label.

### Configuration

To define a resource indicator extension, you implement the `ResourceIndicatorExtension` interface. Here's what it looks
like:

```typescript
interface ResourceIndicatorExtension {
  id: string;
  type: 'resourceIndicator';
  extensionPointIds?: string[];
  getResourceIndicators: (resource: Resource) => ResourceIndicator[] | void;
}
```

For `id`, `type`, and `extensionPointIds`, please see [base configuration section](../index.md#base-configuration) in the extensions docs.

`getResourceIndicators` gets called for every rendered resource. Return an empty value if your extension has nothing to
show for the given resource. This function runs very often, so keep it cheap and return early where possible.

An indicator is either an icon or a tag:

```typescript
interface ResourceIndicatorIcon {
  id: string;
  kind: 'icon';
  label: string;
  accessibleDescription: string;
  type: string;
  category: 'system' | 'sharing' | 'space';
  icon: string;
  fillType: IconFillType;
  handler?: (resource: Resource, event?: MouseEvent) => void;
}

interface ResourceIndicatorTag {
  id: string;
  kind: 'tag';
  label: string;
  accessibleDescription: string;
  type: string;
  category: 'system' | 'sharing' | 'space';
  class?: string;
}
```

### Example

The following example adds a lock icon to every resource that is marked as read only.

```typescript title="src/extensions.ts"
const extension: ResourceIndicatorExtension = {
  id: 'com.github.opencloud-eu.web.app.resource-indicator.read-only',
  type: 'resourceIndicator',
  extensionPointIds: ['global.files.resource-indicator'],
  getResourceIndicators(resource) {
    if (resource.canRename()) {
      return;
    }

    return [
      {
        id: `read-only-${resource.id}`,
        kind: 'icon',
        label: $gettext('Read only'),
        accessibleDescription: $gettext('This item cannot be modified'),
        icon: 'lock-2',
        fillType: 'line',
        category: 'system',
        type: 'read-only'
      }
    ];
  }
};
```
