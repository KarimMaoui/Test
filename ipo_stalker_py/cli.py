import argparse
from .config import save_default_config
from .aggregator import aggregate_sources
from .digest import create_digest

def main():
    parser = argparse.ArgumentParser(description="IPO Stalker Python CLI")
    parser.add_argument("command", choices=["init", "run"], help="init config or run pipeline")
    args = parser.parse_args()

    if args.command == "init":
        save_default_config()
    elif args.command == "run":
        df = aggregate_sources()
        create_digest(df)

if __name__ == "__main__":
    main()
