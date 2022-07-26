import pickle
import os
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt



for i in range(1,4):
    with open(os.path.join(os.path.dirname(__file__), 'feature'+str(i)+'.pickle'), 'rb') as f:
        sensor_values = pickle.load(f)
    with open(os.path.join(os.path.dirname(__file__), 'target'+str(i)+'.pickle'), 'rb') as f:
        PWMs = pickle.load(f)
int_PWMs= list(map(int,PWMs))
scaler_X = MinMaxScaler(feature_range=(0, 1)).fit(sensor_values)
X_scaled = scaler_X.transform(sensor_values)
print(X_scaled)

x_train, x_test, y_train, y_test = train_test_split(X_scaled,int_PWMs ,random_state=1)
model = MLPClassifier(hidden_layer_sizes=(100,100), activation='relu',  solver='adam', alpha=0.0001, batch_size='auto', learning_rate='constant', learning_rate_init=0.001, power_t=0.5, max_iter=15000, shuffle=True, random_state=None, tol=0.0001, verbose=10, warm_start=False, momentum=0.9, nesterovs_momentum=True, early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08, n_iter_no_change=10, max_fun=200).fit(x_train, y_train)
print(model.score(x_test, y_test))
with open(os.path.join(os.path.dirname(__file__), 'model.pickle'), 'wb') as f:
    pickle.dump(model, f)
