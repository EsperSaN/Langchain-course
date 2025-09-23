import os
from dotenv import load_dotenv
from langchain_google_genai import  ChatGoogleGenerativeAI


load_dotenv()

def main():

    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    result = llm.invoke("Sing a ballad of LangChain.")
    print(result.content)

if __name__ == "__main__":
    main()