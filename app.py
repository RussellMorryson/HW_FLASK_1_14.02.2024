from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/main/')
def main_sheet():
    return render_template('main.html')

@app.route('/outerwear/')
def outewear_sheet():
    return render_template('outerwear.html')

@app.route('/clothes/')
def clothes_sheet():
    return render_template('clothes.html')

@app.route('/shoes/')
def shoes_sheet():
    return render_template('shoes.html')

if __name__ == '__main__':
    app.run()