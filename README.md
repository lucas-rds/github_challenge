# Desafio Github
API que funciona como proxy da api do github e possibilita salvar os repositórios desejados.

## Stack
O projeto utiliza `Python 3.9.1` , `alembic`, `FastAPI` com `Uvicorn` e `pytest` para os testes
## Usando
Para subir a aplicação, utilize o domando `docker-compose up --build`

Caso não possua docker, será necessário o uso do python 3.9.1 e a instalação das dependências com o comando: `pip install -r requirements.txt`, neste caso é indicada a criação de um ambiente isolado, usando `virtualenv` ou `pyenv`.
Será preciso também instância do postgres com as seguintes configurações:
```
POSTGRES_DB: github_challenge
POSTGRES_USER: postgres
POSTGRES_PASSWORD: postgres
POSTGRES_PORT: 5432
``` 
Você pode alterar os valores acima como desejado, porém ao faze-lo, deve alterar os valores também nas variáveis de ambiente ou nos valores default na config do sistema.

Após feito o setup do python e do banco, basta utilizar o comando `make migrate && make run` caso esteja no linux, ou `Winfile.bat migrate` e `Winfile.bat run` caso esteja em ambiente windows.

Com a aplicação rodando, um exemplo de uso com o usuário do github lucas-rds seria:

### Acessando
Acesse http://127.0.0.1:8000/repositories/?username=lucas-rds&from_local=false para visualizar os repositorios do usuário de username lucas-rds, note o parâmetro from_local=false, ele indica que os repositórios listados foram consultados da api do github.

Vamos usar o repositório chat-bot-agenda do lucas-rds para o próximo exemplo:

Acesse http://127.0.0.1:8000/repositories/chat-bot-agenda/?username=lucas-rds&save_data=true, note o parâmetro save_data=true, que serve para salvar o repositório no banco de dados local.

Agora com o repositório salvo, podemos utilizar o endpoint anterior com o parametro from_local=true para retornar apenas os repositórios da base de dados e não do github:

http://127.0.0.1:8000/repositories/?username=lucas-rds&from_local=true

### Endpoints:
Os endpoints disponíveis:
Endpoint   | query params |
--------- | ------ |
/repositories | ?username={string:required}&from_local={boolean} | 
/repositories/{repository_name} | ?username={string:required}&save_data={boolean:required} |

## Contribuindo
### Setup
Utilizando o python 3.9.1, basta instalar as dependências com: `pip install -r requirements.txt`, é recomendado o uso de um ambiente isolado com `virtualenv` ou `pyenv`. Para rodar a aplicação siga as instruções no tópico [Usando](#usando) acima

### Debug VSCode
Caso esteja usando o Visual Studio Code, basta rodar o modo debug, o projeto já possui uma pasta .vscode com launch.json, que pode ser alterado como desejado para se adequar a seu ambiente.


### Testes
Para executar os testes use: 
`make test` ou `Winfile.bat test` ou `pytest -v --cov-report term-missing --cov-report html:coverage --cov app/`
