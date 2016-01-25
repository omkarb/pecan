
from flask import Flask, render_template, request, url_for
from API import main as builder

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():

    if request.method == 'POST':
        return redirect(url_for('search'))

    return render_template("pecan.html")


@app.route('/search', methods=['POST'])
def search():
    query = request.form['searchTerm']
    dict = builder.handle_query(query)
    return (builder.get_synopsis(dict['syn']) + builder.get_tt(dict['tt']) + builder.get_wol(dict['wol']))


if __name__ == "__main__":
    app.run()
