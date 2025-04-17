# OpenCloud C4 Model

This directory contains C4 model files for visualizing the OpenCloud architecture using the LikeC4 modeling language.

## Overview

The C4 model provides a way to visualize software architecture at different levels of abstraction:
- **Context**: Shows how the system interacts with users and other systems
- **Containers**: Shows the high-level technology choices and how containers communicate
- **Components**: Shows how a container is made up of components
- **Code**: Shows how a component is implemented (optional)

Our LikeC4 implementation uses a text-based DSL (Domain Specific Language) to define these models, making them version-control friendly and easier to maintain than diagrams.

## Files

- `opencloud.c4`: Main system model defining components, relationships and views
- `spec.c4`: Specification of styles and notations
- `deployment.c4`: Deployment model showing Kubernetes resources and topology

## Viewing the Diagrams

The rendered diagrams are deployed at:
- **https://docs.opencloud.eu/likec4/**

These are automatically generated during the build process and updated with each deployment.

## Rendering the Diagrams

### Option 1: Using the Project Build Tool (Recommended)

The project has a built-in script to render the C4 models:

```bash
# Install dependencies
pnpm install

# Build the LikeC4 diagrams
pnpm build-likec4
```

This will generate the diagrams in the `/static/likec4/` directory which will be included in the built documentation site.

### Option 2: Using the LikeC4 Playground

For quick edits and visualization:

1. Visit [https://likec4.dev/playground/](https://likec4.dev/playground/)
2. Copy and paste the contents of the `.c4` files
3. Visualize in real-time and export diagrams as needed

## Modifying the Models

When modifying the C4 models:

1. Make changes to the relevant `.c4` files
2. Run `pnpm build-likec4` to regenerate the diagrams
3. Preview the changes in the documentation site with `pnpm start`
4. Commit both the `.c4` source files and the generated diagrams

## References

- [LikeC4 Documentation](https://likec4.dev/docs/introduction)
- [C4 Model](https://c4model.com/)
- [The C4 Model for Software Architecture](https://www.infoq.com/articles/C4-architecture-model/)