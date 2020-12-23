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

## Contribuindo
### Setup
Utilizando o python 3.9.1, basta instalar as dependências com: `pip install -r requirements.txt`, é recomendado o uso de um ambiente isolado com `virtualenv` ou `pyenv`. Para rodar a aplicação siga as instruções no tópico [Usando](#usando) acima

### Debug VSCode
Caso esteja usando o Visual Studio Code, basta rodar o modo debug, o projeto já possui uma pasta .vscode com launch.json, que pode ser alterado como desejado para se adequar a seu ambiente.


### Testes
Para executar os testes use: 
`make test` ou `Winfile.bat test` ou `pytest -v --cov-report term-missing --cov-report html:coverage --cov app/`
