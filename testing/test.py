from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os
import getpass
load_dotenv()

os.environ["GOOGLE_API_KEY"] = (str)(os.getenv("GOOGLE_API_KEY") )
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter Google API key: ")
llm = ChatGoogleGenerativeAI(model = "gemini-1.5-pro-002")
loader = CSVLoader(file_path = "flowers.csv", source_column = "prompt")
data = loader.load()
embed = GoogleGenerativeAIEmbeddings(model = "models/text-embedding-004")
vbase = FAISS.from_documents(documents = data, embedding = embed)
#vbase.save_local()
#print("Made vbase")
query = "what does a banana symbolize?"
retrieve = vbase.as_retriever()
ans = retrieve.invoke(query)
#print(ans)
prompt = PromptTemplate.from_template(
    """
    Use the given context to answser the question.
    If you don't know the answer, admit that you do not know.
    DO NOT MAKE INFORMATION UP. If the answer is not written in the given context, reply with the answer: "I don't know".
    Keep your answers concise and to the point; NO PREAMBLE
    Context: {context}
    """
) 
prompt.format(context = vbase)
qa = create_stuff_documents_chain(llm, prompt)
chain = create_retrieval_chain(retrieve, qa)
ans = chain.invoke({"input" : query})
prompt = PromptTemplate.from_template(
        """
        Given the following question and answer:
        {question}
        rephrase the question so that it is in the form of a statement. Be sure to include the answer somewhere in the sentence.
        Return a SINGLE sentence. NO PREAMBLE.
        """
) 
print(llm.invoke(prompt.format_prompt(question = ans)))
#print(ans)