import pandas as pd 
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt 
import math

data = pd.DataFrame({
    'Outlook': ['Sunny','Sunny','Overcast','Rain','Rain','Rain','Overcast','Sunny','Sunny','Rain','Sunny','Overcast','Overcast','Rain'],
    'Temperature': ['Hot','Hot','Hot','Mild','Cool','Cool','Mild','Hot','Cool','Mild','Mild','Mild','Hot','Mild'],
    'Humidity': ['High','High','High','High','Normal','Normal','Normal','High','Normal','Normal','Normal','High','Normal','High'],
    'Wind': ['Weak','Strong','Weak','Weak','Weak','Strong','Strong','Weak','Weak','Weak','Strong','Strong','Weak','Strong'],
    'PlayTennis': ['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
})

print(data.head())
print(" ")

def entropy(data, target_column):
    proportions = data[target_column].value_counts(normalize=True)
    entropy=-sum(p*math.log2(p) for p in proportions)
    return entropy

print(entropy(data,'PlayTennis'))

def information_gain(data,feature,target_column):
    total_entropy = entropy(data,target_column)
    weighted_entorpy = sum(
        (len(subset)/len(data))*entropy(subset,target_column) for _,subset in data.groupby(feature)
    )
    return total_entropy-weighted_entorpy

target = 'PlayTennis'
total_entropy = entropy(data,'PlayTennis')

print(" ")
def best_feature(data,target_column,features):
    ig_data = {}
    for cols in features:
        info_gain = information_gain(data,cols,target_column)
        print(f"{cols} = information_gain: {info_gain:.3f}")
        ig_data[cols]=info_gain
    best_feature = max(ig_data,key=ig_data.get)
    return best_feature

def id3(data,target_column,features):
    if len(data[target_column].unique())==1:
        return data[target_column].iloc[0]
    if len(features)==0:
        return data[target_column].mode().iloc[0]

    b_feature = best_feature(data,target_column,features)
    tree = {b_feature:{}}
    remaining_features = [f for f in features if f != b_feature]

    for value in data[b_feature].unique():
        sub=data[data[b_feature]==value]
        if sub.empty:
            tree[b_feature][value]=data[target_column].mode().iloc[0]
        else:
            tree[b_feature][value]=id3(sub,target_column,remaining_features)
    return tree

features = list(data.columns.drop('PlayTennis'))
tree = id3(data,'PlayTennis',features)
print("\n\n----------------------------")
print("\n Final Decision Tree: ")
print(" ")
print(tree)