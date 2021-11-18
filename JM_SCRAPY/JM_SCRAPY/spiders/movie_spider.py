import scrapy


class MovieSpider(scrapy.Spider):
    name = "movie"

    def start_requests(self):
        urls = [
            'https://movie.naver.com/movie/running/current.naver',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = {}
        movie_sels = response.css('ul.lst_detail_t1 > li')
        for movie_sel in movie_sels:
            # 영화제목
            item['title'] = movie_sel.css('.tit > a::text').get()
            # 나이제한
            item['age_limit'] = movie_sel.css('.tit > span::text').get()
            # 평점
            item['rating'] = movie_sel.css(
                '.star_t1 > a > span.num::text').get()
            # 평점 참여자 수
            item['rating_count'] = movie_sel.css(
                '.star_t1 > a > span.num2>em::text').get()
            yield item
