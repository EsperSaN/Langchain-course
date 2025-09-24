from typing import List 
from pydantic import BaseModel, Field

class Source(BaseModel) : 
    url : str = Field(description="The URL of the source")
    opinion : str = Field(description="the opinion abouth this source rate it from 1 to 10")
class AgentResponse(BaseModel) :
    answer :  str = Field(description="The agent's answer to the query")
    source: List[Source] = Field(default_factory=list, description="List of source used to generate the answer")