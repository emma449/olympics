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
	return dataframe
	
	#data = dataframe returned from bmi_by_sport
	def predict_medal(data, sport):
	sport_data = data[data['sport']==sport]
	sport_data['past_medalist'] = sport_data['total_medals_won'].apply(lambda x: 1 if x>=1 else 0)

	sport_data['month_of_birth'] = sport_data['date_of_birth'].apply(lambda x: int(x[5:7]))

	label_encoder = LabelEncoder()
	categories = ['gender', 'nationality', 'country_name', 'event', 'is_record_holder']
	for i in range(len(categories)):
		sport_data[f'{categories[i]}_encoded'] = label_encoder.fit_transform(sport_data[f'{categories[i]}'])
	print(sport_data.head())

	features = ['gender_encoded', 'age', 'nationality_encoded', 'country_name_encoded', 'event_encoded', 'year', 'total_olympics_attended', 'country_total_gold', 'country_total_medals', 'country_first_participation', 'country_best_rank', 'is_record_holder_encoded', 'height_cm', 'weight_kg', 'BMI', 'month_of_birth']
	x = sport_data[features]
	y = sport_data['past_medalist']
	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=16)
	model = LinearRegression()
	model.fit(x_train, y_train)
	y_pred = model.predict(x_test)
	mae = metrics.mean_absolute_error(y_test, y_pred)
	print(f'mean absolute error for linear regression: {mae}')
	return sport_data


