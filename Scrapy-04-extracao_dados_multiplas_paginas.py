# Importação de biblioteca
import scrapy


# Criação de classe com nome relevante para seu projeto
# sempre terminando com Spider 
class QuotesToScrapeSpider(scrapy.Spider):
    # Identidade da spider = nome do bot 
    name = "extrator_multi_pag"

    # Request = requisição feita ao site
    def start_requests(self):
        # Sites que serão varridos 
        urls = ['https://quotes.toscrape.com/']


        # Criação de laço de repetição que irá entrar em cada site e varre-los
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    
    # Response = resposta da requisição
    # Função que recebe a resposta retornada
    def parse(self, response):
        for elemento in response.xpath("//div[@class='quote']"):
            yield {
                'frase': elemento.xpath(".//span[@class='text']/text()").get(),
                'author': elemento.xpath(".//small[@class='author']/text()").get(),
                'tags': elemento.xpath(".//a[@class='tag']/text()").getall()
            }

        # Buscando o botao da proxima página
        link_proxima_pag = response.xpath("//li[@class='next']/a/@href").get()      
        # Verificando se botão existe e clicando nele
        try:
            if link_proxima_pag:
                link_completo = response.urljoin(link_proxima_pag)
                yield scrapy.Request(url=link_completo,callback=self.parse)
        except:
            # Caso o Botão não exista
            print("Chegamos na última página")
        
