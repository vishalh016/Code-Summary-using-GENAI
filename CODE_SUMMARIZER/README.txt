## TO CREATE VIRTUAL ENV ##
---------------------------
pip install virtualenv

CREATE ENV
virtualenv smryvenv

ACTIVATE ENV
.\smryvenv\Scripts\activate


----------------------------------------------
## STEPS TO EXECUTE 'GENAI CODE EXPLAINER': ##
----------------------------------------------
RUN refactor_code.py to get the code and their corresponding dependencies in a txt file
RUN AI_handler.py to send the text output of refactor_code for summarization
