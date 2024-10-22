from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicialize o WebDriver (neste exemplo, será utilizado o Chrome)
driver = webdriver.Chrome()

# Abra a URL da página da web que você deseja verificar
driver.get('https://www.exemplo.com')

try:
    # Verifique se o elemento <div> está presente na página
    div_element = driver.find_element(By.CSS_SELECTOR, 'div.sua-classe')
    # <span class="show list class1">
    # Encontre o elemento pelo seletor CSS show, list e class1
    # element = driver.find_element(By.CSS_SELECTOR, '.show.list.class1')
    # Encontre o elemento pelo seletor CSS show e class1
    # element = driver.find_element(By.CSS_SELECTOR, '[class*="show"][class*="class1"]')


    print("A <div> está presente na página.")
except NoSuchElementException:
    print("A <div> não está presente na página.")

# Feche o navegador
driver.quit()

"""==============================================================================================================="""


from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicialize o WebDriver (neste exemplo, será utilizado o Chrome)
driver = webdriver.Chrome()

# Abra a URL da página da web que você deseja manipular
driver.get('https://www.exemplo.com')

# Encontre o elemento pelo seletor CSS
element = driver.find_element(By.CSS_SELECTOR, '.seu-seletor-css')

# Adicione uma classe ao elemento através da propriedade class_name
element_class = element.get_attribute('class')
element_class += ' nova-classe'
driver.execute_script("arguments[0].setAttribute('class', arguments[1]);", element, element_class)

# Feche o navegador
driver.quit()

"""==============================================================================================================="""


from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicialize o WebDriver (neste exemplo, será utilizado o Chrome)
driver = webdriver.Chrome()

# Abra a URL da página da web que você deseja manipular
driver.get('https://www.exemplo.com')

# Encontre o elemento pelo seletor CSS
element = driver.find_element(By.CSS_SELECTOR, '.seu-seletor-css')

# Remova uma classe do elemento através da propriedade class_name
element_class = element.get_attribute('class')
element_class = element_class.replace('classe-a-remover', '')
driver.execute_script("arguments[0].setAttribute('class', arguments[1]);", element, element_class)

# Feche o navegador
driver.quit()
