# sector-umbra.net with Astro.js

## 🚀 Project Structure

```text
/
├── public/        <-- Static assets such as images.
├── src/
│   └── layouts/   <-- Layout files. (Reusable layouts.)
│   └── md/        <-- Markdown content files. (Render these on the base layout with a pages/ component.)
│   └── pages/     <-- Route files. (Single components which render a page.)
│   └── styles/    <-- CSS files.
```

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                | Action                                           |
| :--------------------- | :----------------------------------------------- |
| `yarn`                 | Installs dependencies                            |
| `yarn dev`             | Starts local dev server at `localhost:4321`      |
| `yarn build`           | Build your production site to `./dist/`          |
| `yarn preview`         | Preview your build locally, before deploying     |
| `yarn astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `yarn astro -- --help` | Get help using the Astro CLI                     |
