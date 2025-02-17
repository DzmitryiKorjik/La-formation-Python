import json
from pprint import pprint
import time
import requests

def get_all_urls():
    page_number = 1
    links = []
    while True:
        url = f"https://genius.com/api/search/song?page={page_number}&q=Patrick+B"
        res = requests.get(url)

        print(f"Fetching page {page_number} - Status:", res.status_code)

        if res.status_code == 200:
            response = res.json().get("response", {})

            next_page = response.get("next_page", None)
            sections = response.get("sections", [])

            for section in sections:
                if "hits" in section:
                    for song in section["hits"]:
                        url = song["result"].get("url")
                        if url:
                            links.append(url)

                # pprint(links)
                # print("Total links found:", len(links))

            if not next_page:
                # print("No more pages to fetch")
                break

            page_number += 1
            time.sleep(1)
    return links

def save_links_to_file():
    urls = get_all_urls()
    with open("data_links.json", "w", encoding="utf-8") as f:
        json.dump(urls, f, ensure_ascii=False, indent=4)
    print(f"Saved {len(urls)} links to data_links.json")

save_links_to_file()