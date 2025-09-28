from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import hub
from langchain_tavily import TavilySearch
from langchain.agents.react.agent import create_react_agent
from dotenv import load_dotenv
from langchain.agents import AgentExecutor
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

from prompt import REACT_PROMPT_WITH_FORMAT_INSTRUCTION
from schemax import Source, AgentResponse



load_dotenv()

tools_list = [TavilySearch()]
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
react_prompt = hub.pull("hwchase17/react") #import react prompt template
out_parser = PydanticOutputParser(pydantic_object=AgentResponse)
react_prompt_with_pydantic_format = PromptTemplate(
    template = REACT_PROMPT_WITH_FORMAT_INSTRUCTION,
    input_variables=["input", "agent_scartchpad", "tool_names"]
).partial(format_instructions=out_parser.get_format_instructions())

agent = create_react_agent(
    llm=llm ,
    tools = tools_list,
    prompt = react_prompt_with_pydantic_format
)

agent_exe = AgentExecutor(agent=agent, tools=tools_list,verbose=True, handle_parsing_errors=True) # to fix the Parser Error using the handle_parsing_error
extrace_the_output = RunnableLambda(lambda x : x["output"])
prase_out_put_json = RunnableLambda(lambda x : out_parser.parse(x))

agent = agent_exe | extrace_the_output | prase_out_put_json
# pipe the output obj | select the "output" | convert toJson

def main():
    result= agent.invoke(input={
        "input":"find me the langchain job on linkin",
    })
    print("Raw result:", result.answer , result.source[1])
if __name__ == "__main__" :
    main()