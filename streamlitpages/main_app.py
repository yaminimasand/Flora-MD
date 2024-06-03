import base64
import time
import constants
import numpy as np
import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from textblob import TextBlob
import toml
import html
import requests 
from streamlit.runtime.media_file_storage import MediaFileStorageError
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import streamlit as st
from hugchat import hugchat
from hugchat.login import Login
import tensorflow as tf
from PIL import Image
from googletrans import Translator
from streamlit_lottie import *
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

flag = 0

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


rerun = False

def load_bg_and_css():
    
    st.write("""<style>
        iframe[data-testid="stIFrame"] {{
            position: fixed;
            top: 2rem;
            bottom: 0;
            margin: auto;
        }}
        </style>{padding}""".format(
        padding="<br>"*st.session_state["navbar_padding"]), 
        unsafe_allow_html=True
    )   
    
    lottie = """
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
        <lottie-player src="https://lottie.host/5ca098aa-290c-4091-9548-f8f46c51b8ce/gzqvydc0py.json" background="transparent" speed="2" style="width: 2000px; height: 2000px;" loop autoplay></lottie-player>
    """
    st.components.v1.html(lottie, width=2010, height=2010)

    lottie3 = """
    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    <lottie-player src="https://lottie.host/b60fff1d-cbeb-4d41-aba1-b624200c0513/OoZwK6n4cr.json"  background="transparent"  speed="2.75"  style="width: 2000px; height: 2000px;"  loop  autoplay></lottie-player>
    """

    st.components.v1.html(lottie3, width=2010, height=2010)

