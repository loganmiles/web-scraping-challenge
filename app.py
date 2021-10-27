import sys
from flask import Flask
from flask.templating import render_template
from werkzeug.utils import redirect
from flask_pymongo import PyMongo
import pymongo
import mars_scrape


app = Flask(__name__)

mongo = PyMongo(app, uri='mongodb://localhost27017/mars_data')


@app.route('/')
def index():
   mars_data = mongo.db.mars_data.find_one()
   return render_template("index.html", mars_data=mars_data)

@app.route('/scrape')
def scrape():
    mars_data = mongo.db.mars_data
    scraped = mars_scrape.scrape_info()
    mars_data.update({}, scraped, upsert = True)
    return redirect("/", code=302)

    
if __name__ == '__main__':
   app.run()