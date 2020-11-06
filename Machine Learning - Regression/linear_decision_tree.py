import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load data
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:2]
Y = dataset.iloc[:,2]

#run regression
from sklearn.tree import DecisionTreeRegressor
reg = DecisionTreeRegressor(random_state = 0)
reg.fit(X, Y)

#visualize data
X_grid = np.arange(min(X.values), max(X.values), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X,Y, color = 'red')
plt.plot(X_grid, reg.predict(X_grid), color = 'blue')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.title('Decision Tree')
plt.show()