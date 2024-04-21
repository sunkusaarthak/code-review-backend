import os
import ModelSettings as MS
from dotenv import load_dotenv
from BledModel import BledModel
from fastapi import FastAPI
from schemas import CodeModel, OutputModel

load_dotenv()

API_KEY = os.getenv('API_KEY')
CONFIGURE_INPUT = MS.ModelSettings.CONFIGURE_INPUT.value
app = FastAPI()

@app.get('/')
async def root():
    return {'test':'Hello', 'data':0}

@app.post('/getcodereview')
async def get_code_review(code: CodeModel) -> OutputModel:
    bled_obj = BledModel(MS.ModelSettings.model_config, MS.ModelSettings.safety_settings, MS.ModelSettings.model_name)
    final_input_to_bled_model = CONFIGURE_INPUT + code.code
    return bled_obj.parse_input(API_KEY, final_input_to_bled_model)