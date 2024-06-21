import os

from langchain_community.llms import HuggingFaceEndpoint
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()



# setting the Api
model_Api = os.getenv("HUGGINGFACEHUB_API_TOKEN")
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = model_Api

repo_id =  "mistralai/Mistral-7B-Instruct-v0.3"

def QueryBuilding():

    Query_template = """Consider yourself as a personalized professional medical assistant  for the user {query},
                    
                    Answer: provide guidance and support to  the user in a more detailed, simple and straightforward manner. """
    return Query_template

def PromptEngineering():
    Prompt  = PromptTemplate.from_template(QueryBuilding())
    return Prompt



def LLM_building():
    llm_model = HuggingFaceEndpoint(
    repo_id=repo_id,
        max_length =  128,  # Set the maximum input length
        token =  model_Api # Set the API token
    
    )
    return llm_model

def langchainning():
    llm_chain = LLMChain(prompt=PromptEngineering(), llm=LLM_building())
    return llm_chain

# def user_input(user):
#     # user = input()
#     ans = langchainning().run(user)
#     return ans


