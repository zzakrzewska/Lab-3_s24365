from flask import Flask, request, jsonify
import joblib
import pandas as pd

from read_clean_data import prepare_api_input

model = joblib.load("model.pkl")

api = Flask(__name__)

@api.route('/collegeDistance', methods=['POST'])
def college_distance():
    try:
        data = request.get_json()
        dataframe = pd.DataFrame([data])
        dataframe = prepare_api_input(dataframe)
        prediction = model.predict(dataframe)

        return jsonify({'prediction': prediction[0]})

    except Exception as e:
        return jsonify({'exception': str(e)}, 400)

if __name__ == "__main__":
    api.run(host="0.0.0.0", port=5000)