import scrapy

class DmozSpider(scrapy.Spider):
    name = 'xh'
    allowed_domains = ["xiaohuar.com"]
    urls ={
        'http://mydomain.com/',
    }
    def parse(self, response):
       filename =  response.url.split("/")[-2]
       with open(filename, 'wb') as f:
           f.write(response.body)