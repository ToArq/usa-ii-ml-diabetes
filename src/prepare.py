from dvc import api
import pandas as pd
import numpy as np
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

logging.info('Fetching data...')

diabetic_data_path = api.read("dataset/diabetic_data.csv", remote="dataset-tracker", encoding="utf8")
diabetic_train_path = api.read("dataset/diabetic_data.csv", remote="dataset-tracker", encoding="utf8")
diabetic_test_path = api.read("dataset/diabetic_data.csv", remote="dataset-tracker", encoding="utf8")

db_data = pd.read_csv(StringIO(diabetic_data_path))

#diabetic_test_path = api.read("model/model.pkl", remote="model-tracker")
#diabetic_test_path = api.read("model/model.joblib", remote="model-tracker")

logging.info('test data...')
df = db_data

db = df.copy()
db = db.replace("?",np.nan)
db = db.drop(columns=["encounter_id","patient_nbr",'discharge_disposition_id',
                    'admission_source_id','payer_code', 'medical_specialty',
                    'diag_1', 'diag_2', 'diag_3',"medical_specialty","examide", "citoglipton",'glyburide-metformin', 'glipizide-metformin',
                    'glimepiride-pioglitazone', 'metformin-rosiglitazone', 'metformin-pioglitazone','acarbose', 
                    'miglitol', 'troglitazone', 'tolazamide', 'tolbutamide','acetohexamide','chlorpropamide',
                    'repaglinide', 'nateglinide', 'insulin','change','diabetesMed'])

db = db.replace({"No":0,"Down":0, "Steady":1, "Up":1, "Ch":1,"NO":0, "<30":1, ">30":1, "Yes": 1})

db = db.drop(columns=)

logger.info('creating full dataset...')
data_prepared = db
data_prepared.to_csv('dataset/data_prepared.csv')

logger.info('Data fetched and prepared...')