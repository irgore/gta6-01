import { existsSync, mkdirSync, readFileSync, writeFileSync, readdirSync, statSync } from "node:fs";
import { join } from "node:path";

const OUT = process.env.OUTPUT_DIR || "/output";
if (!existsSync(OUT)) mkdirSync(OUT, { recursive: true });

// Copy game files to output
const files = ["index.html"];
for (const f of files) {
  const src = join(process.cwd(), f);
  if (existsSync(src)) {
    writeFileSync(join(OUT, f), readFileSync(src));
    console.log(`Copied: ${f} (${readFileSync(src).length} bytes)`);
  }
}

// This is a single-file static game — no build step needed
// Entry point = index.html
console.log("GTA VI: Leonida Nights ready");
console.log(`Output: ${OUT}/index.html`);