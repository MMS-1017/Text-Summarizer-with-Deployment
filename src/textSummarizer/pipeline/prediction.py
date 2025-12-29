from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()


    
    def predict(self,text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {
            "length_penalty": 0.8,  # Penalizes long outputs (<1 = shorter summaries)
            "num_beams":8,          # Beam search width (quality ↑, speed ↓)
            "max_length": 128       # Maximum summary length
            }
        pipe = pipeline("summarization", model = self.config.model_path,tokenizer = tokenizer)

        print("Dialogue:")
        print(text)

        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)

        return output