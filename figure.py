# %%
# import the necessary packages
import numpy as np
import pandas as pd
import plotly.express as px

# read in the csv 
df = pd.read_csv('data/dataset.csv')


# four datasets to be visualized
'''
distance per date 
calories per date 
average speed per date 
walking duration per date
'''

date_and_distance_df = df[['Date','Distance (m)']]
date_calories_df = df[['Date','Calories (kcal)']]
date_avgspeed_df = df[['Date','Average speed (m/s)']]
date_walkingduration_df = df[['Date','Walking duration (ms)']]

# drop empty ones 

date_and_distance_df = date_and_distance_df.dropna()
date_calories_df = date_calories_df.dropna()
date_avgspeed_df = date_avgspeed_df.dropna()
date_walkingduration_df = date_walkingduration_df.dropna()

# we'd like the dates to be actual dates as supposed to strings or integers. 
date_and_distance_df['Date'] = pd.to_datetime(date_and_distance_df['Date'])
date_calories_df['Date'] = pd.to_datetime(date_calories_df['Date'])
date_avgspeed_df['Date'] = pd.to_datetime(date_avgspeed_df['Date'])
date_walkingduration_df['Date'] = pd.to_datetime(date_walkingduration_df['Date'])

# %%
date_and_distance_df

# %%
date_calories_df

# %%
date_avgspeed_df

# %%


figure_date_distance = px.bar(date_and_distance_df, x='Date', y='Distance (m)',
             title='Distance Traveled in bar form')
figure_date_distance.show()


figure_date_distance.write_image("./distanceperdate.svg")



# %% [markdown]
# ![](./distanceperdate.svg)

# %%
figure_date_distance_scatter = px.scatter(date_and_distance_df, x='Date', y='Distance (m)', size='Distance (m)',
                  title='Distance Traveled in scatter form', color='Distance (m)')
figure_date_distance_scatter.show()

figure_date_distance_scatter.write_image("./distanceperdatescatter.svg")


# %% [markdown]
# ![](./distanceperdatescatter.svg)

# %%
figure_date_calories = px.scatter((date_calories_df), x='Date', y='Calories (kcal)', size='Calories (kcal)', color='Calories (kcal)', title='Calories Burned in scatter form')
figure_date_calories.show()

figure_date_distance_scatter.write_image("./caloriesperdate.svg")


# %% [markdown]
# ![](./caloriesperdate.svg)

# %% [markdown]
# []('./fig2.svg')

# %%
figure_average_speed = px.scatter(date_avgspeed_df, x='Date', y='Average speed (m/s)', size='Average speed (m/s)', color='Average speed (m/s)', title='Average Speed in scatter form')


figure_average_speed.show()

figure_average_speed.write_image("./average_speed.svg")
# 



# %% [markdown]
# ![](./average_speed.svg)

# %%
figure_date_walkingduration = px.scatter(date_walkingduration_df, x='Date', y='Walking duration (ms)', size='Walking duration (ms)', color='Walking duration (ms)', title='Walking Duration in scatter form')

figure_date_walkingduration.show()


figure_date_walkingduration.write_image("./walkingduration.svg")

# %% [markdown]
# ![](./walkingduration.svg)


