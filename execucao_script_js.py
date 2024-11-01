from selenium import webdriver

with open('um_javascript.js', 'r') as file:
    comando_js = file.read()

print(comando_js)

driver = webdriver.Chrome()

# fazer login antes

driver.get('localhost')

driver.execute_script(comando_js)
