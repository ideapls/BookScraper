# BookScraper
O objetivo deste projeto é realizar a leitura de um site que disponibiliza dados de livros para scrapping, e armazenar os dados dos livros em um arquivo json.

Para rodar o código basta digitar:

<code> scrapy runspider .\crawling_spider.py </code>

Caso queira armazenar o resultado e um arquivo de saída basta digitar:

<code> scrapy runspider .\crawling_spider.py -o output.json </code>

A atualização mais recente do código adiciona um arquivo de conexão com o banco de dados, ocultando o login e a senha nas váriaveis de ambiente.
