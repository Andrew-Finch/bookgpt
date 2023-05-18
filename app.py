from flask import Flask, request, render_template, redirect, url_for
from bookgpt.services.promptsender import PromptSender
from bookgpt.services.uidatawrangler import ModelCreator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    search_value = request.args.get('search', '')

    return redirect((url_for('results', query=search_value)))  # or what you want

@app.route('/results', methods=['GET'])
def results():
    query = request.args.get('query', '')
    debug = False
    
    # Perform your search logic here to get the results
    prompter = PromptSender(query, debug)
    response = prompter.call_prompts()

    model = ModelCreator(
        response['query'],
        response['description'],
        response['meaning'],
        response['style'],
        response['quotes'])

    response_model = model.create_UI_view_model()
    print(response_model)

    return render_template('search_result.html', response=response_model)