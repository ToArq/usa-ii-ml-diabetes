from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_null_prediction():
    response = client.post('/v1/prediction', json = {
                                                    "race": "Other",
                                                    "gender": "Male",
                                                    "age": "[10-20)",
                                                    "weight": "[0-25)",
                                                    "admission_type_id": 1,
                                                    "time_in_hospital": 1,
                                                    "num_lab_procedures": 1,
                                                    "num_procedures": 0,
                                                    "num_medications": 1,
                                                    "number_outpatient": 0,
                                                    "number_emergency": 0,
                                                    "number_inpatient": 0,
                                                    "number_diagnoses": 0,
                                                    "max_glu_serum": "None",
                                                    "A1Cresult": "None",
                                                    "metformin": 0,
                                                    "glimepiride": 0,
                                                    "glipizide": 0,
                                                    "glyburide": 0,
                                                    "pioglitazone": 0,
                                                    "rosiglitazone": 0
                                                    })
    assert response.status_code == 200
    assert response.json()['readmitted'] == 0

def test_random_prediction():
    response = client.post('/v1/prediction', json = {
                                                    "race": "Asian",
                                                    "gender": "Female",
                                                    "age": "[20-30)",
                                                    "weight": "[50-75)",
                                                    "admission_type_id": 6,
                                                    "time_in_hospital": 3,
                                                    "num_lab_procedures": 13,
                                                    "num_procedures": 5,
                                                    "num_medications": 57,
                                                    "number_outpatient": 13,
                                                    "number_emergency": 5,
                                                    "number_inpatient": 7,
                                                    "number_diagnoses": 1,
                                                    "max_glu_serum": "None",
                                                    "A1Cresult": ">7",
                                                    "metformin": 1,
                                                    "glimepiride": 1,
                                                    "glipizide": 0,
                                                    "glyburide": 1,
                                                    "pioglitazone": 0,
                                                    "rosiglitazone": 0
                                                }
                                )
    assert response.status_code == 200
    assert response.json()['readmitted'] != 0