import { resolve } from "node:path";
import { readdirSync } from "node:fs";
import { defineConfig } from "vite";

export default defineConfig({
  build: {
    rollupOptions: {
      input: readdirSync(__dirname)
        .filter((f) => f.endsWith(".html"))
        .map((f) => resolve(__dirname, f)),
    },
  },
});
