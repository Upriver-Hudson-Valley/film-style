# Local LUTs (Gitignored)

Licensed `.cube` LUT files are intentionally excluded from git. Copy your local LUT files into this folder before running the skill:

- `CLOGOrion.cube` — Raw / Canon Log (C-Log / C-Log3) input look
- `Orion.cube` — Rec.709 finishing look (applied after `out-rec709.ctf` in ACEScct `openfilm color match` chains)

See `../../references/style-bible.md` for the exact `--of-lut` chain ordering.
