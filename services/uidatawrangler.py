from bookgpt.model.dataclasses import Response, Description

class ModelCreator:
    def __init__(self, query, description, meaning, style, quotes):
        self.query = query
        self.description = description
        self.meaning = meaning
        self.style = style
        self.quotes = quotes

    def create_UI_view_model(self):

        desc = Description(
            author=self.description['author'],
            nationality=self.description['authors nationality'],
            date_of_completion=self.description['date of completion'],
            genre=self.description['genre']
        )

        response = Response(
            query=self.query,
            description=desc,
            meaning=self.meaning,
            style=self.style,
            quotes=[]
        )

        return response