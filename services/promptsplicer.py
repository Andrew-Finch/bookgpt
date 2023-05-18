import logging

class PromptSplicer:
    def __init__(self, input):
        self.input = input

    # Configure logging to display INFO level messages and above
    logging.basicConfig(level=logging.INFO)

    #functions for adding prompts
    
    def check_book_prompt(self):

        dict_format = '''
        {
            "book": percentage chance of being a book as a float,
            "movie": percentage chance of being a movie as a float,
            "series": percentage chance of being a series as a float
        }\
            '''
        
        prompt =  '''Give me a percentage chance that the input {input} is the title of a book, movie or TV series. Output a python dictionary in the format as follows:

        {dict_format}\
        
        Do not output any other text other than the dictionary
        '''.format(input=self.input, dict_format=dict_format)
        
        logging.info("PROMPT: %s", prompt)

        return prompt
    

    def create_description_prompt(self):
        dict_format = '''
        {
            "author": "author value",
            "authors nationality": "nationality value",
            "date of completion": "date of completion value",
            "genre": "genre value"
        }\
            '''
        
        prompt =  '''Tell me the author, authors nationality, date of completion, and genre of the book {input}. Present it as a python dictionary with the author, authors nationality, date of completion, and genre of the book as keys and answers as values. Only output the raw python object in the format of:
        {dict_format}\
        '''.format(input=self.input, dict_format=dict_format)

        logging.info("PROMPT: %s", prompt)

        return prompt
    
    def create_meaning_prompt(self):

        prompt = f"Write a paragraph summarising the key themes of the book {self.input}"
        logging.info("PROMPT: %s", prompt)

        return prompt
    
    def create_writing_style_prompt(self):

        prompt = f"Write a paragraph summarising the writing style of the book {self.input}"
        logging.info("PROMPT: %s", prompt)

        return prompt
    
    def create_top_quotes_prompt(self):

        prompt = f"Provide a list of 5 famous quotes from the book {self.input}"
        logging.info("PROMPT: %s", prompt)

        return prompt

