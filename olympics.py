import os, pandas as pd, matplotlib.pyplot as plt, numpy as np


folder_path = "SET PATH"
dataframe = pd.read_csv(folder_path)
print(dataframe.head())

def bmi_by_sport(dataframe):
	dataframe['BMI'] = dataframe['weight_kg']/((dataframe['height_cm']/100)**2)
	print(dataframe.head())
	result = dataframe.groupby(['sport'])['BMI'].mean().reset_index()
	result.columns = ['sport', 'Average BMI for the sport']
	dataframe = pd.merge(dataframe, result, on='sport', how='inner')
	print(dataframe.head())
	summer_frame = dataframe[dataframe['games_type']=='Summer']
	winter_frame = dataframe[dataframe['games_type']=='Winter']
	x_summer = summer_frame['sport']
	y_summer = summer_frame['Average BMI for the sport']
	x_winter = winter_frame['sport']
	y_winter = winter_frame['Average BMI for the sport']

	fig, axes = plt.subplots(1, 2, figsize=(15, 5))

	axes[0].bar(x_summer, y_summer, color='indianred')
	axes[0].set_title("Summer Olympics")
	axes[0].set_xlabel("Sport")
	axes[0].set_ylabel("Average athlete BMI")
	axes[0].set_xticks(x_summer)
	axes[0].set_xticklabels(x_summer, rotation=45, ha='right')

	axes[1].bar(x_winter, y_winter, color='lightskyblue')
	axes[1].set_title("Winter Olympics")
	axes[1].set_xlabel("Sport")
	axes[1].set_ylabel("Average athlete BMI")
	axes[1].set_xticks(x_winter)
	axes[1].set_xticklabels(x_winter, rotation=45, ha='right')

	plt.suptitle('Average Olympic athlete BMI by sport')
	plt.tight_layout()
	plt.show()

bmi_by_sport(dataframe)
