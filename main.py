from fastapi import FastAPI
from starlette.requests import Request #for request function
from starlette.responses import JSONResponse 
import pandas as pd 

df = pd.read_csv('./data/diagnoses2019.csv')

app = FastAPI()

@app.get('/')
def home():
    return 'this is a API service for MN ICD code details'

@app.get('/preview')
async def preview():
    top10rows = df.head(1)
    result = top10rows.to_json(orient="records")
    return result

@app.get('/icd/{value}') #flask uses <> Fastapi uses {} for placeholders
async def icdcode(value):
    print('value: ', value)
    filtered = df[df['principal_diagnosis_code'] == value]
    if len(filtered) <= 0:
        return 'There is nothing here'
    else: 
        return filtered.to_json(orient="records")

@app.get('/icd/{value}/payer/{value2}') #flask uses <> Fastapi uses {} for placeholders
async def icdcode2(value, value2):
    filtered = df[df['principal_diagnosis_code'] == value]
    filtered2 = filtered[filtered['payer'] == value2]
    if len(filtered2) <= 0:
        return 'There is nothing here'
    else: 
        return filtered2.to_json(orient="records")    
    #use MEDICARE for payer, R73 for value, icd and payer are lower case