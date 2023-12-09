from flask import Flask, request, jsonify, abort
import pandas as pd
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Rota para receber dados de vinho via método POST
@app.route("/vinho", methods=["POST"])
def process_wine_data():
    try:
        # Função para carregar o modelo treinado a partir do caminho especificado
        def load_model(model_path):
            with open(model_path, "rb") as file:
                return pickle.load(file)

        # Função para fazer previsões usando o modelo carregado
        def make_predictions(model, input_data):
            return model.predict(input_data)

        # Caminho do modelo treinado (deve ser ajustado para o caminho real)
        model_path = "../modelo/best_model.pkl"  # Alterado para o caminho específico

        # Carrega o modelo treinado
        loaded_model = load_model(model_path)

        # Gera dados de entrada para previsão a partir dos dados recebidos via formulário POST
        input_data = pd.DataFrame(
            {
                "type": [request.form["type"]],
                "fixed acidity": [request.form["fixed_acidity"]],
                "volatile acidity": [request.form["volatile_acidity"]],
                "citric acid": [request.form["citric_acid"]],
                "residual sugar": [request.form["residual_sugar"]],
                "chlorides": [request.form["chlorides"]],
                "free sulfur dioxide": [request.form["free_sulfur_dioxide"]],
                "total sulfur dioxide": [request.form["total_sulfur_dioxide"]],
                "density": [request.form["density"]],
                "pH": [request.form["pH"]],
                "sulphates": [request.form["sulphates"]],
                "alcohol": [request.form["alcohol"]],
            }
        )

        # Realiza a previsão usando o modelo carregado
        predictions = make_predictions(loaded_model, input_data)

        # Cria um dicionário com os dados do vinho e a qualidade prevista
        dados_do_vinho = {
            "type": request.form["type"],
            "fixed_acidity": float(request.form["fixed_acidity"]),
            "volatile_acidity": float(request.form["volatile_acidity"]),
            "citric_acid": float(request.form["citric_acid"]),
            "residual_sugar": float(request.form["residual_sugar"]),
            "chlorides": float(request.form["chlorides"]),
            "free_sulfur_dioxide": float(request.form["free_sulfur_dioxide"]),
            "total_sulfur_dioxide": float(request.form["total_sulfur_dioxide"]),
            "density": float(request.form["density"]),
            "pH": float(request.form["pH"]),
            "sulphates": float(request.form["sulphates"]),
            "alcohol": float(request.form["alcohol"]),
            "quality": int(predictions[0]),  # Converte para um inteiro Python regular
        }

        # Imprime os dados do vinho no console
        print("dados", dados_do_vinho)

        # Imprime os dados do vinho em formato JSON no console
        print("json", jsonify(dados_do_vinho))

        # Retorna os dados do vinho em formato JSON como resposta
        return jsonify(dados_do_vinho)

    except Exception as e:
        # Em caso de erro, imprime o erro e retorna um código de erro 500
        print("Error:", e)
        abort(500)


if __name__ == "__main__":
    # Inicia o servidor Flask em modo de depuração
    app.run(debug=True)
