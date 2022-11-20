import random
import json

options = {'race': ['Caucasian', 'AfricanAmerican', 'Other', 'Asian'],
 'gender': ['Male', 'Female'],
 'age': ['[60-70)',  '[70-80)',  '[40-50)',  '[10-20)',  '[50-60)',  '[80-90)',  '[30-40)',  '[20-30)',  '[90-100)',  '[0-10)'],
 'weight': ['[75-100)',  '[100-125)',  '[150-175)',  '[50-75)',  '[125-150)',  '[25-50)',  '[0-25)',  '[175-200)',  '>200'],
 'admission_type_id': [3, 1, 2, 6, 5, 4],
 'time_in_hospital': [3, 6, 7, 4, 5, 9, 2, 8, 12, 1, 11, 10, 13, 14],
 'num_lab_procedures': [35,  44,  40,  58,  60, 30,  71,  69,  49, 76,  79,  59,  28,  33,  64,  42,  73,  75, 78,  67, 55,  61,  1,  52,  54,  88,  57,  38,  50,  45, 4,  37,  74,  81,  32,  62,  72,  43,  70,  5,  80,  24,  68,  63,  27,
  3,  20,  82,  51,  13,  66,  16,  53,  56,  46,  48,  21,  36,  87,  77,  83,  93,  47,  11,  39,  86,  18,  41,  65,  14,  34,  31,  85,  89,  17,  12,  10,  29,  25,  8,  103,  2,  96,  15,  19,  26,  90,  84,  23,  91,  7,  92,  95,
  104,  22,  100,  94,  102],
 'num_procedures': [2, 0, 1, 5, 4, 3, 6],
 'num_medications': [20,  14,  18,  15,  43,  16,  13,  27,  10,  9,  22,  24,  7,  11,  8,  39,  17,  6,  12,  34,  2,  19,  21,  23,  49,  25,  5,  30,  26,  36,  29,  3,  28,  44,  41,  33,  46,  57,  32,  31,  40,  51,  48,  42,  45,  37,
  1,  35,  38,  52,  65,  58], 
  'number_outpatient': [1,  0,  5,  4,  3,  2, 10,  13,  9,  6,  11,  8,  7,  14,  12,  15,  16],
 'number_emergency': [0, 1, 5, 2, 3, 4, 10, 6, 11, 9],
 'number_inpatient': [0, 1, 2, 3, 4, 5, 12, 7, 6, 8, 18, 9, 21, 14],
 'number_diagnoses': [9, 5, 7, 8, 6, 1, 4, 3, 2],
 'max_glu_serum': ['None'],
 'A1Cresult': ['None', 'Norm', '>8', '>7'],
 'metformin': [0, 1],
 'glimepiride': [0, 1],
 'glipizide': [0, 1],
 'glyburide': [0, 1],
 'pioglitazone': [0, 1],
 'rosiglitazone': [0, 1]}

random_option = {}

for key, value in options.items():
    random_option [key] = value[random.randint(0,len(value)-1)]

with open("test_data_diabetes.json", "w") as outfile:
    json.dump(random_option, outfile, indent=4)