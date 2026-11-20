import { copyFile, mkdir } from "node:fs/promises";

await mkdir("/output", { recursive: true }).catch(() => {});
try {
  await copyFile("index.html", "/output/index.html");
  console.log("index.html → /output/index.html");
} catch {
  console.log("index.html kept in repo (sandbox: /output read-only)");
}