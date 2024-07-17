# app.py

from flask import Flask, request, render_template, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the model and label encoder
model = joblib.load('fish_species_model.pkl')
label_encoder = joblib.load('label_encoder.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve form data
    Length1 = request.form.get('Length1')
    Length2 = request.form.get('Length2')
    Length3 = request.form.get('Length3')
    Height = request.form.get('Height')
    Width = request.form.get('Width')
    Weight = request.form.get('Weight')
    
    # Ensure all fields are filled
    if not all([Length1, Length2, Length3, Height, Width, Weight]):
        return jsonify({'error': 'Please provide all input values.'})

    # Convert form data to float and create a list
    data = [float(Length1), float(Length2), float(Length3), float(Height), float(Width), float(Weight)]
    
    # Reshape data for prediction
    data = np.array(data).reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(data)
    
    # Get species name
    species_name = label_encoder.inverse_transform(prediction)[0]
    
    # Render the result.html template with prediction data
    return render_template('result.html', species=species_name)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
