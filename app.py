from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Chargement du modèle et du scaler
with open('best_xgboost.pkl', 'rb') as f:
    model = pickle.load(f)

with open('power.pickle', 'rb') as f:
    power = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Récupération des valeurs du formulaire
        data = request.form

        # Conversion en float
        float_features = [float(data[key]) for key in data.keys()]
        print("Initial features -->", float_features)

        # Transformation des données
        final_features = power.transform(np.array(float_features).reshape(1, -1))
        print("Transformed features -->", final_features)

        # Prédiction
        prediction = model.predict(final_features)[0]
        print("Prediction -->", prediction)

        return render_template(
            'index.html',
            prediction_text=f"The predicted apartment price is: {round(prediction, 2)} roubles"
        )

    except Exception as e:
        print("ERROR:", e)
        return render_template(
            'index.html',
            prediction_text="An error occurred during prediction. Check console."
        )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)
