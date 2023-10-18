# bibliotecas utilizadas

import pickle # serialização e deserialização de objetos
import numpy as np # matrizes
import pandas as pd # tratamento do conjunto de dados

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import KFold

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import roc_auc_score

# parâmetros utilizados

C = 1.0
n_splits = 5

output_file = f'model_C={C}.bin' # nome do arquivo que será gerado 

# caminho e carregamento do conjunto de dados que será utilizado
path = 'https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv' 
df = pd.read_csv(path)

# PREPARAÇÃO DOS DADOS

df.columns = df.columns.str.replace(' ', '_').str.lower()
categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)

for col in categorical_columns:
    df[col] = df[col].str.lower().str.replace(' ', '_')

df.fillna(0, inplace=True)
df.rename(columns={'msrp': 'price'}, inplace=True)

price_average = df.price.mean()
df['above_average'] = df['price'].map(lambda x: 1 if x > price_average else 0)
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
numerical = ['year', 'engine_hp', 'engine_cylinders', 'highway_mpg', 'city_mpg']
categorical = ['make', 'model', 'transmission_type', 'vehicle_style']

# VALIDAÇÃO

print(f'Validation with C={C}')

def train(df_train, y_train, C=1.0):
    dicts = df_train[categorical + numerical].to_dict(orient='records')

    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)

    model = LogisticRegression(solver='liblinear', C=C, max_iter=1000)
    model.fit(X_train, y_train)

    return dv, model

def predict(df, dv, model):
    dicts = df[categorical + numerical].to_dict(orient='records') 
    X = dv.transform(dicts)
    y_pred = model.predict_proba(X)[:, 1]

    return y_pred

kfold = KFold(n_splits=n_splits, shuffle=True, random_state=1)

auc_scores = []
fold = 0

for train_index, val_index in kfold.split(df_full_train):
    df_train = df_full_train.iloc[train_index]
    df_val = df_full_train.iloc[val_index] 

    y_train = df_train.above_average.values
    y_val = df_val.above_average.values

    dv, model = train(df_train, y_train)
    y_pred = predict(df_val, dv, model)

    auc = roc_auc_score(y_val, y_pred)
    auc_scores.append(auc)

    print(f'auc on fold {fold} is {auc}')
    fold += 1

mean_auc = np.mean(auc_scores)
std_auc = np.std(auc_scores)

print(f"Mean AUC across {n_splits} folds: {mean_auc:.4f}")
print(f"Standard Deviation of AUC across {n_splits} folds: {round(std_auc, 3)}")

# TREINAMENTO E TESTE DO MODELO FINAL

print(f'Training the final model...')

dv, model = train(df_full_train, df_full_train.above_average.values, C=1.0)
y_pred = predict(df_test, dv, model)

y_test = df_test.above_average.values

auc = roc_auc_score(y_test, y_pred)
auc

print(f'auc on test is {auc:.4f}')

# SALVANDO O MODELO

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print(f'the model is saved to {output_file}.')