def chat_bot():
    HF_EMAIL = os.getenv("HF_EMAIL")
    HF_PASS = os.getenv("HF_PASS")
    BASE_PROMPT = "I want you to act as a virtual assistant for farmers and come up with conventional treatments for plant diseases. You should be able to recommend conventional  methods to resolve the plant disease and other natural alternatives.\n\n"

    if "messages" not in st.session_state.keys():
        st.session_state.messages = [{"role": "assistant", "content": "Hi! How may I help you?"}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    def generate_response(prompt_input, email, passwd):

        sign = Login(email, passwd)
        cookies = sign.login()
        chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

        global flag
        if flag < 1:
            flag += 1
            prompt_input = BASE_PROMPT + prompt_input
        return str(chatbot.chat(prompt_input)).strip('`')

    if prompt := st.chat_input(disabled=not (HF_EMAIL and HF_PASS)):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_response(prompt, HF_EMAIL, HF_PASS) 
                st.write(response) 
        message = {"role": "assistant", "content": response}
        st.session_state.messages.append(message)

def home_page():

    st.write("")
    st.write("")
    st.write("")

    st.write('<div style="text-align: center;">This tool is designed to assist you in identifying the health status of your plants with the help of a Convolutional Neural Network (CNN). Whether you are a home gardener or a farmer, early detection of plant diseases can make a significant difference in preserving the well-being of your plants and optimizing crop yields.</div>', unsafe_allow_html=True)

    def get_image_download_link(img_path):
        with open(img_path, "rb") as img_file:
            img_bytes = img_file.read()
        img_base64 = base64.b64encode(img_bytes).decode()
        return f"data:image/png;base64,{img_base64}"

    image_path = "assets/floralogo.png"

    st.write(
        """
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -210%);">
            <img src="{}" alt="Local Image" width=500>
        </div>
        """.format(get_image_download_link(image_path)),
        unsafe_allow_html=True
    )

credentials = toml.load(".streamlit/secrets.toml")


gsheets_connection = credentials.get("connections", {}).get("gsheets", {})


conn = GSheetsConnection(
    connection_name="gsheets", 
    spreadsheet=gsheets_connection.get("spreadsheet"),
    worksheet=gsheets_connection.get("worksheet"),
    type=gsheets_connection.get("type"),
    project_id=gsheets_connection.get("project_id"),
    private_key_id=gsheets_connection.get("private_key_id"),
    private_key=gsheets_connection.get("private_key"),
    client_email=gsheets_connection.get("client_email"),
    client_id=gsheets_connection.get("client_id"),
    auth_uri=gsheets_connection.get("auth_uri"),
    token_uri=gsheets_connection.get("token_uri"),
    auth_provider_x509_cert_url=gsheets_connection.get("auth_provider_x509_cert_url"),
    client_x509_cert_url=gsheets_connection.get("client_x509_cert_url")
)

def forum_page():
    st.write("<h1>Feedback forum</h1>", unsafe_allow_html=True)

    card_width = 800

    st.markdown(
        f"""
        <style>
            .banner-card {{
                width: {card_width}px;
                display: flex;
                flex-direction: column;
                align-items: center;
                background-color: #f0f0f0;
                border-radius: 12px;
                padding: 20px;
                box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
            }}
            .banner-card img {{
                width: 100%;
                border-radius: 12px;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
    if uploaded_image is not None:
        st.markdown(
            f'<div class="banner-card"><img src="data:image/jpeg;base64,{uploaded_image.read().encode("base64").decode()}"></div>',
            unsafe_allow_html=True
        )

    data = conn.read(worksheet="Forum", headers="first_row")

    df = pd.DataFrame(data)

    with st.expander("Community Reviews"):
        for index, row in df.iterrows():
            sentiment = str(row.iloc[0])  
            feedback = row.iloc[1]  
            if sentiment.lower() == "positive":
                st.success(f"👍 Positive Feedback: {feedback}")
            elif sentiment.lower() == "negative":
                st.error(f"👎 Negative Feedback: {feedback}")

    feedback_input = st.text_area("Enter Feedback")
    blob = TextBlob(feedback_input)
    sentiment = blob.sentiment.polarity
    sentiment_label = "Positive" if sentiment > 0 else "Negative" if sentiment < 0 else "Neutral"
    if st.button("Submit"):
        new_entry = {"Sentiment": sentiment_label, "Feedback": feedback_input}
        df = df.dropna(subset=["Sentiment", "Feedback"]) 
        last_index = len(df)  
        df = df.append(new_entry, ignore_index=True)

        print("Updated DataFrame:")
        print(df)

        conn.update(worksheet="Forum", data=df.values.tolist())
        print("Data updated successfully!")

        st.success("Feedback submitted successfully!")


def news_page():
    API_KEY = os.getenv("NEWS")
    news_data = requests.get(f'https://newsapi.org/v2/everything?q=plant%20disease&apiKey={API_KEY}&language=en&searchIn=title').json()['articles']

    for random_news in news_data:
        st.write(f"""<h2>{html.unescape(random_news['title'])}</h2><br>""", unsafe_allow_html=True)
        try:
            if random_news["urlToImage"]:
                st.image(f'{random_news["urlToImage"]}')
        except MediaFileStorageError:
            st.image("https://unsplash.com/photos/red-and-green-leaf-in-close-up-photography-E3g2UP9WoLU")
            
        st.write(f"""
            <h5>{random_news['description']}</h5>
            Link : <a href="{random_news['url']}">{random_news['url'][:80]}...</a><br>
            Author : {random_news['author']}, &nbsp; <i>{random_news['publishedAt'][:10]}</i>
            <hr>
        """, unsafe_allow_html=True)

def display_team_members():
    EMOJI = "assets/team.png"
    TEAM_MEMBERS = ["Siddharth Mohril 22BAI10132", "Ravneet Kaur 22BAI10246", "Vansh Dudeja 22BAI10257", "Mitali Rawat 22BAI10429", "Yamini Masand 22BAI10426"]
    st.markdown(f"<h1 style='text-align:center;'>Meet our dedicated team members</h1>", unsafe_allow_html=True)
    st.markdown("<br><br><div class='team-container'>", unsafe_allow_html=True)

    t_left, t_mid, t_right = st.columns(3)

    with t_left:
        st.markdown(
            f"""
            <a href="https://github.com/siddharth-mohril" target="_blank">
                <div class='team-member'>
                    <h3>{TEAM_MEMBERS[0]}</h3>
                    <p>DATA TRAINING AND TESTING</p>
                </div>
            </a>
            <br>
            """,
            unsafe_allow_html=True
        )

    with t_mid:
        st.image(EMOJI)


        st.empty()

    with t_right:
        st.markdown(
            f"""
            <a href="https://github.com/Ravneetk342" target="_blank">
                <div class='team-member'>
                    <h3>{TEAM_MEMBERS[1]}</h3>
                    <p>MODEL TESTING</p>
                </div>
            </a>
            <br>
            """,
            unsafe_allow_html=True
        )


    b_left, b_mid, b_right = st.columns(3)

    with b_left:
        st.markdown(
            f"""
            <a href="https://github.com/Vanshdudeja27" target="_blank">
                <div class='team-member'>
                    <h3>{TEAM_MEMBERS[2]}</h3>
                    <p>DATA TRAINING AND TESTING</p>
                </div>
            </a>
            <br>
            """,
            unsafe_allow_html=True
        )

    with b_mid:
        st.markdown(
            f"""
            <a href="https://github.com/mitalirawat20" target="_blank">
                <div class='team-member'>
                    <h3>{TEAM_MEMBERS[3]}</h3>
                    <p>FEATURE EXTRACTION</p>
                </div>
            </a>
            <br>
            """,
            unsafe_allow_html=True
        )

    with b_right:
        st.markdown(
            f"""
            <a href="https://github.com/yaminimasand" target="_blank">
                <div class='team-member'>
                    <h3>{TEAM_MEMBERS[4]}</h3>
                    <p>DATA PREPROCESSING</p>
                </div>
            </a>
            <br>
            """,
            unsafe_allow_html=True
        )


def predict_disease():
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

        selected_language = st.sidebar.selectbox("Choose a language", list(indian_languages.keys()), index=0)

        dest_language = indian_languages[selected_language]

        
        
        uploaded_file = st.file_uploader("Upload an image", type=['png', 'jpg', 'jpeg'])
        
        st.info("""
                # About
                This is a web app to predict the disease in a plant using Convolutional Neural Network (CNN).
                
                # Contact
                For inquiries, you can mail us [here](mailto:mohrilsiddharth@gmail.com).
                """)
        st.image("assets/logovit.png")

    home_page = st.empty()
    home_page.write(constants.FRONT_PAGE, unsafe_allow_html=True)

    display_image = st.empty()
    classifying_text = st.empty()
    button = st.empty()    

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
            
            if label == 'Powdery':
                translated_solutions = translate_solutions(constants.POWDERY_SOLUTIONS, dest_language)
            elif label == 'Healthy':
                translated_solutions = translate_solutions(constants.HEALTHY_SOLUTIONS, dest_language)
            else:
                translated_solutions = translate_solutions(constants.RUST_SOLUTIONS, dest_language)
            
            st.write(translated_solutions)

        classifying_text.empty()




def main():
    configure()
    st.set_page_config(
        page_title='FloraMD',
        page_icon='🌱',
        layout='wide',
        initial_sidebar_state='collapsed'
    )
    
    with st.sidebar:
        
        if "navbar_padding" not in st.session_state.keys():
            st.session_state["navbar_padding"] = 10
        
    load_bg_and_css()

    app_mode = option_menu(
        options=["Home", "Predict", "ChatBot", "News", "Forum", "Team"],
        orientation="horizontal",
        menu_title="",
        styles={
            "nav-link-selected": {"background-color": "#A47CF3", "z-index": "100"},
        }
    )
    
    if app_mode == "Home":
        st.session_state["navbar_padding"] = 10
        home_page()
        
    elif app_mode == "Predict":
        st.session_state["navbar_padding"] = 0
        predict_disease()
        
    elif app_mode == "ChatBot":
        st.session_state["navbar_padding"] = 0
        chat_bot()
        
    elif app_mode == "News":
        st.session_state["navbar_padding"] = 0
        news_page()
        
    elif app_mode == "Forum":
        st.session_state["navbar_padding"] = 5
        forum_page()
        
    elif app_mode == "Team":
        st.session_state["navbar_padding"] = 0
        display_team_members()

    if st.session_state.get("rerun", False):
        st.session_state["rerun"] = False
        st.experimental_rerun()
    else:
        st.session_state["rerun"] = True


if __name__ == "__main__":
    main()
