import pickle
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
total_sensor_values=[]
total_PWMs=[]
for i in range(1,38):
    with open(os.path.join(os.path.dirname(__file__), 'feature'+str(i)+'.pickle'), 'rb') as f:
         sensor_values = pickle.load(f)
    with open(os.path.join(os.path.dirname(__file__), 'target'+str(i)+'.pickle'), 'rb') as f:
         PWMs = pickle.load(f)
    int_PWMs= list(map(int,PWMs))
    total_sensor_values.extend(sensor_values)
    total_PWMs.extend(int_PWMs)
print(len(total_sensor_values))
print(len(total_PWMs))
x_train, x_test, y_train, y_test = train_test_split(total_sensor_values, total_PWMs, test_size = 0.25, random_state = 5)
model = RandomForestClassifier(200)
model.fit(x_train, y_train)
predicted = model.predict(x_train)
print('訓練集: ',model.score(x_train, y_train))
print('測試集: ',model.score(x_test, y_test))
print('特徵重要程度: ',model.feature_importances_)
with open(os.path.join(os.path.dirname(__file__), 'model.pickle'), 'wb') as f:
     pickle.dump(model, f)
