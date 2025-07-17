# Image Classification System (Fruits & Vegetables)

This project is a deep learning-powered **image classification system** built with **Streamlit** and **TensorFlow**. It identifies fruits and vegetables from uploaded images with high accuracy.

##  Features

- Upload an image of a fruit or vegetable (`.jpg`, `.jpeg`, `.png`)
- Model predicts the class label with confidence score
- Supports 36 different fruit and vegetable categories
- Responsive web interface built with Streamlit



### Upload Image
![Upload Screenshot](/Users/srujanappu/image_classification_system/screenshots/Image_5.jpg)

### Prediction Result
![Prediction Screenshot](/Users/srujanappu/image_classification_system/screenshots/working_model.png)

##  Model Details

- Format: `.keras`
- Input shape: `(180, 180, 3)`
- Framework: TensorFlow/Keras

##  Installation

```bash
# Clone the repository
git clone https://github.com/Srujanx/image-classification-system.git
cd image-classification-system

# (Optional) Create a virtual environment
conda create -n tf-env python=3.9 -y
conda activate tf-env

# Install dependencies
pip install -r requirements.txt
