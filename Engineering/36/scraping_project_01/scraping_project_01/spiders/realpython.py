import scrapy


class RealpythonSpider(scrapy.Spider):
    name = 'realpython'
    allowed_domains = ['olympus.realpython.org']
    start_urls = ['http://olympus.realpython.org/profiles/aphrodite']

    def parse(self, response):
        # Use response.css to fetch text from CSS
        # Use response.xpath to fetch content from XPath
        title = response.xpath("/html/body/center/h2").get()
        return {"title": title}
