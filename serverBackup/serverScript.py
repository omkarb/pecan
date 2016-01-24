
from flask import Flask, render_template, request, url_for
import pecan.main as builder

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():

    if request.method == 'POST':
        return redirect(url_for('search'))

    return render_template("pecan.html")


@app.route('/search', methods=['POST'])
def search():
    query = request.form['searchTerm']
    return "<h1>title</h1>" + builder.get_synopsis(builder.handle_query(query)['syn'])


if __name__ == "__main__":
    app.run()
