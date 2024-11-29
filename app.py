import streamlit as st
import numpy as np
import pickle

# Feature extraction class
class FeatureExtraction:
    def __init__(self, url):
        self.url = url

    def getFeaturesList(self):
        features = []
        
        # Example feature extraction (add your actual feature extraction logic here)
        features.append(len(self.url))  # URL length
        features.append(self.url.count('.'))  # Number of periods in the URL
        
        # Add more features until you have 30 features
        while len(features) < 30:
            features.append(0)  # Add dummy features (you should replace this with real feature extraction logic)
        
        return features

# Load the trained model
file = open("pickle/model.pkl", "rb")
gbc = pickle.load(file)
file.close()

# Streamlit title
st.title("Phishing URL Detection")

# Input field for URL
url = st.text_input("Enter URL:")

if url:
    # Feature extraction
    obj = FeatureExtraction(url)
    features_list = obj.getFeaturesList()

    # Ensure that the list has exactly 30 features
    if len(features_list) < 30:
        features_list.extend([0] * (30 - len(features_list)))  # Pad with zeros if there are fewer than 30 features

    # Reshape the feature array
    x = np.array(features_list).reshape(1, 30)

    # Prediction
    y_pred = gbc.predict(x)[0]
    y_pro_phishing = gbc.predict_proba(x)[0, 0]
    y_pro_non_phishing = gbc.predict_proba(x)[0, 1]

    # Display the result
    if y_pred == 1:  # Safe URL
        pred = "It is {0:.2f} % safe to go.".format(y_pro_phishing * 100)
    else:  # Phishing URL
        pred = "This URL is unsafe."

    # Display safety probability
    st.write(f"Safety Probability: {y_pro_non_phishing*100:.2f}%")
    st.write(pred)
else:
    st.write("Please enter a URL to check its safety.")
