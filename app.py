
import sys
from flask import Flask, render_template, jsonify, redirect
import pymongo
import mission_to_mars

sys.setrecursionlimit(2000)
app = Flask(__name__)


client = pymongo.MongoClient()
db = client.mars_db
collection = db.mars_data



@app.route("/scrape")
def scrape():
    
   # db.collection.remove()
    mars = mission_to_mars.scrape()
    print("\n\n\n")
    db.mars_data.insert_one(mars)
    mars = list(db.mars_data.find())
    return render_template("index.html", mars = mars)
    # return "Complete Scraping Mars Data!"

@app.route("/")
def home():
    mars = list(db.mars_data.find())
    print(mars)
    return render_template("index.html", mars = mars)


if __name__ == "__main__":
    app.run(debug=True)


