# Instalando nossa primeira API

1. Criar a pasta fastAPI.
2. Instalar fastAPI `python3 -m venv primeira_api`
3. Ativa a api com o comando: `.\primeira_api\Scripts\activate`. Pode desativar com o comando: `.deactivate`
    - No caso de ser windows no powershel rodar como admin o comando: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` e depois apertar `S`
    - No caso de ser linux digitar no terminal: 'source primeira_api\bin\activate'
4. Vamos instalar o fastAPI: `pip install fastapi`
5. Vamos instalar o servidor uvicorn: `pip install uvicorn[standard]`, no caso do linux é: `pip3 install 'uvicorn[standard]'`.
6. Criar o main com o exemplo do [Create it da fastAPI](https://fastapi.tiangolo.com/) e rodar no terminal dentro da pasta `primeira_api`: `uvicorn main:app --reload`
7. Se precisar ajuda somente acrescentar ao link: `\docs`
