---
title: 'Vault extensions'
sidebar_position: 11
id: vault-extensions
---

## Extension Type Vault

Vault extensions add a client side encryption scheme to OpenCloud Web. A vault is a folder or a space whose content, and
usually also whose resource names, are encrypted in the browser before they reach the server.

The Web runtime stays scheme-agnostic. It only knows that some location is a vault and whether it is unlocked. All
cryptography, all key handling and the unlock user interface come from the extension.

:::note
This extension type is meant for encryption schemes. If you only want to add functionality to a vault, use one of the
other extension types instead. A reference implementation is the
[rclone-crypt app](https://github.com/opencloud-eu/web/tree/main/packages/web-app-rclone-crypt).
:::

### Configuration

To define a vault extension, you implement the `VaultExtension` interface. Here's what it looks like:

```typescript
interface VaultExtension {
  id: string;
  type: 'vault';
  extensionPointIds?: string[];
  claimsPath: (space: SpaceResource, path: string) => VaultClaim | null;
  resolve: (space: SpaceResource, path: string) => Promise<VaultEngine | null>;
  creation?: VaultCreation;
}
```

For `id`, `type`, and `extensionPointIds`, please see [base configuration section](../index.md#base-configuration) in the extensions docs.

- `claimsPath` - Tells the runtime if your extension is responsible for the given location, no matter if the vault is
  unlocked. This is a cheap, synchronous check. Return `null` if the location is not one of your vaults.
- `resolve` - Returns the engine that encrypts and decrypts for the given location. Return `null` if your extension is
  not responsible, or if the vault is locked.
- `creation` - Optional. Its presence tells the user interface that your extension can create new vaults, so an
  encryption option is offered when a user creates a folder or a space.

#### VaultClaim

```typescript
interface VaultClaim {
  vaultRoot: string;
  encryptsNames: boolean;
  unlockRoute?: RouteLocationNamedRaw;
}
```

- `vaultRoot` - The clear text root of the vault, for example `/my-vault.vault`. Use `/` for a vault space.
- `encryptsNames` - Set this to `true` if your scheme also encrypts resource names, not just their content.
- `unlockRoute` - The route that asks the user to unlock the vault. Your route handler fills the vault store and then
  redirects back to `query.redirectUrl`. Without this route the vault is treated as permanently locked.

#### VaultEngine

The engine does the actual cryptography. All of its path methods work on paths that are relative to the vault root. A
bare resource name is a relative path with one segment, so a name must encrypt independently of its position in the tree.

```typescript
interface VaultEngine {
  vaultRoot: string;
  encryptPath: (relativePath: string) => Promise<string>;
  decryptPath: (relativePath: string) => Promise<string>;
  encryptContent: (plaintext: ReadableStream<Uint8Array>) => ReadableStream<Uint8Array>;
  decryptContent: (encrypted: ReadableStream<Uint8Array>) => ReadableStream<Uint8Array>;
  createIntegrityToken: () => Promise<string>;
  verifyIntegrityToken: (token: string) => Promise<boolean>;
  verifySegment: (sampleEncryptedSegment: string) => Promise<boolean>;
}
```

The integrity token commits a vault to the key of your engine. It gets written once, when the secret of a vault is first
set, and it is stored as a WebDAV property on the vault root. Its format is up to your engine. `verifySegment` is the
weaker fallback for vaults that carry no token, for example vaults created outside of OpenCloud Web.

If you have full clear text paths, use the `encryptVaultPath` and `decryptVaultPath` helpers from `web-pkg` instead of
calling the engine directly.

#### VaultCreation

```typescript
interface VaultCreation {
  vaultExtension: string;
  vaultContentType: string;
  setupComponent: Component;
}
```

- `vaultExtension` - The name extension a vault folder carries, without the leading dot, for example `vault`.
- `vaultContentType` - The content type a vault space carries in its `@libre.graph.contentType` drive property.
- `setupComponent` - The component that collects and commits the secret of a new vault. It is rendered as the second
  step of the create folder or create space flow. It takes a `vaultName` prop, emits `update:valid`, and exposes a
  `finalize` function that gets called once the folder or space exists on the server.

### Example

```typescript title="src/extensions.ts"
import { markRaw } from 'vue';
import { VaultExtension } from '@opencloud-eu/web-pkg';
import VaultSetup from './components/VaultSetup.vue';

export const vaultSchemeExtension: VaultExtension = {
  id: 'app.rclone-crypt.vault',
  type: 'vault',
  resolve(space, path) {
    return Promise.resolve(resolveVault(space, path));
  },
  claimsPath(space, path) {
    return claimsVaultPath(space, path);
  },
  creation: {
    vaultExtension: 'vault',
    vaultContentType: 'application/vnd.opencloud.vault',
    setupComponent: markRaw(VaultSetup)
  }
};
```
