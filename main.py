from fastapi import FastAPI 

app = FastAPI()

@app.get('/')


def index():
    return {'data': { 'message': 'Hello Nishant'}}


@app.get('/about')

def about():
    return {'data': { 'message': 'About Nishant'}}