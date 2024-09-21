from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
@app.route('/Home')
def home_page():
    return render_template('home.html')


@app.route('/op')
def hello_world():
    return '<h1> hello world  biggger</h1><h2> nice to have u guys</h2>'
@app.route('/Login')
def Login():
    return '<h1>tHIS IS THE LOGIN page you want </h1><div></div><p>hello you wnat to login to this particular page</p>'
@app.route('/Register')
def Register():
    return '<h1>So you not register yet</h1><div></div><p>If you want to register just click on register</p>'
@app.route('/Market')
def market_page():
     items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150},
        {'id': 4, 'name': 'mouse', 'barcode': '231985148446', 'price': 125}
    ]
     return render_template('market.html', items=items)
@app.route('/Sell')
def Sell():
    return '<h1> you want to sell something on this page</h1>'



@app.route('/about/<username>')

def about_page(username):
    return f'<h1>this is the about page {username}</h1>'

@app.route('/usr/<name1>')

def usr(name1):
    return f'<p>hello there this will be the user page welcome here {name1} </p>'


if __name__ == "__main__":
    app.run(debug=True)