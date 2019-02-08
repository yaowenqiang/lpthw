import scrapy
class QoutesSpider(scrapy.Spider):
    name = "qoutes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
        ]


    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get()
            }
