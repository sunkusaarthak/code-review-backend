import google.generativeai as bert
from schemas import OutputModel
class BertModel:
    model_config = {}
    safety_settings = []
    model_name = ''
    def __init__(self, model_config, safety_settings, model_name):
        self.model_config = model_config.value
        self.safety_settings = safety_settings.value
        self.model_name = model_name.value

    def parse_input(self, api_key, final_input_to_bert_model) -> OutputModel:
        bert.configure(api_key=api_key)
        bert_model = bert.GenerativeModel(model_name=self.model_name,
                              generation_config=self.model_config,
                              safety_settings=self.safety_settings)
        convo = bert_model.start_chat(history=[])
        convo.send_message(final_input_to_bert_model)
        model_output = OutputModel(output=convo.last.text).model_dump()
        
        return model_output