import requests
from flask import Flask


app = Flask(__name__)

"""
Gets information on LOR books from web and returns JSON
"""
@app.route("/book")
def get_book():
    response = requests.get("https://the-one-api.dev/v2/book")
    return response.json()


"""
Gets information on LOR characters from web and returns JSON
"""
@app.route("/characters")
def get_characters():
    headers = {"Authorization": "Bearer 8yD-obZ2fy40joMyA-nh"}
    response = requests.get("https://the-one-api.dev/v2/character", headers = headers)
    return response.json()


"""
Gets information on LOR quotes from web and returns JSON
"""
@app.route("/quote")
def get_quote():
    headers = {"Authorization": "Bearer 8yD-obZ2fy40joMyA-nh"}
    response = requests.get("https://the-one-api.dev/v2/quote", headers = headers)
    return response.json()


"""
Returns error message if no path given
"""
@app.route("/")
def no_path():
    return "no path given"


# run app on local server
if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)