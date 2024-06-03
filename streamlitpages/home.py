# import streamlit as st
# import base64


# def home_page():
#     st.image("/Users/Sid/Downloads/Project Exib 2/Plant_Disease_Detection-main/assets/poten2.png")
#     st.write("""
#         ## Introduction to Alzheimer's Disease
#         Alzheimer's disease (AD) is a progressive neurodegenerative disease. Though best known for its role in declining memory function, symptoms also include: difficulty thinking and reasoning, making judgements and decisions, and planning and performing familiar tasks. It may also cause alterations in personality and behavior. The cause of AD is not well understood. There is thought to be a significant hereditary component. For example, a variation of the APOE gene, APOE e4, increases risk of Alzheimer's disease.

#         ## Why Early Detection Matters
#         Early detection of Alzheimer's disease is paramount because it offers the best chance for effective treatment and improved quality of life. Identifying the condition at its onset allows for timely interventions, which can slow its progression and enable individuals and their families to plan for the future. Early detection also facilitates access to support services and clinical trials, fostering hope for more effective therapies in the fight against this devastating disease.

#         ## Purpose of the project
#         The purpose of this project proposal is to develop a machine learning model for the early prediction of Alzheimer's disease. Alzheimer's disease is a devastating neurodegenerative disorder that affects millions of individuals worldwide. Early detection is crucial for better patient care and the development of potential interventions. This project aims to leverage machine learning techniques to create a predictive model that can identify individuals at risk of Alzheimer's disease based on relevant data.
        
#         <br>
                
#         """, unsafe_allow_html=True)

#     st.caption('Finished reading? Navigate to the `Prediction Page` to make some predictions')
# @st.cache_data()
# # def get_base64_of_bin_file(bin_file):
# #     with open(bin_file, 'rb') as f:
# #         data = f.read()
# #     return base64.b64encode(data).decode()


# st.set_page_config(
#     page_title="Plant Disease Detection",
#     page_icon="🌱",
#     layout="wide",  # Set layout to wide
#     initial_sidebar_state="expanded"  # Expand the sidebar by default
# )

# css = """
# <style>
# .container {
#   width: 100%;
#   height: 100%;
#   --color: rgba(114, 114, 114, 0.3);
#   background-color: #191a1a;
#   background-image: linear-gradient(0deg, transparent 24%, var(--color) 25%, var(--color) 26%, transparent 27%,transparent 74%, var(--color) 75%, var(--color) 76%, transparent 77%,transparent),
#       linear-gradient(90deg, transparent 24%, var(--color) 25%, var(--color) 26%, transparent 27%,transparent 74%, var(--color) 75%, var(--color) 76%, transparent 77%,transparent);
#   background-size: 55px 55px;
# }
# </style>
# """

# st.markdown(css, unsafe_allow_html=True)


# def set_page_background(png_file):
#     @st.cache_data
#     def get_base64_of_bin_file(bin_file):
#         with open(bin_file, 'rb') as f:
#             data = f.read()
#         return base64.b64encode(data).decode()

#     bin_str = get_base64_of_bin_file(png_file)
#     page_bg_img = '''
#         <style>
#         .stApp {{
#             background-image: url("data:image/png;base64,{bin_str}");
#             }}
#         </style>
#     '''.format(bin_str=bin_str)
#     st.markdown(page_bg_img, unsafe_allow_html=True)

# set_page_background("/Users/Sid/Downloads/Project Exib 2/Plant_Disease_Detection-main/assets/poten2.png")


# def set_png_as_page_bg(png_file):
#     bin_str = get_base64_of_bin_file(png_file)
#     page_bg_img = '''
#     <style>
#     body {
#     background-image: url("data:image/png;base64,%s") !important;
#     background-size: cover !important;
#     }
#     </style>
#     ''' % bin_str
    
#     st.markdown(page_bg_img, unsafe_allow_html=True)
#     return

# set_png_as_page_bg('assets/bg.png')


# # Define CSS button style
# css_button_style = """
#     <style>
#         .predict-btn {
#             border: none;
#             width: 15em;
#             height: 5em;
#             border-radius: 3em;
#             display: flex;
#             justify-content: center;
#             align-items: center;
#             gap: 12px;
#             background: #1C1A1C;
#             cursor: pointer;
#             transition: all 450ms ease-in-out;
#         }

