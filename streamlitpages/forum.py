import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from textblob import TextBlob
import toml

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

st.set_page_config(
    page_title='Feedback',
    page_icon='👥',
    layout='wide',
    initial_sidebar_state='collapsed'
)

lottie2 = """
<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
<lottie-player src="https://lottie.host/b60fff1d-cbeb-4d41-aba1-b624200c0513/OoZwK6n4cr.json"  background="transparent"  speed="1"  style="width: 1000px; height: 1000px;"  loop  autoplay></lottie-player>
"""

st.markdown("""
    <style>
        iframe {
            position: fixed;
            top: 2rem;
            bottom: ;
            left: 0;
            right: 0;
            margin: auto;
            z-index=-1;
        }
        .nav-pills {
            position: relative;
            z-index: 10; /* Ensure the option menu is above the Lottie animation */
        }
    </style>
    """, unsafe_allow_html=True
)


st.components.v1.html(lottie2, width=1010, height=1300)

app_mode = st.sidebar.selectbox(
    "Please navigate through the different sections of our website from here",
    ["Home", "Disease Detection", "Helpbot", "Latest News","Feedback Forum", "Team Members"],
)

st.write("<h1>Feedback forum</h1>", unsafe_allow_html=True)

with st.sidebar:
    st.image("assets/logo.png")
    st.info("""
            # About
            This is a web app to predict the disease in a plant using Convolutional Neural Network (CNN).
            
            # Contact
            For inquiries, you can mail us [here](mailto:mohrilsiddharth@gmail.com).
            """)

home_page = st.empty()
display_image = st.empty()
classifying_text = st.empty()
button = st.empty()

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

# Display the banner card
uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
if uploaded_image is not None:
    st.markdown(
        f'<div class="banner-card"><img src="data:image/jpeg;base64,{uploaded_image.read().encode("base64").decode()}"></div>',
        unsafe_allow_html=True
    )

# Read data from the specified worksheet with headers specified
data = conn.read(worksheet="Forum", headers="first_row")

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Filter out rows with empty feedback
df = df.dropna(subset=["Feedback"])

# Display feedback in a Streamlit expander
with st.expander("Community Reviews"):
    for index, row in df.iterrows():
        sentiment = row["Sentiment"]
        feedback = row["Feedback"]
        if sentiment.lower() == "positive":
            st.success(f"👍 Positive Feedback: {feedback}")
        elif sentiment.lower() == "negative":
            st.error(f"👎 Negative Feedback: {feedback}")
        else:
            st.warning(f"Unrecognized sentiment: {sentiment}")

# Create an input field for feedback
feedback_input = st.text_area("Enter Feedback")

# Perform sentiment analysis using TextBlob
blob = TextBlob(feedback_input)
sentiment = blob.sentiment.polarity
sentiment_label = "Positive" if sentiment > 0 else "Negative" if sentiment < 0 else "Neutral"

# Add a button to submit the feedback and sentiment
if st.button("Submit"):
    # Append the new feedback and sentiment to the DataFrame
    new_entry = {"Sentiment": sentiment_label, "Feedback": feedback_input}
    df = df.append(new_entry, ignore_index=True)
    
    # Write the updated DataFrame back to the Google Sheets document
    conn.update(worksheet="Forum", data=df.values.tolist())

    st.success("Feedback submitted successfully!")
