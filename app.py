from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Função para iniciar o WhatsApp Web e fazer login
def iniciar_whatsapp():
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=./User_Data")  # Usar perfil do Chrome para não precisar escanear QR Code a cada execução
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("https://web.whatsapp.com/")
    print("Escaneie o QR Code para entrar no WhatsApp Web.")
    time.sleep(15)  # Aguarda 15 segundos para o login (ajuste conforme necessário)
    
    return driver

# Função para enviar mensagem a um contato específico
def enviar_mensagem(driver, contato, mensagem):
    # Localiza o campo de pesquisa e busca o contato
    search_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='3']")
    search_box.click()
    search_box.send_keys(contato)
    time.sleep(2)  # Espera um pouco para a pesquisa
    search_box.send_keys(Keys.ENTER)
    
    # Envia a mensagem
    message_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='1']")
    message_box.click()
    message_box.send_keys(mensagem)
    message_box.send_keys(Keys.ENTER)
    print(f"Mensagem enviada para {contato}: {mensagem}")

# Função para simular o chatbot (resposta simples)
def chatbot_resposta(mensagem_usuario):
    respostas = {
        "olá": "Olá! Como posso ajudá-lo?",
        "tchau": "Até logo!",
        "como você está?": "Estou bem, obrigado! E você?"
    }
    return respostas.get(mensagem_usuario.lower(), "Desculpe, não entendi.")

def main():
    driver = iniciar_whatsapp()

    try:
        while True:
            # Simula um loop de conversa
            mensagem_usuario = input("Digite uma mensagem para o chatbot (ou 'sair' para encerrar): ")
            if mensagem_usuario.lower() == "sair":
                print("Bot encerrado.")
                break
            
            resposta_bot = chatbot_resposta(mensagem_usuario)
            contato = "Nome do Contato"  # Substitua com o nome do contato desejado
            enviar_mensagem(driver, contato, resposta_bot)
            time.sleep(2)  # Aguardar um tempo antes de enviar a próxima mensagem
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
