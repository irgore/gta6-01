import { copyFile, mkdir, stat } from "node:fs/promises";

await mkdir("/output", { recursive: true });
await copyFile("index.html", "/output/index.html");
const s = await (await import("node:fs/promises")).stat("/output/index.html");
console.log(`index.html → /output/index.html (${s.size} bytes)`);