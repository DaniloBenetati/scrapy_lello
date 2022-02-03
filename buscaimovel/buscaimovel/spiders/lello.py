import scrapy

start_urls = list()
for link in range(1, 609):
    url = (f'https://www.lelloimoveis.com.br/venda/residencial/apartamento-tipos/{link}-pagina/')
    start_urls.append(url)

class LelloSpider(scrapy.Spider):
    name = 'lello'
    start_urls = start_urls

    def parse(self, response):
        for imovel in response.css('.col-lg-4')[0:12]:
            yield{
                'valores': imovel.css('.mb-0.font-weight-bold::text').get(),
                'rua': imovel.css('.text-truncate.mb-0::text').get(),
                'bairro_cidade': imovel.css('.mt-1::text').get(),
                'link': response.xpath(
                    '//*[@id="__next"]/main/div[4]/div/div[1]/div[1]/div[1]/div/article/div[1]/div[1]/div/div/div/ul/li[2]/div/a').attrib[
                    'href']
            }


# scrapy crawl lello -O lello.csv para criar um arquivo do