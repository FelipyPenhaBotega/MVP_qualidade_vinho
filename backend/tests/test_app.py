import pytest
from app.app import app
from flask import Flask, abort

# Define uma fixture para criar um cliente de teste para o aplicativo Flask
@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()

# Escreve testes usando o client
def test_process_wine_data(client):
    # Envia uma solicitação POST simulando dados do formulário
    response = client.post("/vinho", data={
        "type": "white",
        "fixed_acidity": "7.1",
        "volatile_acidity": "0.25",
        "citric_acid": "0.35",
        "residual_sugar": "6.7",
        "chlorides": "0.038",
        "free_sulfur_dioxide": "42",
        "total_sulfur_dioxide": "162",
        "density": "0.994",
        "pH": "3.21",
        "sulphates": "0.54",
        "alcohol": "10.3",
    })
    
    # Verifica se a resposta tem um código de status 200 (OK)
    assert response.status_code == 200
