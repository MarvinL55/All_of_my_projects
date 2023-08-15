from flask import Flask, render_template
from Pets import Pet

app = Flask(__name__)

pets = []

@app.route('/')
def home():
    return render_template("VirtualPet.html")

@app.route("/add_pet/<string:name>/<string:pet_type>")
def add_pet(name, pet_type):
    pet = Pet(name, pet_type)
    pets.append(pet)
    return f"Add {pet_type} name {name}!"

@app.route("/feed/<int:pet_id>")
def feed(pet_id):
    if pet_id >= len(pets):
        return "Invalid pet ID"
    pet = pets[pet_id]
    pet.hunger -= 10
    pet.happiness += 5
    return f"{pet.name} has been fed!"

@app.route("/play/<int:pet_id>")
def play(pet_id):
    if pet_id >= len(pets):
        return "Invalid pet ID"
    pet = pets[pet_id]
    pet.hunger += 5
    pet.happiness += 15
    return f"{pet.name} had fun playing!"

if __name__ == "__main__":
    app.run(debug=True)
