from selenium import webdriver

# Instancia o WebDriver do Firefox usando o geckodriver
driver = webdriver.Firefox()

# Navega até a página desejada
driver.get('https://mozilla.org')

# Acessa o título da página e imprime-o
print(driver.title)

# espera por um input
le_variavel = input("digite alguma coisa para terminar: ")

# Fecha o navegador
driver.quit()