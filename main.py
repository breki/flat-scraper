import spider

class NepremicnineSpider(scrapy.Spider):
    def parse(self, response):
        for href in response.css('.oglasi .oglas a::attr(href)'):
            yield response.follow(href, self.parse_ad)

        for href in response.css('.pagination a::attr(href)'):
            yield response.follow(href, self.parse)


if __name__ == '__main__':
    # https://www.nepremicnine.net/oglasi-prodaja/podravska/maribor/stanovanje/2-sobno,2.5-sobno,3-sobno/
    ...
