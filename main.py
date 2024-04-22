import os
import ModelSettings as MS
from dotenv import load_dotenv
from BledModel import BledModel
from fastapi import FastAPI
from schemas import CodeModel, OutputModel
from ptree.utils import load_config
from ptree.utils import return_string_from_tokens
from ptree.parser.grammar import Grammar
from ptree.lexer.lexer import Lexer
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

@app.post('/getcodetokenized')
async def get_code_tokenized(code: CodeModel) -> OutputModel:
    config = load_config('configs/test-lexer-test-cpp.yaml')
    grammar = Grammar(config)
    lexer = Lexer(config, symbol_pool=grammar.symbol_pool)
    tokens = lexer.tokenize(code.code)
    model_output = OutputModel(output=return_string_from_tokens(tokens)).model_dump()

    return model_output