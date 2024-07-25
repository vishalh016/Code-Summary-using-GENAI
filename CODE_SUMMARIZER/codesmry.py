import os
from dotenv import load_dotenv
import openai
from langchain_community.llms import OpenAI

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

print(API_KEY)

def summarize_code_file(file_path):
  """Summarizes a single code file using OpenAI."""
  with open(file_path, 'r') as f:
    code_content = f.read()

  # Use OpenAI to generate a summary
  openai.api_key = API_KEY
    
  #llm = OpenAI(temperature=0.7)
  #summary = llm.generate(f"Summarize the following code:\n{code_content}")
  
#   openai.api_key = "YOUR_OPENAI_API_KEY"
  llm = OpenAI(temperature=0.7)
  summary = llm.generate(f"Summarize the following code:\n{code_content}")

  return summary.text

def summarize_code_folder(folder_path):
  """Summarizes all code files in a given folder."""
  all_summaries = []
  for root, _, files in os.walk(folder_path):
    for file in files:
      if file.endswith(".py"):  # Adjust for other file types if needed
        file_path = os.path.join(root, file)
        summary = summarize_code_file(file_path)
        all_summaries.append(summary)

  # Combine summaries into a comprehensive overview
  combined_summary = "\n".join(all_summaries)

  return combined_summary

def write_summary_to_file(summary, output_file):
  """Writes the summary to a text file."""
  with open(output_file, 'w') as f:
    f.write(summary)

if __name__ == "__main__":
  folder_path = "D:\AI Project\CODE_SUMMARIZER"
  output_file = "code_summary.txt"

  summary = summarize_code_folder(folder_path)
  write_summary_to_file(summary, output_file)
