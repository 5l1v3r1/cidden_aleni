import scrapy


class AymListeSayfasiSpider(scrapy.Spider):
    name = "aym_liste_sayfasi"
    allowed_domains = ["kararlarbilgibankasi.anayasa.gov.tr"]
    start_urls = ["https://kararlarbilgibankasi.anayasa.gov.tr"]

    def parse(self, response):
        pass
class DecisionScraper:
    def scrape_decisions(self):
        # Scrapes decisions from the Constitutional Court website
        pass

    def clean_data(self):
        # Cleans and preprocesses the scraped data
        pass
