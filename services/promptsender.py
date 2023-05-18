import openai
from bookgpt.services.promptsplicer import PromptSplicer
from bookgpt.model.dataclasses import APIkeys
import json
import logging

class PromptSender:
    def __init__(self, input, debug):
        self.input = input
        self.debug = debug
        self.prompt_splicer = PromptSplicer(input)
        self.api_key = APIkeys.openai

    def check_if_bookprompt(self):

        openai.api_key = self.api_key

        description_prompt = self.prompt_splicer.check_book_prompt()

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": description_prompt
                    }])

            raw_response = response["choices"][0]["message"]["content"].strip()

            processed_response = json.loads(raw_response)

            return processed_response
        
        except Exception:
            logging.exception('JSON Load conditions not met, sampling LLM again')
            print(raw_response)
            return self.check_if_bookprompt()


    def send_and_process_description_prompt(self):

        openai.api_key = self.api_key

        description_prompt = self.prompt_splicer.create_description_prompt()

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": description_prompt
                    }])

            raw_response = response["choices"][0]["message"]["content"].strip()

            processed_response = json.loads(raw_response)

            return processed_response
        except Exception:
            logging.exception('JSON Load conditions not met, sampling LLM again')
            return self.send_and_process_description_prompt()
    
    def send_and_process_meaning_prompt(self):

        openai.api_key = self.api_key

        description_prompt = self.prompt_splicer.create_meaning_prompt()

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": description_prompt
                }])

        return response["choices"][0]["message"]["content"].strip()
    
    def send_and_process_style_prompt(self):

        openai.api_key = self.api_key

        description_prompt = self.prompt_splicer.create_writing_style_prompt()

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": description_prompt
                }])

        return response["choices"][0]["message"]["content"].strip()
    
    def send_and_process_top_quotes_prompt(self):

        openai.api_key = self.api_key

        description_prompt = self.prompt_splicer.create_top_quotes_prompt()

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": description_prompt
                }])

        return response["choices"][0]["message"]["content"].strip()
    
    def call_prompts(self):

        if self.debug:
            response = {
                'query' : self.input,
                'description' : 'description description description',
                'meaning' : 'meaning meaning meaning',
                'style' : 'style style style',
                'quotes' : 'quotes quotes quotes'
            }

        else:
            response = {
                'query' : self.input,
                'description' : self.send_and_process_description_prompt(),
                'meaning' : self.send_and_process_meaning_prompt(),
                'style' : self.send_and_process_style_prompt(),
                'quotes' : 'quotes quotes quotes'
            }

            print(self.check_if_bookprompt())

        return response



