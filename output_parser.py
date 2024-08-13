from typing import List, Dict, Any

from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field


class Summary(BaseModel):
    summary: str = Field(description="summary")
    facts: List[str] = Field(description="interesting facts about them")
    convo_starter: str = Field(description="icebreaker to start a conversation with them")

    def to_dict(self) -> Dict[str, Any]:
        return {"summary": self.summary, "facts": self.facts, "convo_starter": self.convo_starter}


summary_parser = PydanticOutputParser(pydantic_object=Summary)