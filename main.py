from time import time
import pandas as pd
from fastapi import FastAPI, __version__

df = pd.read_csv('./data/diagnoses2019.csv')

app = FastAPI() # This is what will be refrenced in config

@app.get('/')
async def hello():
    return {'res': 'pong', 'version': __version__, "time": time()}

@app.get('/preview')
async def preview():
    top10rows = df.head(1)
    result = top10rows.to_json(orient="records")
    return result

@app.get('/icd/<value>')
def icdcode(value):
    print('value: ', value)
    filtered = df[df['principal_diagnosis_code'] == value]
    if len(filtered) <= 0:
        return 'There is nothing here'
    else: 
        return filtered.to_json(orient="records")

@app.get('/icd/<value>/sex/<value2>')
def icdcode2(value, value2):
    filtered = df[df['principal_diagnosis_code'] == value]
    filtered2 = filtered[filtered['sex'] == value2]
    if len(filtered2) <= 0:
        return 'There is nothing here'
    else: 
        return filtered2.to_json(orient="records")


