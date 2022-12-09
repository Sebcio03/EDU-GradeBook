import { defineConfig, loadEnv } from "vite";
import vue from "@vitejs/plugin-vue";


export default defineConfig(({mode}) => {
  const env = loadEnv(mode, "env");
  console.log(`Using env mode ${mode}`, env);
  return {
    plugins: [vue()],
  };
});