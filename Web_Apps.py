from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("home.html", name="Marvin", age="17")

@views.route("/json")
def get_json():
    return jsonify({"name": "Marvin", "coding": 5})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.get_json"))