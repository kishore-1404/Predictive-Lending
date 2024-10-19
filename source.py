import pandas as pd
import numpy as np

from scipy import stats

import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score


# Data Directory
data_dir = 'dataset/'

# Load the data
train_1 = pd.read_csv(data_dir + 'train_1.csv')
train_2_1 = pd.read_csv(data_dir + 'train_2_1.csv')
train_2_2 = pd.read_csv(data_dir + 'train_2_2.csv')
test_1 = pd.read_csv(data_dir + 'test_1.csv')
test_2_1 = pd.read_csv(data_dir + 'test_2_1.csv')
test_2_2 = pd.read_csv(data_dir + 'test_2_2.csv')

# Merge the data
train = pd.merge(train_1, train_2_1, on='id', how='left')
train = pd.merge(train, train_2_2, on='id', how='left')
test = pd.merge(test_1, test_2_1, on='id', how='left')
test = pd.merge(test, test_2_2, on='id', how='left')

# Handle missing values and outliers
train.fillna(train.mean(), inplace=True)
test.fillna(test.mean(), inplace=True)

# Detect outliers using Z-score
z_scores = np.abs(stats.zscore(train.select_dtypes(include=[np.number])))
outliers = np.where(z_scores > 3)  # Outliers are usually z-scores > 3

# Remove outliers
train = train[(z_scores < 3).all(axis=1)] # Remove rows with outliers

#Feauture Engineering 
# from the column 'prod' create 'prod_num' from the text of the column as 'prod[num]' extract the number
train['prod_num'] = train['prod'].str.extract('(\d+)') 

# Split train data into X (features) and y (target)
X = train.drop(columns=['loan_id', 'id', 'label'])
y = train['label']

# Split the training data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)


# Initialize XGBoost model
xgb_model = xgb.XGBClassifier(
    use_label_encoder=False,
    eval_metric='auc',
    random_state=42
)

# Train XGBoost model
xgb_model.fit(X_train, y_train)

# Predict probabilities for validation set
y_val_pred_proba_xgb = xgb_model.predict_proba(X_val)[:, 1]

# Evaluate using ROC AUC Score
auc_score_xgb = roc_auc_score(y_val, y_val_pred_proba_xgb)
print(f"XGBoost ROC AUC Score: {auc_score_xgb}")