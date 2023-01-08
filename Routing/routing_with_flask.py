from flask import Flask

app=Flask(__name__)

# defining functions that correspond to a certain route
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/my_name')
def print_my_name():
    return 'My name is : Salomon'

if(__name__=='__main__'):
    app.run()