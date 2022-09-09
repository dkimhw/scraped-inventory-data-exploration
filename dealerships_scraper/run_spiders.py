from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import spiders.stream_auto_outlet_spider as stream_auto_outlet_spider
import spiders.irwin_auto_group_spider as irwin_auto_group_spider
import spiders.ct_auto_spider as ct_auto_spider

def run_spider():
    process = CrawlerProcess(get_project_settings())
    try:
      # process.crawl(irwin_auto_group_spider.IrwinAutoGroupSpider)
      # process.crawl(stream_auto_outlet_spider.StreamAutoOutletSpider)
      process.crawl(ct_auto_spider.CTAutoSpider)
      process.start()
    except Exception as e:
      print(e)


if __name__  == '__main__':
  run_spider()