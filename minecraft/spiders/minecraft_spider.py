import scrapy

class MobsSpider(scrapy.Spider):
    name = 'mobs'

    def start_requests(self):
        urls = [
            'https://minecraft.fandom.com/wiki/Mob'
        ]

        scrapy.Request(url=urls[0], callback=self.parse)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.get_mobs_links)

    def get_mobs_links(self, response):
        names = response.css('td>a::attr(href)').getall()
        for name in names:
            next_page = response.urljoin(name)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse(self, response):
        print(response.css('.notaninfobox>table').get())