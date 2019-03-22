from scrapy import Spider
from scrapy.selector import HtmlXPathSelector
import csv


class ProductSpider(Spider):
    name = "parfum.de"
    allowed_domains = ["parfum.de"]
    start_urls = [
        "https://www.parfum.de/marken/gainsboro/?p=1&o=2&n=120",
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//div[@class="product--box box--minimal"]')

        with open('test.csv', 'w', newline="") as fp:
            writer = csv.writer(fp, delimiter=',')
            writer.writerow(["Product", "URL"])

            for site in sites:
                title = site.select('.//a[@class="product--brandline"]/text()')[0].extract()
                url = site.select('.//a[@class="product--brandline"]/@href')[0].extract()

                title = title[1:-1:]  # delete quotes from beginning and ending
                writer.writerows([(title, url)])
