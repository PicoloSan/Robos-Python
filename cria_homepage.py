# Importando as bibliotecas necessárias
import htmlgen
import time
from selenium import webdriver

# Cria um documento HTML
doc = htmlgen.Document("Exemplo de Uso HTMLgen")

# Cria um parágrafo com um link
paragrafo = htmlgen.Paragraph("Este é um exemplo de uso da biblioteca HTMLgen. Veja a documentação completa em ")
paragrafo.append(htmlgen.Link('https://github.com/marcelom-ags/HTMLgen', 'GitHub'))
doc.append_body(paragrafo)

# Gera a representação em HTML do documento
html_content = doc.__str__()

# Escreve o conteúdo HTML em um arquivo
with open('exemplo.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

# Configuração do WebDriver
driver = webdriver.Chrome()

# Abre o arquivo HTML no WebDriver
driver.get('file:///c:/users/cmp010/downloads/exemplo.html')

# Aguarda 1 minuto e 30 segundos
time.sleep(90)

# Fecha o WebDriver
driver.quit()
