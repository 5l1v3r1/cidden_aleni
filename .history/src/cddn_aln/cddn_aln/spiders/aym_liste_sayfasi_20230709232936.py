import scrapy
from scraping_code import extract_table_data, extract_decision_listing_data
from cddn_aln.items import KararItem, KararBilgiFormuItem, AramaSonucuItem

class DecisionListingScraper(scrapy.Spider):
    name = "aym_liste_sayfasi"
    allowed_domains = ["kararlarbilgibankasi.anayasa.gov.tr"]
    start_urls = ["https://kararlarbilgibankasi.anayasa.gov.tr"]

    def parse_listing_page(self, response):
        item = AramaSonucuItem()
        decisions = extract_decision_listing_data(response)
        current_page = response.xpath('//li[@class="active"]/span/text()').get()
        for decision in decisions:
            item['title'] = decision['title']
            item['summary'] = decision['topic']
            item['link'] = decision['link']
            item['page'] = current_page
            item['details'] = decision['detailed_info']
            yield item

            







    def parse_decision_page(self, response):
        pass
        table = response.xpath('//*[@class="table"]')
        karar_bilgi_formu_values = extract_table_data(table)
