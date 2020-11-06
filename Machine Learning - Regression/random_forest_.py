import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline 
plt.style.use('ggplot')

#load data
dataset=pd.read_csv('Position_Salaries.csv')
X = dataset['Level'].values.reshape(-1,1)
y = dataset['Salary'].values

#run regression
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=300, random_state=0)
regressor.fit(X,y)

#visualize data
X_grid = np.arange(min(X.values), max(X.values), 0.01).reshape(-1,1)
plt.plot(X_grid, regressor.predict(X_grid))