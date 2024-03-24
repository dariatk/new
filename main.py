from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return 'Hello, World'

app.run(host='o.o.o.o', port = 8000)
