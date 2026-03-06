# Scraper functionality

import requests

class Scraper:
    def fetch_data(self, url):
        response = requests.get(url)
        return response.text

scraper = Scraper()