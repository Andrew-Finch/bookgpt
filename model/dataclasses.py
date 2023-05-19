
from dataclasses import dataclass
import os


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
class Recommendation:
    author: str
    book: str

@dataclass
class Response:
    query: str
    description: Description
    meaning: str
    style:str
    recommendations : list[Recommendation]
    quotes: list[Quote]

@dataclass(frozen=True)
class APIkeys:
    openai: str = os.environ.get('openai_api_key')