from flask import Flask, render_template, url_for, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

# Configure the database URI and disable track modifications to improve performance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///adopt.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Connect the database and create all the tables
connect_db(app)
db.create_all()

# Enable Flask Debug Toolbar for easy debugging
toolbar = DebugToolbarExtension(app)

# Route to display a list of pets
@app.route("/")
def list_pets():
    pets = Pet.query.all()
    return render_template("petList.html", pets=pets)

# Route to add a new pet to the database
@app.route("/add", methods=["GET", "POST"])
def add_pet():
    form = AddPetForm()

    if form.validate_on_submit():
        # Extract form data and create a new Pet instance
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        
        # Add the new pet to the database and commit the changes
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        return redirect(url_for('list_pets'))
    else:
        return render_template("pet_add_form.html", form=form)

# Route to edit an existing pet's information
@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        # Update pet's information and commit the changes
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f'{pet.name} updated.')
        return redirect(url_for('list_pets'))
    else:
        return render_template("petEditForm.html", form=form, pet=pet)

# API route to retrieve pet information in JSON format
@app.route("/api/pets/<int:pet_id>", methods={'GET'})
def api_get_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    info = {"name": pet.name, "age": pet.age}
    return jsonify(info)
