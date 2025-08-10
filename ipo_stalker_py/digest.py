from pathlib import Path
from .config import load_config

def create_digest(df):
    cfg = load_config()
    digest_dir = Path(cfg["digest_dir"])
    digest_dir.mkdir(parents=True, exist_ok=True)

    lines = ["# IPO Digest\n"]
    for _, row in df.iterrows():
        lines.append(f"- {row['date']}: {row['company']} ({row['source']})")

    digest_path = digest_dir / "digest.md"
    with open(digest_path, "w") as f:
        f.write("\n".join(lines))

    print(f"Digest saved to {digest_path}")
