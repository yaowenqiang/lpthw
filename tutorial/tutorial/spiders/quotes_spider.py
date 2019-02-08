import scrapy
class QoutesSpider(scrapy.Spider):
    name = "qoutes"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url,self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            self.log('parse')
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
            self.log('parse')

        #  next_page = response.css('li.next a::attr(href)').get()
        #  if next_page is not None:
            #  next_page = response.urljoin(next_page)
            #  yield scrapy.Request(next_page, callback=self.parse)
