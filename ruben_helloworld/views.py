from ruben_helloworld import app

@app.route('/')
def index():
    return 'Ruben Anderson Louis'
