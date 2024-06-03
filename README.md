# Flora-MD
This repository houses a robust implementation of plant disease detection leveraging a Convolutional Neural Network (CNN) architecture developed from scratch. Alongside the CNN model, a user-friendly web application has been crafted, enabling users to effortlessly upload images of plants. Upon submission, the CNN model swiftly classifies the plant's health status, distinguishing between a healthy state and instances of powdery mildew or rust infestation.

Notably, this application offers comprehensive language support, accommodating users from diverse linguistic backgrounds by providing translations in all Indian regional languages. Furthermore, the platform boasts additional features, including an interactive chatbot, a curated news section, and practical solutions for identified plant diseases. Users can also access links to purchase relevant products, enhancing their ability to address plant health issues effectively.

Coupled with its elegant and intuitive user interface design, this application seamlessly blends aesthetics with functionality, ensuring an enriching user experience.

***
NOTE:
Download Weights: <a href="https://www.mediafire.com/file/1j3dwd2pzs7xc13/weights.rar/file">link.</a> 
***


Introduction
---
Plant diseases pose a significant threat to crop yield, often leading to substantial losses. Timely detection and intervention play a pivotal role in containing their spread and mitigating potential damage. Our Streamlit web application offers a user-friendly interface, empowering users to effortlessly upload images of plants. Leveraging a Convolutional Neural Network (CNN) model, the application accurately predicts the health status of the plant, aiding in prompt decision-making.

Moreover, our platform goes beyond mere diagnosis. With features tailored to cater to diverse user needs, we've integrated multi-lingual support for seamless accessibility. Users can interact with a robust chatbot, stay informed through curated news updates, and access comprehensive solutions alongside convenient product links, ensuring holistic support in plant care endeavors.

In essence, our application amalgamates cutting-edge technology with user-centric design, fostering proactive plant disease management and enhancing agricultural sustainability.

Prerequisites
---
Before running the application, make sure you have the following dependencies installed:

-Python>=3.6 -Streamlit>=1.0 -numpy>=1.20.3 -pandas>=1.3.3 -textblob>=0.15.3 -toml>=0.10.2 -requests>=2.26.0 -streamlit-lottie>=0.0.6 -streamlit-option-menu>=1.0.3 -hugchat>=0.2.0 -tensorflow>=2.7.0 -Pillow>=8.4.0 -googletrans>=4.0.0

The model weights file (plant_disease_classifier.h5) should be download from the link provided before.
You can install the required packages using pip:

pip install tensorflow streamlit numpy pillow

Usage
---
1. Clone the repository:
   ```
   git clone
   cd Plant_Disease_Detection_using_CNN
   ```
2. Place the model weights file (plant_disease_classifier.h5) in the weights directory.
3. Run the Streamlit app:
   ```
   streamlit run main_app.py
   ```
4. The web app will open in your default web browser, allowing you to upload plant images for disease classification.

Model
---
The model used for plant disease classification is a CNN model. It has been trained to classify plants into one of the following categories:

* Healthy
* Powdery
* Rust
The model's architecture and weights are loaded from the plant_disease_classifier.h5 file.

Demo
---
To see a live demo of the web app, you can visit <a href="https://plant-disease-detection-pkue.onrender.com/">this link.</a>

License
---
This project is licensed under the MIT License.