#         .sparkle {
#             fill: #AAAAAA;
#             transition: all 800ms ease;
#         }

#         .text {
#             font-weight: 600;
#             color: #AAAAAA;
#             font-size: medium;
#         }

#         .predict-btn:hover {
#             background: linear-gradient(0deg,#A47CF3,#683FEA);
#             box-shadow: inset 0px 1px 0px 0px rgba(255, 255, 255, 0.4),
#             inset 0px -4px 0px 0px rgba(0, 0, 0, 0.2),
#             0px 0px 0px 4px rgba(255, 255, 255, 0.2),
#             0px 0px 180px 0px #9917FF;
#             transform: translateY(-2px);
#         }

#         .predict-btn:hover .text {
#             color: white;
#         }

#         .predict-btn:hover .sparkle {
#             fill: white;
#             transform: scale(1.2);
#         }
#     </style>
# """

# # Write CSS button HTML
# button_html = f"""
# <button onclick="predict()" class="predict-btn">
#     <span class="text">Predict</span>
#     <svg class="sparkle" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24">
#         <path fill="none" d="M0 0h24v24H0z"/>
#         <path d="M10 6.83v-.01l-.01-.01L3.41 13.4a1 1 0 0 0 .3 1.4 1 1 0 0 0 1.4-.3l5.6-5.6a1 1 0 0 1 1.4 1.42l-5.6 5.6a3 3 0 0 1-4.24-4.24l6.36-6.36a3.011 3.011 0 0 1 4.24 4.24l-5.25 5.25a1 1 0 1 1-1.42-1.41l5.25-5.25-1.58-1.58L10 6.83z"/>
#     </svg>
# </button>
# """

# # Write CSS button HTML
# st.write(css_button_style, unsafe_allow_html=True)
# st.write(button_html, unsafe_allow_html=True)


# st.write("<h1>Plant Disease Detection using CNN</h1>", unsafe_allow_html=True)

# with st.sidebar:
#     st.image("assets/logo.png")
    
#     uploaded_file = st.file_uploader("Upload an image", type = ['png', 'jpg', 'jpeg'])
    
#     st.info("""
#             # About
#             This is a web app to predict the disease in a plant using Convolutional Neural Network (CNN).
            
#             # Contact
#             For inquiries, you can mail us [here](mailto:mohrilsiddharth@gmail.com).
#             """)

# home_page = st.empty()
# home_page.write(constants.FRONT_PAGE, unsafe_allow_html=True)

# display_image = st.empty()
# classifying_text = st.empty()
# button = st.empty()    

# # use_sample_image = st.checkbox("Use example image", value = False)

# # if use_sample_image:
# #     display_image.image(f'sample/{random.randint(1,10)}.jpg')
# #     uploaded_file = True


# app_mode = st.sidebar.selectbox(
#     "Please navigate through the different sections of our website from here",
#     ["Home", "Predict Plant D", "ChatBot", "Latest News", "Team Members"],
# )

# home_page()

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from textblob import TextBlob
import toml
import html
import requests

# Load credentials from secrets.toml
credentials = toml.load("/Users/Sid/Downloads/Project Exib 2/Plant_Disease_Detection-main/.streamlit/secrets.toml")

# Get the GSheets connection details
gsheets_connection = credentials.get("connections", {}).get("gsheets", {})

# Establish connection with Google Sheets using credentials
conn = GSheetsConnection(
    connection_name="gsheets",  # Add the missing connection_name argument
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

# Define a function to fetch news articles
def _get_news(): 
    return requests.get(f'https://newsapi.org/v2/everything?q=plant%20disease&apiKey={API_KEY}&language=en&searchIn=title').json()['articles']

# Define a function to display news articles
def news_page():
    for random_news in list(_get_news()):
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

# Define the sections of the website for the selectbox
app_sections = ["Home", "Disease Detection", "Helpbot", "Latest News", "Feedback Forum", "Team Members"]

# Sidebar selectbox to navigate between sections
app_mode = st.sidebar.selectbox("Select Section", app_sections)

# Display the selected section
if app_mode == "Latest News":
    news_page()
elif app_mode == "Feedback Forum":
    forum()
    pass
elif app_mode == "Home":
    # Your existing code for the home section
    pass
# Add conditions for other sections as needed
