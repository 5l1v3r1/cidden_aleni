import scrapy
from scraping_code import extract_table_data


class DecisionScraper(scrapy.Spider):
    name = "aym_liste_sayfasi"
    allowed_domains = ["kararlarbilgibankasi.anayasa.gov.tr"]
    start_urls = ["https://kararlarbilgibankasi.anayasa.gov.tr"]

    def parse_listing_page(self, response):
        pass
    def parse_decision_page(self, response):
        pass
        table = response.xpath('//*[@class="table"]')
