# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CddnAlnPipeline:
    def process_item(self, item, spider):
        return item
class


class DecisionDatabase:
    def save_decision(self, decision):
        # Saves decision data to a database
        pass

    def retrieve_decision(self, decision_id):
        # Retrieves decision data from the database
        pass
