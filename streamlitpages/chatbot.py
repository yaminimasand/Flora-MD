import streamlit as st
from hugchat import hugchat
from hugchat.login import Login
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

configure()

# Login Credentials
HF_EMAIL = os.getenv("HF_EMAIL")
HF_PASS = os.getenv("HF_PASS")
BASE_PROMPT = "I want you to act as a virtual assistant for farmers and come up with conventional treatments for plant diseases. You should be able to recommend conventional  methods to resolve the plant disease and other natural alternatives.\n\n"

flag = 0

st.set_page_config(
    page_title='ChatBot',
    page_icon='🤖',
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


def chat_bot():

    # Store LLM generated responses
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [{"role": "assistant", "content": "Hi! How may I help you?"}]

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Function for generating LLM response
    def generate_response(prompt_input, email, passwd):

        # Hugging Face Login
        sign = Login(email, passwd)
        cookies = sign.login()
        # Create ChatBot                            
        chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

        global flag
        if flag<1:
            flag+=1
            prompt_input=BASE_PROMPT+prompt_input
        return str(chatbot.chat(prompt_input)).strip('`')

    # User-provided prompt
    if prompt := st.chat_input(disabled=not (HF_EMAIL and HF_PASS)):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

    # Generate a new response if last message is not from assistant
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_response(prompt, HF_EMAIL, HF_PASS) 
                st.write(response) 
        message = {"role": "assistant", "content": response}
        st.session_state.messages.append(message)

if __name__ == '__main__':
    chat_bot()
