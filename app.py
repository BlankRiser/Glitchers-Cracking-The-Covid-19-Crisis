from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
import requests
import folium

app = Flask(__name__)


@app.route('/home')
@app.route('/index')
@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/')
def homePage():
    return render_template('index.html')


@app.route('/<errors>')
def errorPage(errors):
    # return (errors + ' not found')
    return render_template('404.html', errors=errors)

# Displaying map in a new window
# @app.route('/map')
# def index():
#     start_coords = (46.9540700, 142.7360300)
#     folium_map = folium.Map(location=start_coords, zoom_start=14)
#     return folium_map._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)
