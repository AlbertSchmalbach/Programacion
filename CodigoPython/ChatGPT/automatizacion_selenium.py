from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Configura el controlador del navegador (asegúrate de que tengas el controlador correcto instalado)
driver = webdriver.Chrome(executable_path='ruta_al_chromedriver.exe')  # Reemplaza con la ubicación de tu Chromedriver

# Navega a una página web
driver.get("https://www.ejemplo.com")

# Encuentra un campo de entrada y envía texto
campo_de_entrada = driver.find_element_by_name("nombre_del_campo")  # Reemplaza con el nombre o selector del campo
campo_de_entrada.send_keys("Texto de ejemplo")

# Envía una tecla "Enter" (opcional)
campo_de_entrada.send_keys(Keys.ENTER)

# Encuentra un botón y haz clic en él
boton_enviar = driver.find_element_by_id("id_del_boton")  # Reemplaza con el ID o selector del botón
boton_enviar.click()

# Puedes agregar más acciones aquí, como navegar a otras páginas, raspar datos, etc.

# Cierra el navegador al finalizar
driver.quit()
