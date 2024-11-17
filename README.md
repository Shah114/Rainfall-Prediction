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
  
The trained model will be saved as model/rainfall_prediction.pkl.

<br/>

3. Making Predictions <br/>

   Use the saved model for predictions:

   ```python
   import pickle
   
   # Load the model
   with open('model/rainfall_prediction.pkl', 'rb') as f:
       model = pickle.load(f)
   
   # Example prediction
   model = model_data["model"]
   feature_names = model_data["feature_names"]
   
   input_data = (1015.9, 19.9, 95, 81, 0.0, 40.0, 13.7)
   input_df = pd.DataFrame([input_data], columns=feature_names)
   
   prediction = model.predict(input_df)
   print("Prediction result:", "Rainfall" if prediction[0] == 1 else "No rainfall")
   ```
