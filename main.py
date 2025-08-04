from scraper import scrape_defillama_chains
from config_loader import load_config
import json
import csv
import time
import os


def save_data(data, config):
    fmt = config["output"]["format"]
    path = config["output"]["path"]
    os.makedirs(os.path.dirname(path), exist_ok=True)

    if fmt == "json":
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    elif fmt == "csv":
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "protocols", "tvl"])
            writer.writeheader()
            writer.writerows(data)


if __name__ == "__main__":
    config = load_config()
    interval = config["scrape_interval_minutes"]

    while True:
        print("[RUNNING] Scraping started")
        data = scrape_defillama_chains(proxy=config["proxy"])
        save_data(data, config)
        print(f"[DONE] Sleeping for {interval} minutes...\n")
        time.sleep(interval * 60)

