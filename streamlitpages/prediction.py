import base64
import time
import constants
import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image
from googletrans import Translator
from streamlit_lottie import *

st.set_page_config(
    page_title='FloraMD',
    page_icon='🌱',
    layout='wide',
    initial_sidebar_state='collapsed'
)

model = tf.keras.models.load_model(constants.MODEl_PATH)

indian_languages = {
    'English': 'en',
    'Hindi': 'hi',
    'Bengali': 'bn',
    'Telugu': 'te',
    'Marathi': 'mr',
    'Tamil': 'ta',
    'Urdu': 'ur',
    'Gujarati': 'gu',
    'Kannada': 'kn',
    'Odia': 'or',
    'Malayalam': 'ml',
    'Punjabi': 'pa',
    'Assamese': 'as',
    'Maithili': 'mai',
    'Santali': 'sat',
    'Kashmiri': 'ks',
    'Nepali': 'ne',
    'Sindhi': 'sd',
    'Konkani': 'kok',
    'Manipuri': 'mni',
    'Dogri': 'doi',
    'Bodo': 'brx',
    'Sanskrit': 'sa'
}

translator = Translator()

def translate_text(text, dest_language):
    return translator.translate(text, dest=dest_language).text

def translate_dict(dictionary, dest_language):
    return {key: translate_text(value, dest_language) for key, value in dictionary.items()}

def translate_solutions(solutions, dest_language):
    if isinstance(solutions, str):
        return translate_text(solutions, dest_language)
    elif isinstance(solutions, dict):
        return translate_dict(solutions, dest_language)
    else:
        return solutions

def predict_class(image_path):
    original_image = Image.open(image_path)

    preprocessed_image = original_image.resize((256, 256))
    preprocessed_image = np.array(preprocessed_image) / 255.0

    preds = model.predict(np.expand_dims(preprocessed_image, axis=0))
    labels = ['Healthy', 'Powdery', 'Rust']

    preds_class = np.argmax(preds)
    preds_label = labels[preds_class]

    return preds_label, round(preds[0][preds_class], 2)

def display_solutions(predicted_class):
    solutions = {
        'Healthy': constants.HEALTHY_SOLUTIONS,
        'Powdery': constants.POWDERY_SOLUTIONS,
        'Rust': constants.RUST_SOLUTIONS
    }
    
    if predicted_class in solutions:
        st.subheader("Solutions:")
        translated_solutions = translate_solutions(solutions[predicted_class], dest_language)
        st.write(translated_solutions)

@st.cache_data()
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


