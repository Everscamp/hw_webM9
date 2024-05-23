import scrapy


class AuthorsSpider(scrapy.Spider):
    name = 'authors'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        for quote in response.xpath("/html//div[@class='quote']"):
            next_links = quote.xpath("//html//div[@class='quote']/span/a/@href").extract()
            for link in next_links:
                yield scrapy.Request(url=self.start_urls[0] + link, callback=self.access_details)

    def access_details(self, response):
        for auth in response.xpath("/html//div[@class='author-details']"):
            yield {
                "fullname": auth.xpath("h3[@class='author-title']/text()").extract(),
                "born_date": auth.xpath("p/span[@class='author-born-date']/text()").extract(),
                "born_location": auth.xpath("p/span[@class='author-born-location']/text()").extract(),
                "description": auth.xpath("div[@class='author-description']/text()").extract()
            }
