# Rainfall-Prediction
The goal is to predict rainfall based on various meteorological features such as temperature, humidity, pressure, and others. The trained model is saved as a .pkl file for deployment and reuse.This project demonstrates a Rainfall Prediction Model built using the Random Forest Algorithm. The goal is to predict rainfall based on various meteorological features such as temperature, humidity, pressure, and others. The trained model is saved as a .pkl file for deployment and reuse. <br/>
<br/>

## Features
* Data preprocessing pipeline
* Random Forest model implementation
* Saved model file for predictions
* Example notebook for training and evaluation <br/>
<br/>

## Installation
1. Clone the repository:
   
   ```bash
   git clone https://github.com/Shah114/Rainfall-Prediction.git
   cd Rainfall-Prediction
   ```

2. Install the required dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```

<br/>

## Usage
1. Data Loading and Preprocessing
The notebook data_preprocessing.ipynb contains the data loading and preprocessing steps. Ensure the dataset is available in the data/ directory.
<br/>

2. Training the Model
Run the notebook train_model.ipynb to train the Random Forest model. This notebook includes:

* Loading preprocessed data
* Training the model
* Evaluating model performance
* 
The trained model will be saved as model/random_forest_model.pkl.

<br/>
3. Making Predictions
