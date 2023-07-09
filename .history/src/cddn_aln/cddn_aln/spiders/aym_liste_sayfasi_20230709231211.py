import scrapy
from scraping_code import extract_table_data, extract_decision_listing_data
from cddn_aln.items import KararItem, KararBilgiFormuItem, AramaSonucuItem

class DecisionScraper(scrapy.Spider):
    name = "aym_liste_sayfasi"
    allowed_domains = ["kararlarbilgibankasi.anayasa.gov.tr"]
    start_urls = ["https://kararlarbilgibankasi.anayasa.gov.tr"]

    def parse_listing_page(self, response):
        item = AramaSonucuItem()
        links = response.xpath('//titles/a').getall()
        results = response.xpath('//div[@class="karargoruntulemealani col-sm-12"]/div[@class="birkarar col-sm-12"]')





    def parse_decision_page(self, response):
        pass
        table = response.xpath('//*[@class="table"]')
        karar_bilgi_formu_values = extract_table_data(table)
