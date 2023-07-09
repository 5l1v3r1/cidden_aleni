import scrapy
from scraping_code import extract_table_data, extract_decision_listing_data
from cddn_aln.items import KararItem, KararBilgiFormuItem, AramaSonucuItem
from toolkit import UserAgents
class DecisionListingScraper(scrapy.Spider):
    name = "aym_liste_sayfasi"
    allowed_domains = ["kararlarbilgibankasi.anayasa.gov.tr"]
    def start_requests(self):
        self.ua = UserAgents()
        self.headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                "authority": "www.vividseats.com",
                "User-Agent": self.ua.get_rand_UA(),
                'Accept-Encoding': 'gzip, deflate, br'
            }
        page1_url = 'https://kararlarbilgibankasi.anayasa.gov.tr/?page='
        yield scrapy.Request(
                    page1_url,
                    callback = self.parse_listing_page,
                    dont_filter =True,
                    headers = self.headers)
        

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