css = """
<style>
.container {
  width: 100%;
  height: 100%;
  --color: rgba(114, 114, 114, 0.3);
  background-color: #191a1a;
  background-image: linear-gradient(0deg, transparent 24%, var(--color) 25%, var(--color) 26%, transparent 27%,transparent 74%, var(--color) 75%, var(--color) 76%, transparent 77%,transparent),
      linear-gradient(90deg, transparent 24%, var(--color) 25%, var(--color) 26%, transparent 27%,transparent 74%, var(--color) 75%, var(--color) 76%, transparent 77%,transparent);
  background-size: 55px 55px;
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

css_button_style = """
    <style>
        .predict-btn {
            border: none;
            width: 15em;
            height: 5em;
            border-radius: 3em;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 12px;
            background: #1C1A1C;
            cursor: pointer;
            transition: all 450ms ease-in-out;
        }

        .sparkle {
            fill: #AAAAAA;
            transition: all 800ms ease;
        }

        .text {
            font-weight: 600;
            color: #AAAAAA;
            font-size: medium;
        }

        .predict-btn:hover {
            background: linear-gradient(0deg,#A47CF3,#683FEA);
            box-shadow: inset 0px 1px 0px 0px rgba(255, 255, 255, 0.4),
            inset 0px -4px 0px 0px rgba(0, 0, 0, 0.2),
            0px 0px 0px 4px rgba(255, 255, 255, 0.2),
            0px 0px 180px 0px #9917FF;
            transform: translateY(-2px);
        }

        .predict-btn:hover .text {
            color: white;
        }

        .predict-btn:hover .sparkle {
            fill: white;
            transform: scale(1.2);
        }

    </style>
"""

button_html = f"""
<button onclick="predict()" class="predict-btn">
    <span class="text">Predict</span>
    <svg class="sparkle" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24">
        <path fill="none" d="M0 0h24v24H0z"/>
        <path d="M10 6.83v-.01l-.01-.01L3.41 13.4a1 1 0 0 0 .3 1.4 1 1 0 0 0 1.4-.3l5.6-5.6a1 1 0 0 1 1.4 1.42l-5.6 5.6a3 3 0 0 1-4.24-4.24l6.36-6.36a3.011 3.011 0 0 1 4.24 4.24l-5.25 5.25a1 1 0 1 1-1.42-1.41l5.25-5.25-1.58-1.58L10 6.83z"/>
    </svg>
</button>
"""

st.write(css_button_style, unsafe_allow_html=True)
st.write(button_html, unsafe_allow_html=True)

st.write("<h1>Plant Disease Detection using CNN</h1>", unsafe_allow_html=True)

with st.sidebar:
    st.image("assets/logo.png")

    app_mode = st.sidebar.selectbox(
        "Please navigate through the different sections of our website from here",
        ["Home", "Predict Plant D", "ChatBot", "Latest News", "Team Members"],
    )
    selected_language = st.sidebar.selectbox("Choose a language", list(indian_languages.keys()), index=0)

    dest_language = indian_languages[selected_language]

    
    
    uploaded_file = st.file_uploader("Upload an image", type=['png', 'jpg', 'jpeg'])
    
    st.info("""
            # About
            This is a web app to predict the disease in a plant using Convolutional Neural Network (CNN).
            
            # Contact
            For inquiries, you can mail us [here](mailto:mohrilsiddharth@gmail.com).
            """)
    st.image("/Users/Sid/Downloads/Project Exib 2/Plant_Disease_Detection-main/assets/vitlogo3.png")

home_page = st.empty()
home_page.write(constants.FRONT_PAGE, unsafe_allow_html=True)

display_image = st.empty()
classifying_text = st.empty()
button = st.empty()    


# Translate the page to the selected language


# Translate all the static content
translated_front_page = translate_text(constants.FRONT_PAGE, dest_language)
translated_about = translate_text("""
            # About
            This is a web app to predict the disease in a plant using Convolutional Neural Network (CNN).
            
            # Contact
            For inquiries, you can mail us [here](mailto:mohrilsiddharth@gmail.com).
            """, dest_language)

home_page.write(translated_front_page, unsafe_allow_html=True)

if uploaded_file is not None:
    home_page.empty()
    display_image.image(uploaded_file)
    
    predict_button = button.button("Predict", use_container_width=True)

    if predict_button and uploaded_file is not None: 
        classifying_text.empty()
        button.empty()
        label, confidence = predict_class(uploaded_file)
        
        loading_bar = st.empty()
        loading_bar.write("Classifying...")
        progress_text = "Please wait, we're predicting the image..."
        my_bar = loading_bar.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)

        my_bar.empty()
        st.toast("Prediction Complete!")
        st.info(f"##### Prediction: {label}\n##### Confidence: {confidence}")
        
    
        # Translate solutions based on the predicted disease
        if label == 'Powdery':
            translated_solutions = translate_solutions(constants.POWDERY_SOLUTIONS, dest_language)
        elif label == 'Healthy':
            translated_solutions = translate_solutions(constants.HEALTHY_SOLUTIONS, dest_language)
        else:
            translated_solutions = translate_solutions(constants.RUST_SOLUTIONS, dest_language)
        
        st.write(translated_solutions)

    classifying_text.empty()
