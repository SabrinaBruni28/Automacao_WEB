import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Site que será aberto
url = "https://caldeirao.onrender.com/"  # Substitua pelo site desejado

# Configurar o Chrome com modo headless
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Rodar sem abrir janela
options.add_argument("--disable-gpu")  # Recomendado no Windows
options.add_argument("--no-sandbox")  # Necessário em alguns ambientes Linux
options.add_argument("--window-size=1920,1080")  # Define tamanho da tela virtual

print(f"Abrindo o site (modo headless): {url}")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url)

# Esperar 60 segundos
time.sleep(60)

# Fecha o navegador
driver.quit()
