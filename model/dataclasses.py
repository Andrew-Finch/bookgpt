
from dataclasses import dataclass
 
@dataclass
class Quote:
    author: str
    description: str

@dataclass
class Description:
    author: str
    nationality: str
    date_of_completion: str
    genre: str

@dataclass
class Response:
    query: str
    description: Description
    meaning: str
    style:str
    quotes: list[Quote]