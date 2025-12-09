from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
# -----------------------------------------------------------------------


driver.get("https://univirtus.uninter.com/ava/web/")


wait = WebDriverWait(driver, 20)
print("🔎 Aguardando o formulário de login carregar...")


wait.until(EC.visibility_of_element_located((By.ID, "ru")))


campo_ru = driver.find_element(By.ID, "ru")
campo_senha = driver.find_element(By.ID, "senha")

#DIGITE SEU RU AQUI EM BAIXO
campo_ru.send_keys("DigiteRUaqui")
#Digite sua senha aqui em baixo
campo_senha.send_keys("DigiteSenhaAqui")
print("✅ Credenciais preenchidas.")



print("➡️ Simulando a tecla Enter para realizar o login...")
campo_senha.send_keys(Keys.RETURN)


print("Página pós-login carregada.")




print("🔄 Diminuindo o zoom da página (simulando Ctrl -)...")


zoom_level = 0.75
driver.execute_script(f"document.body.style.zoom = '{zoom_level}'")

print(f"Zoom da página ajustado para {int(zoom_level * 100)}%.")


# =========================================================================

print("\n\n✅ Login automático e ajuste de zoom COMPLETO e BEM-SUCEDIDO!")
print("Navegador aberto para sua navegação.")


time.sleep(9999999)