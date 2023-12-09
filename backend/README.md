# BackEnd MVP

Este é o projeto referente a parte do backEnd do MVP da sprint **Qualidade de Software, Segurança e Sistemas Inteligentes**

O projeto abrange um sistema de previsão da qualidade de vinhos. Por meio do navegador, é possível realizar operações de consulta, inserindo atributos essenciais para a execução da análise preditiva.



---

## Como executar

Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

O ambiente virtual pode ser instalado e utilizado através dos comandos abaixo, os comandos apresentados são compatíveis com o sistema operacional Windows.

```
python -m venv venv
```

para ativar o ambiente virtual:

```
.\venv\scripts\activate
```

Posteriormente, será necessário instalar todas as dependências listadas em `requirements.txt`, através do seguinte comando:

```
(env)$ pip install -r requirements.txt
```

Para executar as testes automatizados basta acessar o diretório "tests" e executar:

```
(env)$ pytest
```

Para executar a API basta acessar o diretório "app" e executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

