import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz

train = pd.read_csv("./train.csv")

features = ['encoded reputation', 'gender'] # and however we're going to deal with location


