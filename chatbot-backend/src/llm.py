import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from src.store import Store
load_dotenv()
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

repo_id = "meta-llama/Meta-Llama-3-8B-Instruct"

class LLM:
    llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    max_length=128,
    temperature=0.5,
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
    )

    template = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>

    You are an expert at paraphrasing sentences so that they can be passed to a chatbot for aiding deaf and mute. Do not change meaning or move periods. Here is the sentence that you have to paraphrase {transcription}. 

    Assistant:<|eot_id|><|start_header_id|>user<|end_header_id|><|eot_id|><|start_header_id|>assistant<|end_header_id|>"""

    prompt = PromptTemplate.from_template(template)
    
    EXPRESSIVE_CHAIN = prompt | llm

    def gloss(self, transcription):
        
        response = LLM.EXPRESSIVE_CHAIN.invoke(
            {
                "transcription": transcription,
            }
        )

        return response
