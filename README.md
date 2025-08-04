# 🧪 DeFiLlama Chains Web Scraper

This Python 3 project is a web scraper for (https://defillama.com/chains), which dynamically loads decentralized blockchain data. The script extracts three key statistics for each chain:

- **Name**  
- **Protocols (number of protocols supported)**  
- **TVL (Total Value Locked)**

The scraper is configurable via a YAML file and includes proxy support, flexible output format (JSON or CSV), robust error handling, and logging.

---

## 🚀 Features

- Parses dynamic content using **undetected-chromedriver** and **Selenium**
- Scrapes **Name**, **Protocols**, and **TVL** for each chain
- Fully configurable via `config.yaml`
- Proxy support (HTTP/HTTPS)
- Adjustable scraping interval
- Logs all scraping activities to file
- Error-resilient (fails gracefully)

---

## 📁 Project Structure
.
├── config.yaml # Configuration file

├── config_loader.py # YAML config loader

├── logger.py # Logging setup

├── main.py # Main script execution

├── scraper.py # Core scraping logic

├── logs/

│ └── scraper.log # Log output (created automatically)

├── data/

│ └── output.json # Output example

├── requirements.txt # Python dependencies

└── README.md # This file

### 1. Install dependencies

```bash
  pip install -r requirements.txt
```

### 2. Running the Scraper
```bash
  python main.py
```

