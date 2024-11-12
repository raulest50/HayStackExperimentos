
from haystack import component, Pipeline

@component
class WelcomeTextGenerator:
    """
    component generating personal welcome message and making it upper case
    """

    @component.output_types(welcome_text= str, note=str)
    def run(self, name: str):
        return {"welcome_text" : ('Hello {name}, welcome to Haystack.'.format(name=name)).upper(),
                "note": "Welcome message is ready"}


@component
class WhiteSpaceSplitter:
    """
    component generating personal welcome message and making it upper case
    """

    @component.output_types(splitted_text=List[str])
    def run(self, text: str):
        return {"splitted_text": text.split()}




text_pipeline = Pipeline()
text_pipeline.add_component(name="welcome_text_generator", instance=WelcomeTextGenerator)
text_pipeline.add_component(name="white_space_splitter", instance=WhiteSpaceSplitter)
text_pipeline.connect()



