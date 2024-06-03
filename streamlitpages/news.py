import html
import requests, streamlit as st
# from config import KEYWORD, DEFAULT_IMAGE, NEWS_API_KEY as API_KEY
from streamlit.runtime.media_file_storage import MediaFileStorageError
# API_KEY = st.secrets["NEWS_API"]
API_KEY = "8efc9c32c15e48a995ee95ea892226ee"


st.set_page_config(
    page_title='News',
    page_icon='📰',
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




def _get_news(): 
    return requests.get(f'https://newsapi.org/v2/everything?q=plant%20disease&apiKey={API_KEY}&language=en&searchIn=title').json()['articles']

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
        
        
        
if __name__ == '__main__':
    news_page()
