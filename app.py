from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('ProcessUserInfo/<string:username>', methods=['POST'])
def ProcessUserInfo:
    username = JSON.loads(username)
    return render_template('/')
    
@app.route('ProcessUserInfo/<string:password>', methods=['POST'])
def ProcessUserInfo:
    password = JSON.loads(password)
    return render_template('/')

if __name__ == '__main__':
    app.run()

    
