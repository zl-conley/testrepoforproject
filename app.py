from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__, static_folder='static')

# MongoDB Configuration
# app.config["MONGO_URI"] = "mongodb://localhost:27017/pet_adoption"
# mongo = PyMongo(app)

client = MongoClient('mongodb://localhost:27017/')  
db = client['pet_adoption']  
 

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/about")
def aboutus():
    return render_template("aboutus.html")

@app.route("/adopt")
def adopt():
    return render_template("adopt.html")

@app.route("/adoptionprocess")
def adoptionprocess():
    return render_template("adoptionprocess.html")

@app.route("/animalinfo/<id>")
def animal_info(id):
    pet = db.Pets.find_one({"_id": ObjectId(id)}) 
    print(pet) 
    return render_template('animalinfo.html', pet=pet)


@app.route("/cat")
def cat():
    pets = db.Pets.find({'Species': 'Cat'})
    return render_template("cat.html",pets=pets)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        phone = request.form.get('phone')
        email = request.form.get('email')
        query = request.form.get('query')
        db.ContactInfo.insert_one({"Contact": phone, "Email": email, "query": query})
        return redirect(url_for('contact'))
    return render_template("contactus.html",contact=contact)

# @app.route("/dog")
# def dog():
#     pets = db.Pets.find({'Species': 'Dog'})
#     return render_template("dog.html",pets=pets)

@app.route("/dog1")
def dog1():
    pets = db.Pets.find({'Species': 'Dog'})
    return render_template("dog.html",pets=pets)

@app.route("/donation")
def donation():
    return render_template("donation.html")



if __name__ == "__main__":
    app.run(debug=True)
