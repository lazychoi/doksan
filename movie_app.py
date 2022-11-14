import streamlit as st
import joblib
import numpy as np
from PIL import Image

image = Image.open('sunrise.jpg')
st.image(image, caption='Sunrise by the mountains')
st.snow()

st.write("# 좋은 말 or 나쁜 말")
st.write("좋은 말 나쁜 말에 따라 어떻게 반응하는지 보세요.")

text = st.text_area

predict_button = st.button("예측")

if predict_button:
    model = joblib.load('movie.pkl')
    pred = int(model.predict(text))
    if pred > 0:
        st.write('나빠요, 그런 말 하지 마세요.')
    else:
        st.write('감사합니다.')