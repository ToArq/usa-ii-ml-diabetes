from pydantic import BaseModel

class PredictionRequest(BaseModel):
    race: str
    gender:  str
    age: str
    weight:  str
    admission_type_id: int
    time_in_hospital:  int
    num_lab_procedures:  int
    num_procedures:  int
    num_medications:  int
    number_outpatient:  int
    number_emergency:  int
    number_inpatient:  int
    number_diagnoses:  int
    max_glu_serum: str
    A1Cresult:  str
    metformin:  int
    glimepiride:  int
    glipizide:  int
    glyburide:  int
    pioglitazone:  int
    rosiglitazone: int

class PredictionResponse(BaseModel):
    readmitted: int
