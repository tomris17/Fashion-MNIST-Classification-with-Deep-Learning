import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model

st.set_page_config(page_title="Fashion-MNIST Classification App", layout="centered")

st.title("Fashion-MNIST Classification App")
st.write(
    "Bu uygulama, Fashion-MNIST veri seti ile eğitilmiş Yapay Sinir Ağı (ANN) modelini kullanarak kıyafet görsellerini sınıflandırır."
)

@st.cache_resource
def load_nn_model():
    return load_model("fashion_mnist_model.h5")

model = load_nn_model()

class_names = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]

st.subheader("Model Durumu")
st.success("Model (fashion_mnist_model.h5) başarıyla yüklendi.")
st.write("Bu model, 784 piksellik (28x28) gri tonlamalı kıyafet görüntülerini 10 farklı kategoride sınıflandırmak üzere eğitilmiştir.")