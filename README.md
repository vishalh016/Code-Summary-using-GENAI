# Code Summarizer
This repository contains a Python-based code summarizer project that leverages the OpenAI API and langchain library to automatically generate natural language summaries for Python scripts. The summarizer not only explains the functionality of the code but also provides an overview of the expected output.<BR

## Features
Text-to-Code Summary: Automatically generate a concise and clear summary of any Python script.
Output Prediction: Provides insights into what outputs can be expected from the code.
Customizable Prompts: Easily adjust the summarization template to fit specific needs or focus areas.

## Installation
###Clone the repository:
  git clone https://github.com/vishalh016/Code-Summary-using-GENAI.git
  cd code-summarizer

###Create and activate a virtual environment (optional but recommended):
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`

###Install the required dependencies:
  pip install -r requirements.txt

###Set up your environment variables:
  Create a .env file in the root directory.
###Add your OpenAI API key:
  OPENAI_API_KEY=your-openai-api-key

## Usage
###Summarize a Python Script
  Place your Python script in the same directory as the summarizer.py file or specify the path to your script.

###Run the summarizer:
  python summarizer.py
  
###Follow the prompts:
  Enter the path to the Python script you want to summarize.
  Specify the output file name where the summary will be saved.
###View the Summary:
  The summary, along with explanations and expected outputs, will be printed to the console and saved in the specified output file.

Example
  Enter the path to the Python script: example_script.py
  Enter the output file name: summary.txt
The script will then process example_script.py and save the summary in summary.txt.

## Customization
You can customize the prompt template used for summarization by editing the template variable in the summarizer.py file. This allows you to tweak how the summarizer interprets and generates summaries for different types of code.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an issue for any bugs, feature requests, or suggestions.

Fork the repository.
  Create your feature branch (git checkout -b feature/your-feature).
  Commit your changes (git commit -m 'Add some feature').
  Push to the branch (git push origin feature/your-feature).
  Open a Pull Request.

## Contact
For any questions or inquiries, please contact me at vishalh016@gmail.com.

