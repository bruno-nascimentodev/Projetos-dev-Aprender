# DESAFIO 02
# 1 - Crie uma spider que navega até o site https://www.goodreads.com/quotes
# 2 - Extrair todas citações, autores e tags que estão em todas as páginas
# 3 - Exportar esse resultado para um arquivo CSV

# Importação de biblioteca
import scrapy


# Criação de classe com nome relevante para seu projeto
# sempre terminando com Spider 
class QuotesToScrapeSpider(scrapy.Spider):
    # Identidade da spider = nome do bot 
    name = "extrator_multi_pag_quotes"

    # Request = requisição feita ao site
    def start_requests(self):
        # Sites que serão varridos 
        urls = ['https://www.goodreads.com/quotes']


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
        # # 1 - Crie uma spider que navega até o site https://www.goodreads.com/quotes
        # # 2 - Extrai todas citações, autores e tags que estão na página
        # # 3 - Exporte esse resultado para um arquivo CSV
        for elemento in response.xpath("//div[@class='quote']"):
            yield {
                'frase': elemento.xpath(".//div[@class='quoteText']/text()").get(),
                'autor': elemento.xpath(".//span[@class='authorOrTitle']/text()").get(),
                'tags': elemento.xpath(".//div[@class='greyText smallText left']/a/text()").getall()
            }

        # Buscando botão de proxima página
        link_proxima_pag = response.xpath("//a[@rel='next']/@href").get()

        # Verificando se botão existe 
        try:
            if link_proxima_pag:
               link_completo = response.urljoin(link_proxima_pag)
               yield scrapy.Request(url=link_completo,callback=self.parse)
        except:
            print("Chegamos na última página")
              
        
