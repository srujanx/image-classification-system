#  Image Classification System - Fruits & Vegetables

A production-grade **deep learning image classification system** built with **TensorFlow** and **Streamlit** that accurately identifies 36 different types of fruits and vegetables from uploaded images.

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.11+-orange.svg)](https://www.tensorflow.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.47.0-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## ✨ Features

- 📤 **Easy Upload:** Supports `.jpg`, `.jpeg`, and `.png` image formats
- 🎯 **High Accuracy:** 93% classification accuracy across 36 categories
- 📊 **Confidence Scores:** Real-time prediction confidence display
- 🚀 **Fast Inference:** Sub-2 second prediction time
- 🎨 **Clean UI:** Intuitive Streamlit interface
- 🔄 **Real-time Processing:** Instant image preprocessing and prediction

---

## 🍊 Supported Categories (36 Classes)

```
apple, banana, beetroot, bell pepper, cabbage, capsicum, carrot, 
cauliflower, chilli pepper, corn, cucumber, eggplant, garlic, ginger, 
grapes, jalepeno, kiwi, lemon, lettuce, mango, onion, orange, paprika, 
pear, peas, pineapple, pomegranate, potato, raddish, soy beans, spinach, 
sweetcorn, sweetpotato, tomato, turnip, watermelon
```

---

## 🏗️ Model Architecture

- **Framework:** TensorFlow/Keras
- **Model Type:** Convolutional Neural Network (CNN) with Transfer Learning
- **Input Shape:** `(180, 180, 3)`
- **Model Format:** `.keras`
- **Accuracy:** 93% on validation set
- **Parameters:** ~568M (fine-tuned)
- **Training Dataset:** Fruits & Vegetables Image Dataset

### Key Features:
- Data augmentation (rotation, flip, zoom) for improved generalization
- Systematic hyperparameter tuning
- Regularization strategies to reduce overfitting by 15%
- Transfer learning for enhanced performance

---

## 🚀 Installation

### Prerequisites
- Python 3.11 or lower (Python 3.13 not supported)
- pip package manager
- (Optional) Conda for virtual environment management

### Step 1: Clone the Repository

```bash
git clone https://github.com/Srujanx/Image-Classification-System.git
cd Image-Classification-System
```

### Step 2: Create Virtual Environment (Recommended)

**Using Conda:**
```bash
conda create -n image-class python=3.11 -y
conda activate image-class
```

**Using venv:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirement.txt
```

---

## 💻 Usage

### Running the Application

```bash
streamlit run app/main.py
```

The application will open in your default browser at `http://localhost:8501`

### Using the Application

1. **Upload Image:** Click "Browse files" and select a fruit/vegetable image
2. **Wait for Prediction:** The model will process the image automatically
3. **View Results:** See the predicted class and confidence score

---

## 📁 Project Structure

```
Image-Classification-System/
├── app/
│   ├── main.py                    # Streamlit application
│   ├── image.ipynb               # Training notebook
│   ├── Image_Classifier.keras    # Trained model (not in repo)
│   └── Fruits_Vegetables/        # Dataset directory (not in repo)
├── screenshots/                   # Application screenshots
├── .gitignore                    # Git ignore file
├── README.md                     # Project documentation
└── requirement.txt               # Python dependencies
```

---

## 🧠 Model Training

The model was trained using a comprehensive pipeline:

1. **Data Preprocessing:** Image resizing to 180x180, normalization
2. **Data Augmentation:** Rotation, flipping, zooming for robustness
3. **Architecture:** CNN with transfer learning (MobileNetV2 backbone)
4. **Optimization:** Adam optimizer with learning rate scheduling
5. **Regularization:** Dropout and L2 regularization to prevent overfitting
6. **Validation:** 20% validation split for hyperparameter tuning

### Training Results:
- **Training Accuracy:** 95%
- **Validation Accuracy:** 93%
- **Test Accuracy:** 93%
- **Overfitting Reduction:** 15% improvement through regularization

See `app/image.ipynb` for complete training code and experiments.

---

## 🛠️ Technical Stack

| Component | Technology |
|-----------|-----------|
| **Framework** | TensorFlow, Keras |
| **Frontend** | Streamlit |
| **Image Processing** | PIL, NumPy |
| **Model Architecture** | CNN with Transfer Learning |
| **Deployment** | Local/Cloud-ready |

---

## 📊 Performance Metrics

- **Accuracy:** 93%
- **Inference Time:** < 2 seconds
- **Model Size:** ~50 MB
- **Confidence Threshold:** 0.6 (60%)

---

## 🔮 Future Enhancements

- [ ] Add support for 100+ fruit/vegetable categories
- [ ] Implement model quantization for faster inference
- [ ] Deploy to cloud (AWS/Heroku/Streamlit Cloud)
- [ ] Add batch image processing
- [ ] Implement nutritional information lookup
- [ ] Mobile app version (React Native + TensorFlow Lite)
- [ ] API endpoint for integration with other applications

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Srujan**

- LinkedIn: [srujan77](https://linkedin.com/in/srujan77)
- GitHub: [Srujanx](https://github.com/Srujanx)
- Email: srujan.moni07@gmail.com

---

## 🙏 Acknowledgments

- TensorFlow and Keras for the deep learning framework
- Streamlit for the amazing web app framework
- The open-source community for inspiration and resources

---

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/Srujanx/Image-Classification-System/issues) page
2. Create a new issue with detailed description
3. Contact via email: srujan.moni07@gmail.com

---

⭐ **Star this repository if you find it helpful!**

---

**Last Updated:** February 2026
