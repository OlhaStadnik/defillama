from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logger import setup_logger
import undetected_chromedriver as uc
import time

logger = setup_logger()


def scroll_to_bottom(driver, pause_time=1.0, max_scrolls=60):
    last_height = driver.execute_script("return document.body.scrollHeight")
    scrolls = 0

    while scrolls < max_scrolls:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break

        last_height = new_height
        scrolls += 1

    logger.info(f"Finished scrolling after {scrolls} iterations.")


def scrape_defillama_chains(proxy=None):
    options = uc.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # options.headless = True

    if proxy and proxy.get("use_proxy"):
        options.add_argument(f'--proxy-server={proxy["http"]}')
        logger.info(f"Using proxy: {proxy['http']}")

    driver = uc.Chrome(options=options)

    try:
        logger.info("Opening page...")
        driver.get("https://defillama.com/chains")

        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[style*='display: grid']"))
        )
        logger.info("Page loaded")
        scroll_to_bottom(driver)

        grid_rows = driver.find_elements(By.CSS_SELECTOR, "div[style*='display: grid']")
        logger.info(f"Found {len(grid_rows)} grid rows")

        result = []
        for row in grid_rows:
            cells = row.find_elements(By.XPATH, "./div")
            if len(cells) >= 7:
                try:
                    name = cells[0].find_element(By.TAG_NAME, "a").text.strip()
                except:
                    continue

                protocols = cells[1].text.strip()
                tvl = cells[6].text.strip()

                result.append({
                    "name": name,
                    "protocols": protocols,
                    "tvl": tvl
                })

        logger.info(f"Scraped {len(result)} chains")
        return result

    except Exception as e:
        logger.error(f"Scraping failed: {e}")
        return []

    finally:
        driver.quit()


