import { resolve } from "node:path";
import { readdirSync } from "node:fs";
import handlebars from "vite-plugin-handlebars";
import { defineConfig } from "vite";

export default defineConfig({
  plugins: [
    // @ts-expect-error
    handlebars({
      partialDirectory: resolve(__dirname, "partials"),
    }),
  ],
  build: {
    rollupOptions: {
      input: readdirSync(__dirname)
        .filter((f) => f.endsWith(".html"))
        .map((f) => resolve(__dirname, f)),
    },
  },
});
