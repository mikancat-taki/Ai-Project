from flask import Flask, request, jsonify
from models.model import AIModel
from pipelines.inference import generate_prediction
from config.settings import MODEL_PATH

app = Flask(__name__)

# Initialize the AI model
model = AIModel(MODEL_PATH)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    if not data or 'input' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    input_data = data['input']
    prediction = generate_prediction(model, input_data)
    
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)