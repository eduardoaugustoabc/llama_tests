from groq import Groq

client = Groq(
    # default, pode ser omitido
    api_key="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",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "you are a helpful assistant."
        },
        {
            "role": "user",
            "content": """check this selenium code and give a review about its quality and possible results in english:
            from selenium import webdriver
            from selenium.webdriver.common.by import By
            from selenium.webdriver.common.keys import Keys
            import time

            # Configurar WebDriver
            driver = webdriver.Chrome()
            driver.get("https://www.opencartbrasil.com.br/conta/acessar")

            # Preencher e enviar o formulário de login
            driver.find_element(By.ID, "input-email").send_keys("duduaugustoabc@gmail.com")
            driver.find_element(By.ID, "input-password").send_keys("Dudu2510")
            driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

            # Verificar se o login foi bem-sucedido
            time.sleep(2)  # Aguardar pelo carregamento

            # Espera até que o elemento "Meus dados" esteja presente na página
            meus_dados = driver.find_element(By.LINK_TEXT, "Meus dados")
            assert meus_dados.is_displayed(), "O link 'Meus dados' não está visível após o login."
            print("O link 'Meus dados' está visível. Login bem-sucedido!")

            # Finalizar WebDriver
            driver.quit()
            """,
        }
    ],
    model="llama-3.1-70b-versatile",
)

print(chat_completion.choices[0].message.content)