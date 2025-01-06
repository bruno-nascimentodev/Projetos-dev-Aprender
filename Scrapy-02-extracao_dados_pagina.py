# Importação de biblioteca
import scrapy


# Criação de classe com nome relevante para seu projeto
# sempre terminando com Spider 
class QuotesToScrapeSpider(scrapy.Spider):
    # Identidade da spider = nome do bot 
    name = "extrator"

    # Request = requisição feita ao site
    def start_requests(self):
        # Sites que serão varridos 
        urls = ['https://quotes.toscrape.com/']

        # Criação de laço de repetição que irá entrar em cada site e varre-los
        for url in urls:
            # yield = não aguarda o carregamento de todos os sites para obter os resultados  
            # Retorna os resultados a medida que vai encontrando, passando pelos links
            # url = local onde a varredura está ocorrendo 
            # callback = representa a função que vc quer que rode a cada repetição do for 
            # self.parse = função responsável de extrair os dados de uma página 
            yield scrapy.Request(url=url,callback=self.parse)
    
    
    # Response = resposta da requisição
    # Função que recebe a resposta retornada
    def parse(self, response):
        # Local de processamento do que será retornado da resposta
        # Crinado arquivo que receberá o resultado 
        for elemento in response.xpath("//div[@class='quote']"):
                yield {
                    'frase': elemento.xpath(".//span[@class='text']/text()").get(),
                    'author': elemento.xpath(".//small[@class='author']/text()").get(),
                    'tags': elemento.xpath(".//a[@class='tag']/text()").getall()
                }

        
