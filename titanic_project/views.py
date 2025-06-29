import os
import json
import numpy as np
import joblib
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from keras.models import load_model

# --- CONFIGURAÇÃO E CARREGAMENTO INICIAL ---

# Base dir
# Usar dirname(dirname(...)) para subir dois níveis se 'views.py' está em 'titanic_project/titanic_project/'
# Com base na sua imagem (views.py dentro de 'titanic_project'), o seu BASE_DIR original está correto.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Categoria Mappings (Mantido como estava, parece correto)
category_mappings = {
    "sex": {"female": 0, "male": 1},
    "embarked": {"C": 0, "Q": 1, "S": 2},
    "class": {"First": 0, "Second": 1, "Third": 2},
    "who": {"child": 0, "man": 1, "woman": 2},
    "deck": {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "Unknown": 7},
    "embark_town": {"Cherbourg": 0, "Queenstown": 1, "Southampton": 2},
    "pclass": {1: 0, 2: 1, 3: 2},
    "sibsp": {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 8: 6},
}

# Ordem das features (Mantido como estava)
FEATURE_ORDER = [
    "pclass",
    "sex",
    "age",
    "sibsp",
    "parch",
    "fare",
    "embarked",
    "class",
    "who",
    "adult_male",
    "deck",
    "embark_town",
    "alone",
]

# Variáveis globais para o modelo e scaler
MODEL = None
SCALER = None


def load_prediction_components():
    """Carrega o modelo Keras e o scaler Joblib para as variáveis globais."""
    global MODEL, SCALER
    # Esta função só precisa rodar uma vez. O 'if' garante isso.
    if MODEL is None or SCALER is None:
        try:
            # O caminho '../models/' sobe um nível a partir de 'titanic_project' para encontrar a pasta 'models'
            # Com base na sua imagem, isso parece estar correto.
            model_path = os.path.join(
                BASE_DIR, "..", "models", "model.h5"
            )  # Mudei para .h5, que é mais comum. Se o seu é .keras, mantenha.
            scaler_path = os.path.join(BASE_DIR, "..", "models", "keras_scaler.pkl")

            MODEL = load_model(model_path)
            SCALER = joblib.load(scaler_path)
            print(">>> Modelo e scaler carregados com sucesso na memória. <<<")
        except Exception as e:
            print(f"!!!!!! Erro ao carregar o modelo ou scaler: {e} !!!!!!")
            # Deixamos como None para que as requisições futuras retornem um erro claro.
            MODEL = None
            SCALER = None


# Carrega os componentes UMA VEZ quando o servidor Django inicia.
# Esta é a melhor prática para performance.
load_prediction_components()

# --- VIEW DA API ---


@csrf_exempt
def predict(request):
    """View para receber dados via POST e retornar uma predição."""
    if request.method != "POST":
        return JsonResponse({"error": "Only POST method is allowed."}, status=405)

    # CORREÇÃO 1: Checar se os modelos foram carregados na inicialização.
    # Não precisamos chamar a função de load de novo aqui.
    if MODEL is None or SCALER is None:
        return JsonResponse(
            {"error": "Model or Scaler not loaded. Please check server logs."},
            status=500,
        )

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format."}, status=400)

    # --- Pré-processamento dos dados de entrada ---
    try:
        input_features = []
        for feature in FEATURE_ORDER:
            value = data.get(feature)

            if value is None:
                return JsonResponse(
                    {"error": f"Missing required feature: '{feature}' in input data."},
                    status=400,
                )

            if feature in category_mappings:
                mapped_value = category_mappings[feature].get(
                    str(value)
                )  # Converte valor para string para garantir a busca
                if mapped_value is None:
                    return JsonResponse(
                        {
                            "error": f"Invalid value '{value}' for category '{feature}'. Value not in mapping."
                        },
                        status=400,
                    )
                input_features.append(mapped_value)
            else:  # Features numéricas
                # Garante que o valor seja convertido para float
                input_features.append(float(value))

    except (ValueError, TypeError) as e:
        return JsonResponse({"error": f"Data preprocessing error: {e}"}, status=400)

    # --- Predição ---
    try:
        input_data = np.array([input_features])

        # CORREÇÃO 2: Usar as variáveis globais corretas (maiúsculas)
        input_scaled = SCALER.transform(input_data)
        prediction = MODEL.predict(input_scaled)

        survived = bool(prediction[0][0] > 0.5)
        confidence = float(prediction[0][0])

        return JsonResponse(
            {
                "survived": survived,
                "confidence": confidence,
                "message": "Prediction successful",
            }
        )

    except Exception as e:
        return JsonResponse(
            {"error": f"Prediction failed due to internal processing error: {e}"},
            status=500,
        )
