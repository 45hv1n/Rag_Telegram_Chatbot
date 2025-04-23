from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA

def set_custom_prompt(prompt_template):
  prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
  return prompt


def get_qa_chain(model, vector_data, custom_prompt_template):
    
    print("@@@@@@#@@ creating QA CHain, ", custom_prompt_template)
    reteriver = vector_data.as_retriever(search_type = "similarity", search_kwargs = {"k": 3})
    qaChain = RetrievalQA.from_chain_type(
        llm = model,
        chain_type = "stuff",
        retriever = reteriver,
        chain_type_kwargs = {"prompt": set_custom_prompt(custom_prompt_template)},
    )
    return qaChain