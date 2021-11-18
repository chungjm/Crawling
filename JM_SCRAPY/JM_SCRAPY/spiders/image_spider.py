import scrapy


class ImageSpider(scrapy.Spider):
    name = "image"

    def start_requests(self):
        urls = [
            'https://movie.naver.com/movie/running/current.naver',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        images = response.css('.thumb > a > img').xpath('@src').getall()
        yield {
            'image_urls': images
        }
