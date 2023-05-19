from bookgpt.model.dataclasses import Response, Description, Recommendation

class ModelCreator:
    def __init__(self, query, description, meaning, style, recommendations, quotes):
        self.query = query
        self.description = description
        self.meaning = meaning
        self.style = style
        self.recommendations = recommendations
        self.quotes = quotes

    def create_UI_view_model(self):

        desc = Description(
            author=self.description['author'],
            nationality=self.description['authors nationality'],
            date_of_completion=self.description['date of completion'],
            genre=self.description['genre']
        )

        recs = [Recommendation(author=rec, book=self.recommendations[rec]) for rec in self.recommendations]

        print(recs)

        response = Response(
            query=self.query,
            description=desc,
            meaning=self.meaning,
            style=self.style,
            recommendations=recs,
            quotes=[]
        )

        return response