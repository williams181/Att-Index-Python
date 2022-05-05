from flask import Flask, render_template

# Declare a flask app
app = Flask(__name__, template_folder='./templates', static_folder='./static')

@app.route('/')
def index():

    return render_template('index.html')

if __name__ == '__main__':

    print('='*50)
    print('Running...')
    print('='*50)

    app.run(host='0.0.0.0', port=4000, debug=True)
