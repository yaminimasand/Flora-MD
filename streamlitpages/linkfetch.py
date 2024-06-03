import requests
from bs4 import BeautifulSoup

def search_iffco_bazar(items):
    base_url = 'https://www.iffcobazar.in/en/search'

    # Create a dictionary to store links for each item
    item_links = {}

    for item in items:
        params = {'keyword': item}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

        try:
            response = requests.get(base_url, params=params, headers=headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            results = soup.find_all('div', class_='product-wrap')

            links = []
            for result in results:
                link_element = result.find('a', href=True)
                if link_element:
                    link = link_element['href']
                    links.append(link)

            item_links[item] = links
        except Exception as e:
            print(f"Error fetching IFFCO Bazar links for {item}: {e}")
            item_links[item] = []

    return item_links

# Example items for IFFCO Bazar
fertiliser_items = [
    "fertiliser",
    "organic fertiliser",
    "NPK fertiliser",
    "micronutrient fertiliser"
]

# Search IFFCO Bazar for fertiliser items
fertiliser_links_iffco = search_iffco_bazar(fertiliser_items)

# Print the results for IFFCO Bazar
print("\nFertiliser Links (IFFCO Bazar):")
for item, links in fertiliser_links_iffco.items():
    print(f"{item}: {links}")
