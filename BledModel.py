import google.generativeai as bled
from schemas import OutputModel
class BledModel:
    model_config = {}
    safety_settings = []
    model_name = ''
    def __init__(self, model_config, safety_settings, model_name):
        self.model_config = model_config.value
        self.safety_settings = safety_settings.value
        self.model_name = model_name.value

    def parse_input(self, api_key, final_input_to_bled_model) -> OutputModel:
        bled.configure(api_key=api_key)
        bled_model = bled.GenerativeModel(model_name=self.model_name,
                              generation_config=self.model_config,
                              safety_settings=self.safety_settings)
        convo = bled_model.start_chat(history=[])
        convo.send_message(final_input_to_bled_model)
        model_output = OutputModel(output=convo.last.text).model_dump()
        return model_output