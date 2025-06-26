import gradio as gr
import pickle
import numpy as np

# Load scaler and model
scaler = pickle.load(open('model/Linear/scaled_data.pkl', 'rb'))
model = pickle.load(open('model/Linear/model.pkl', 'rb'))

MIN_USD_INR = 82.0
MAX_USD_INR = 86.0

def calculate_goldrate(usd_inr):
    if usd_inr < MIN_USD_INR:
        return f"⚠️ Model was trained only on USD/INR values from {MIN_USD_INR} This input may give inaccurate results."

    # Predict safely
    scaled_input = scaler.transform(np.array(usd_inr).reshape(1, -1))
    prediction = model.predict(scaled_input)[0][0]
    prediction = np.maximum(prediction, 0)      # to avoid the neagtive answer
    return round(prediction, 2)

# Launch Gradio interface
demo = gr.Interface(
    fn=calculate_goldrate,
    inputs=gr.Number(label="Enter USD to INR value"),
    outputs=gr.Textbox(label="Predicted Gold Price (₹)"),
    title="How much is 1g of gold in India NOW?",
    description="⚠️ For best accuracy, use USD/INR values from 82."
)

demo.launch(share=True)
