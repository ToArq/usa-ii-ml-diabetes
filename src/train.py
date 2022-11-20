#General libraries 
import pandas as pd
import numpy as np
import seaborn as sns
from utils import update_model, save_simple_metric_report, get_model_performance_test_set

#Pipeline creation libraries
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler

#Modeling libraries
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression

#Hyperparameter tunning
from sklearn.model_selection import GridSearchCV

#Automation libraries
from joblib import dump

#Database conection
from io import StringIO
import sys
import logging


logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(name)s: %(message)s',
    level=logging.INFO,
    datefmt='%H:%M:%S',
    stream=sys.stderr
)

logger = logging.getLogger(__name__)


logger.info('Loading data...')
data = pd.read_csv('dataset/data_prepared.csv')

logger.info('Setting data transformers...')
numeric_pipeline = Pipeline(
    [
        ('Imputación con la media',   SimpleImputer(strategy='mean')),
        ('Escalado minmax', MinMaxScaler())
        
    ]
)
categorical_pipeline = Pipeline(
        [
            ('imputación moda', SimpleImputer(strategy='most_frequent')),
            ('onehot encoder', OneHotEncoder(handle_unknown="ignore",sparse=False))
        ]
)

column_transformer = ColumnTransformer(
    [
        ('numeric pipeline', numeric_pipeline,[4,5,6,7,8,9,10,11,12,15,16,17,18,19,20]),
        ('categorical pipeline', categorical_pipeline,[0,1,2,3,13,14])
    ]
)

logger.info('Spliting and preparing training data...')

train, test = train_test_split(data, test_size=0.3, 
                               random_state=42,
                              stratify=data['readmitted'])

features = [['race', 'gender', 'age', 'weight', 'admission_type_id',
       'time_in_hospital', 'num_lab_procedures', 'num_procedures',
       'num_medications', 'number_outpatient', 'number_emergency',
       'number_inpatient', 'number_diagnoses', 'max_glu_serum', 'A1Cresult',
       'metformin', 'glimepiride', 'glipizide', 'glyburide', 'pioglitazone',
       'rosiglitazone']]

#Train
train = train.dropna()
X_train = train[features[0]]
y_train = train['readmitted']
X_train = X_train.dropna()

#Test
test = test.dropna()
X_test = test[features[0]]
y_test = test['readmitted']
X_test = X_test.dropna()


logger.info('Setting Logistic Regression model...')

final_pipeline = Pipeline(
    [
        ('preprocesamiento', column_transformer),
        ('modelo',LogisticRegression(max_iter=1000))
    ]
)

logger.info('Setting results...')
results = cross_validate(final_pipeline,X_train,y_train,
                        cv=10, return_train_score=True,
                        #scoring=['accuracy', 'f1', 'precision', 'recall'])
                        scoring=['accuracy', 'f1', 'precision', 'recall'])

accuracy_train_score = results['train_accuracy'].mean()
accuracy_test_score = results['test_accuracy'].mean()

f1_train_score = results['train_f1'].mean()
f1_test_score = results['test_f1'].mean()

precision_train_score = results['train_precision'].mean()
precision_test_score = results['test_precision'].mean()

recall_train_score = results['train_recall'].mean()
recall_test_score = results['test_recall'].mean()


logger.info('Printing results...')

print('---'*30)
print('train Accuracy ', results['train_accuracy'].mean(),'+-', results['train_accuracy'].std())
print('val Accuracy', results['test_accuracy'].mean(),'+-', results['test_accuracy'].std())
print('---'*30)
print('train f1 ', results['train_f1'].mean(),'+-', results['train_f1'].std())
print('val f1', results['test_f1'].mean(),'+-', results['test_f1'].std())
print('---'*30)
print('train precision ', results['train_precision'].mean(),'+-', results['train_precision'].std())
print('val precision', results['test_precision'].mean(),'+-', results['test_precision'].std())
print('---'*30)
print('train recall ', results['train_recall'].mean(),'+-', results['train_recall'].std())
print('val recall', results['test_recall'].mean(),'+-', results['test_recall'].std())
print('---'*30)


logger.info('Fitting model...')
final_pipeline.fit(X_train, y_train)


logger.info('updating model...')
update_model(final_pipeline)


logger.info('Generating model report...')

save_simple_metric_report(accuracy_train_score, accuracy_test_score, final_pipeline)

y_test_pred = final_pipeline.predict(X_test)
get_model_performance_test_set(y_test, y_test_pred)


logger.info('Training finished, thank you! xx...')

