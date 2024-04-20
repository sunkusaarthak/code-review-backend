import os
from dotenv import load_dotenv
from BledModel import BledModel 
import ModelSettings as MS

load_dotenv()

API_KEY = os.getenv('API_KEY')
CONFIGURE_INPUT = MS.ModelSettings.CONFIGURE_INPUT.value
current_input = r"""
    #include<stdio.h>
    #include<conio.h>

    void main() 
    {
        int x = 10;
        printf("%d", x);
    }
"""
bled_obj = BledModel(MS.ModelSettings.model_config, MS.ModelSettings.safety_settings, MS.ModelSettings.model_name)
final_input_to_bled_model = CONFIGURE_INPUT + current_input
bled_obj.parse_input(API_KEY, final_input_to_bled_model)