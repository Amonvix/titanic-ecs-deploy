=======
AWS PORTFOLIO PROJECT -
=======

# 🧠 Titanic Survival Prediction – Data Science Project

This project uses a structured machine learning pipeline to predict passenger survival on the Titanic, using open data and popular Python libraries.

## 📚 Technologies Used

- **Python** (v3.12)
- **Pandas**, **NumPy** – data manipulation
- **Matplotlib**, **Seaborn** – data visualization
- **Scikit-learn** – machine learning
- **TensorFlow**, **Keras**, **PyTorch** – deep learning (to be added)
- **Jupyter** – interactive development

## 📁 Project Structure

titanic-survival-prediction/
├── data/
│ ├── titanic.csv # Raw dataset
│ └── titanic_clean.csv # Cleaned dataset
├── scripts/
│ ├── load_dataset.py # Download and save dataset
│ ├── analyze_dataset.py # Initial analysis and profiling
│ ├── clean_dataset.py # Preprocessing and feature formatting
│ └── visualize_dataset.py # Exploratory visualizations
├── requirements.txt
├── README.md
└── venv/


## ✅ Completed Tasks

- [x] Project setup and virtual environment
- [x] Required libraries installed and frozen in requirements.txt
- [x] Raw data collected and saved to local directory
- [x] Dataset analyzed with Pandas and statistics reviewed
- [x] Null values handled and categorical features encoded
- [x] Core exploratory visualizations plotted and reviewed

## ✅ Completed Tasks

## 📊 3. Exploration and Visualization
- [x] Created plots using Seaborn and Matplotlib (visualize_dataset.py)
- Survival count (bar plot)
- Age distribution (histogram with KDE)
- Survival by sex (countplot with hue)
- Feature correlation heatmap
- [x] Extracted visual insights and initial patterns

## 🧠 4. Modeling with Scikit-learn
- [x] Cleaned and converted all features to numeric format (clean_dataset.py)
- [x] Performed train/test split (80/20) using train_test_split
- [x] Trained logistic regression model (train_model.py)
- [x] Evaluated model using:
- Accuracy
- Precision
- Recall
- Confusion Matrix
- Full Classification Report

## 🧪 Upcoming Tasks

## 🤖 5. Deep Learning with TensorFlow/Keras
- [x] Build a simple feedforward neural network using Keras
- [x] Train and evaluate the model
- [x] Plot training and validation curves

## 🔁 6. Comparison with PyTorch
- [x] Build an equivalent model using PyTorch
- [x] Train and compare results side-by-side

## 🌐 7. Deployment (Bonus)
- [x] Wrap prediction logic in a Django REST API
- [x] Save trained models using dockers
- [x] Deploy via Docker in AWS ECS



## 🧬 How to Run Locally

bash
# Step 1: Activate virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Step 2: Run scripts
python scripts/load_dataset.py
python scripts/analyze_dataset.py
python scripts/clean_dataset.py
python scripts/visualize_dataset.py

This project is part of a broader portfolio aimed at showcasing skills in data analysis, model development, and clean code practices for real-world machine learning scenarios.

👨‍💻 Autor
Daniel Pedroso (Amon)
Backend Developer | Java & Python | Projects focused on quality and professional deployment.