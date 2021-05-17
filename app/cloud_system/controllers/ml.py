#machine learning packages 
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier

def trim_all_columns(df):
    """
    Trim whitespace from ends of each value across all series in dataframe
    """
    trim_strings = lambda x: x.strip() if isinstance(x, str) else x
    return df.applymap(trim_strings)

#machine learning section 
# Decision Tree
#data cleaning
data = pd.read_csv('../../../data_analysis/heatAlerts.csv')
df = data[data['outcome'] != "."]
for i in range(1,10):
    df = df.drop(['Unnamed: 4' + str(i)], axis = 1)
df = trim_all_columns(df)
df = df[df['SB_HTENDS'] != '.']
df.dropna(subset = ['ID','DIMatheat', 'SB_PROB', 'Heat Probability Category', 'DC_ACLEV', 'DC_ACTIM'], inplace = True)
df2 = pd.DataFrame(columns = df.columns)

for index, row in df.iterrows():
    try:
        i = int(row['DC_ACLEV'])
        df2.loc[len(df2.index)] = row
    except: 
        continue
df = df2
data_with_outcome = df

#training model 
data_with_outcome = data_with_outcome[(data_with_outcome['outcome']=="P") | (data_with_outcome['outcome']=="O") | (data_with_outcome['outcome']=="A")]
new_sb_htstarts = pd.to_timedelta(data_with_outcome['SB_HTSTARTS'])
new_sb_htends = pd.to_timedelta(data_with_outcome['SB_HTENDS'])  
data_with_outcome['time_elapsed'] = new_sb_htends - new_sb_htstarts
data_with_outcome['sc_elapsed'] = data_with_outcome.time_elapsed.dt.total_seconds()
data_with_outcome.dropna(subset = ['sc_elapsed'], inplace = True)

Y = data_with_outcome['outcome']
X = data_with_outcome.drop(columns=['outcome'])
Y[Y=="P"] = 1
Y[Y=="A"] = 1  # aborted is also pregnant
Y[Y=="O"] = 0
Y = Y.astype(int)
X = X[['DIMatheat', 'SB_PROB', 'Heat Probability Category', 'DC_ACLEV', 'DC_ACTIM', 'sc_elapsed']]
x_train, x_test, y_train, y_test = train_test_split(X.to_numpy(), Y.to_numpy(), test_size=0.33, random_state=42)
clf = AdaBoostClassifier(base_estimator=DecisionTreeClassifier(max_depth=2), n_estimators=20, random_state=0)
clf.fit(x_train, y_train)

#neural network
clf2 = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
clf2.fit(X, Y)
