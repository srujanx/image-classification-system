import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import load_img, img_to_array
from tensorflow.keras.models import load_model
from PIL import Image


img_height, img_width = 180, 180  

model = load_model("app/Image_Classifier.keras")

data_cat = ['apple',
 'banana',
 'beetroot',
 'bell pepper',
 'cabbage',
 'capsicum',
 'carrot',
 'cauliflower',
 'chilli pepper',
 'corn',
 'cucumber',
 'eggplant',
 'garlic',
 'ginger',
 'grapes',
 'jalepeno',
 'kiwi',
 'lemon',
 'lettuce',
 'mango',
 'onion',
 'orange',
 'paprika',
 'pear',
 'peas',
 'pineapple',
 'pomegranate',
 'potato',
 'raddish',
 'soy beans',
 'spinach',
 'sweetcorn',
 'sweetpotato',
 'tomato',
 'turnip',
 'watermelon']


st.title("Image Classification System")
st.subheader("Upload an image of a fruit or vegetable")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocessing
    image = image.resize((img_width, img_height))
    img_array = img_to_array(image)
    img_batch = np.expand_dims(img_array, axis=0)

    # Prediction
    prediction = model.predict(img_batch)
    predicted_index = np.argmax(prediction)
    confidence = np.max(prediction) * 100

    # Result display
    st.markdown(f"**Predicted:** `{data_cat[predicted_index]}`")
    st.markdown(f"**Confidence:** `{confidence:.2f}%`")
