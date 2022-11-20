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
db_train = pd.read_csv(StringIO(diabetic_train_path))
db_test = pd.read_csv(StringIO(diabetic_test_path))


#diabetic_test_path = api.read("model/model.pkl", remote="model-tracker")
#diabetic_test_path = api.read("model/model.joblib", remote="model-tracker")

logging.info('test data...')
df = db_data

db = df.copy()
db = db.replace("?",np.nan)
db = db.drop(columns=["encounter_id","patient_nbr",'discharge_disposition_id',
                    'admission_source_id','payer_code', 'medical_specialty',
                    'diag_1', 'diag_2', 'diag_3',"medical_specialty"])

db = db.replace({"No":0,"Down":0, "Steady":1, "Up":1, "Ch":1,"NO":0, "<30":1, ">30":1, "Yes": 1})

db = db.replace({"[0-10)":"0-10","[10-20)":"10-20", "[20-30)":"20-30", "[30-40)":"30-40", "[40-50)":"40-50",
                "[50-60)":"50-60", "[60-70)":"60-70", "[70-80)":"70-80", "[80-90)": "80-90", "[90-100)": "90-100"})

db = db.drop(columns=["examide", "citoglipton",'glyburide-metformin', 'glipizide-metformin',
                    'glimepiride-pioglitazone', 'metformin-rosiglitazone', 'metformin-pioglitazone','acarbose', 
                    'miglitol', 'troglitazone', 'tolazamide', 'tolbutamide','acetohexamide','chlorpropamide',
                    'repaglinide', 'nateglinide'])

logger.info('creating full dataset...')
data_prepared = db
data_prepared.to_csv('dataset/data_prepared.csv')

logger.info('Data fetched and prepared...')