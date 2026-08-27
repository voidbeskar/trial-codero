"""
Simple Web Scraper
-------------------
Scrape kutipan (quotes) dari https://quotes.toscrape.com
lalu simpan hasilnya ke file CSV.

Install dulu library yang dibutuhkan:
    pip install requests beautifulsoup4
"""

import csv
import requests
from bs4 import BeautifulSoup


BASE_URL = "https://quotes.toscrape.com/page/{}/"


def scrape_page(page_number):
    """Ambil semua quote dari satu halaman."""
    url = BASE_URL.format(page_number)
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    quote_blocks = soup.find_all("div", class_="quote")

    results = []
    for block in quote_blocks:
        text = block.find("span", class_="text").get_text(strip=True)
        author = block.find("small", class_="author").get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in block.find_all("a", class_="tag")]

        results.append({
            "text": text,
            "author": author,
            "tags": ", ".join(tags)
        })

    return results


def scrape_all_pages(max_pages=5):
    """Scrape beberapa halaman sekaligus."""
    all_quotes = []

    for page in range(1, max_pages + 1):
        print(f"Scraping halaman {page}...")
        quotes = scrape_page(page)

        if not quotes:
            print("Tidak ada data lagi, berhenti.")
            break

        all_quotes.extend(quotes)

    return all_quotes


def save_to_csv(data, filename="quotes.csv"):
    """Simpan hasil scraping ke file CSV."""
    if not data:
        print("Tidak ada data untuk disimpan.")
        return

    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["text", "author", "tags"])
        writer.writeheader()
        writer.writerows(data)

    print(f"Berhasil menyimpan {len(data)} quote ke '{filename}'")


if __name__ == "__main__":
    quotes = scrape_all_pages(max_pages=5)
    save_to_csv(quotes)