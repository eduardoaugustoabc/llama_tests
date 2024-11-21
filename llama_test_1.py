from groq import Groq

client = Groq(
    # default, pode ser omitido
    api_key="your_api_key",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "you are a helpful assistant."
        },
        {
            "role": "user",
            "content": """create a selenium code that fits this test case with your comments in english and consider that the driver path is alrealdy in the environment variables:
            # Caso de Teste 1: Login com Credenciais Válidas
            # Objetivo: Confirmar que o login com credenciais corretas permite o acesso à área do usuário.

            # Passos:
            # 1. Abra o navegador e acesse a página de login: "https://www.opencartbrasil.com.br/conta/acessar".
            # 2. No campo de e-mail (localizado pelo ID "input-email"), insira um e-mail válido.
            # 3. No campo de senha (localizado pelo ID "input-password"), insira a senha correspondente.
            # 4. Clique no botão de login (CSS Selector: "input[type='submit']").
            # 5. Aguarde o carregamento e verifique se o link "Meus dados" está visível após o login.

            # Resultado Esperado:
            # O link "Meus dados" deve ser exibido na página, indicando que o login foi bem-sucedido.
            """,
        }
    ],
    model="llama-3.1-70b-versatile",
)

print(chat_completion.choices[0].message.content)
