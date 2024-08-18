import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o")

def summarize_text(text):
    """Summarizes the given text using the OpenAI API."""

    # openai.api_key = os.getenv("OPENAI_API_KEY")
    template = """You are a code summarizer assistant.
    Human: Explain me the following code,{code} ,also show me what to expect as output.
    Assistant:"""
    prompt_template = ChatPromptTemplate.from_template(template)
    prompt = prompt_template.invoke({"code": text})

    
    result = model.invoke(prompt)
    print(result.content)


    # return response.choices[0].text.strip()

def summarize_file(file_path):
  """Reads the content of a text file and summarizes it."""

  with open(file_path, 'r') as f:
    text = f.read()

  summary = summarize_text(text)
  return summary

# if __name__ == "__main__":
file_path = "abc.txt"  # Replace with your file path
summary = summarize_file(file_path)
print(summary)
