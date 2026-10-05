# Fashion-MNIST Classification using ANN Project

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-orange.svg)](https://tensorflow.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)

This repository contains a deep learning classification project that trains an Artificial Neural Network (ANN) using TensorFlow and Keras to recognize and classify fashion items from the Fashion-MNIST dataset[cite: 17].

---

## Dataset Notice
*Note: The dataset (`fashion-mnist_train.csv` and `fashion-mnist_test.csv`) used in this project[cite: 17] is publicly available on Kaggle.*

---

## Dataset Features & Preprocessing
* **Pixel Normalization**: Scaling input pixel values by dividing by 255.0 to range between 0 and 1[cite: 17].
* **Labels**: 10 distinct fashion and clothing categories[cite: 17].

---

## Project Workflow
1. **Data Loading**: Reading train and test CSV files[cite: 17].
2. **Preprocessing**: Normalizing feature matrices[cite: 17].
3. **Model Architecture**: Constructing a Sequential model containing Dense layers with ReLU activations and a Softmax output layer for 10 classes[cite: 17].
4. **Model Compilation**: Compiling with the Adam optimizer and sparse categorical crossentropy loss[cite: 17].
5. **Training**: Fitting the model for 5 epochs with validation splits[cite: 17].
6. **Model Persistence**: Saving the trained neural network model into `fashion_mnist_model.h5`[cite: 17].
7. **Web Application**: Interactive deployment interface built with Streamlit.

---

## Getting Started & Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/fashion-mnist-ann.git](https://github.com/YOUR_USERNAME/fashion-mnist-ann.git)
   cd fashion-mnist-ann
