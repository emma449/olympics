import os
import pandas as pd
import matplotlib.pyplot as plt

folder_path = "/Users/emmawrenn/Downloads/olympics_athletes_dataset.csv"
dataframe = pd.read_csv(folder_path)
print(dataframe.head())

def bmi_by_sport():
	dataframe['BMI'] = dataframe['weight_kg']/((dataframe['height_cm']/100)**2)
	print(dataframe.head())
	result = dataframe.groupby(['sport'])['BMI'].mean().reset_index()
	result.columns = ['sport', 'BMI']
	print(result.head())
	x = result['sport']
	y = result['BMI']
	plt.bar(x,y)
	plt.title('Average Olympic athlete BMI by sport')
	plt.xlabel('Olympic sport')
	plt.ylabel('Average athlete BMI')
	plt.show()

bmi_by_sport()