# https://medium.com/@kalyaniavhale7/tutorial-on-gradio-library-ecb8055923a1

import gradio as gr
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
#load the dataset to pandas dataframe
URL = "http://bit.ly/w-data"
student_data = pd.read_csv(URL)
#Prepare data
X = student_data.copy()
y = student_data['Scores']
del X['Scores']
#create a machine learning model and train it
lineareg = LinearRegression()
lineareg.fit(X,y)
print('Accuracy score : ',lineareg.score(X,y),'\n')
#now the model has been trained well let test it
#function to predict the input hours
def predict_score(hours):
    hours = np.array(hours)
    pred_score = lineareg.predict(hours.reshape(-1,1))
    return np.round(pred_score[0], 2)
input = gr.components.Number(label='Number of Hours studied')
output = gr.components.Textbox(label='Predicted Score')
gr.Interface( fn=predict_score,
              inputs=input,
              outputs=output).launch();