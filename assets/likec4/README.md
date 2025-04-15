# OpenCloud C4 Model

This directory contains C4 model files for visualizing the OpenCloud architecture.

## Files

- `opencloud.c4`: Main system model defining components, relationships and views
- `specs.c4`: Specification of styles and notations
- `deployment.c4`: Deployment model showing Kubernetes resources

## Rendering Options

### Option 1: Using LikeC4 CLI (Recommended for .c4 files)

The `.c4` files in this directory appear to use the LikeC4 format, which can be rendered with the LikeC4 CLI:

1. Install LikeC4 CLI:
   ```bash
   pnpm install
   ```

2. Build the models:
   ```bash
   pnpm build-likec4
   ```

### Option 2: Using the LikeC4 Playground

1. Visit [https://likec4.dev/playground/](https://likec4.dev/playground/)
2. Copy and paste the contents of the .c4 files
3. Download the rendered diagrams
4. Include them in your documentation

## References

- [LikeC4 Documentation](https://likec4.dev/docs/introduction)
- [C4 Model](https://c4model.com/)

