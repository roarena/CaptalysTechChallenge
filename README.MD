# Teste técnico
## Captalys — BackEnd Developer
O objeto deste desafio e criar uma API REST que se comunica com a API REST oficial do Github: https://api.github.com/

## Instalação

Instalar Postgres com os seguintes detalhes:
```sh
user: postgres <Esse é o usuário default>
pw: testcapt
```
Instalar os pacotes do requirements.txt

```sh
pip install -r requirements.txt
```

## Execução

```sh
python3 main.py
```
A aplicação irá subir no IP 127.0.0.1:8000, como definido no [main.py](https://github.com/roarena/CaptalysTechChallenge/blob/main/main.py)

### Retornar dados do usuário
Parâmetro opcional from_local=true ou false
```sh
http://127.0.0.1:8000/repositories/?username=<user_name>
http://127.0.0.1:8000/repositories/?username=<user_name>&from_local=true
```

### Retornar dados do repositório
Parâmetro obrigatório save_data=true ou false, salva os dados do usuário e do repositório.

```sh
http://127.0.0.1:8000/repositories/<repo_name>?username=<user_name>&save_data=true
```