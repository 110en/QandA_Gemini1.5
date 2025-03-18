Good Day ^-^

All you need is the app folder, everything else is unnecessary for this program to work. Make sure that you have a valid Google api key
and have a .env file that contains your key. Should look like GOOGLE_API_KEY = "<your key>"

The user will ask a question regarding flowers. If the question is irrelevant to flowers or the question is asking about a flower or topic
the vector database doesn't contain information about, the llm will simply respond along the lines of "I don't know". Otherwise, it will
give an answer. 
Note: The temperature is set to a very low level so that the llm doesn't stray to far away from the facts.
You can change this in QandA.py
Warning: the .csv file in which the vector database used is NOT factually checked and all the information was produced by a genAI. Please
do not utilize this program as a way to learn about flowers as the database is very limited and may contain incorrect data.

For the program to work, in the command prompt type: streamlit run <path to main.py>. If for whatever reason command prompt doesn't
allow streamlit commands, use: python -m streamlit run <path to main.py>.

Packages used in this program (not necessarily exhaustive):
- streamlit
- langchain
    - _community
    - _google_genai
    - _core
- protobuf
- faiss-cpu
- tiktoken
- python-dotenv