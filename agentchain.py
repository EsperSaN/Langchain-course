from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import hub
from langchain_tavily import TavilySearch
from langchain.agents.react.agent import create_react_agent
from dotenv import load_dotenv
from langchain.agents import AgentExecutor

load_dotenv()

tools_list = [TavilySearch()]
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
react_prompt = hub.pull("hwchase17/react") #import react prompt template
agent = create_react_agent(
    llm=llm ,
    tools = tools_list,
    prompt = react_prompt
)
agent_exe = AgentExecutor(agent=agent, tools=tools_list,verbose=True, handle_parsing_errors=True) # to fix the Parser Error using the handle_parsing_error


def main():
    result= agent_exe.invoke(input={
        "input":"find me the langchain job on linkin",
    })
    print("Raw result:", result)
if __name__ == "__main__" :
    main()