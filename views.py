from flask import Blueprint, render_template, request, jsonify, redirect, url_for
views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html", name="Marquita", money='2 Million')

@views.route("/profile")
def profile():
    return render_template("profile.html")

@views.route("/json")
def get_json():
    return jsonify({'name': 'marquita', 'kids':'2'})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("go-to-home")
def go_to_home():
    return  redirect(url_for("views.home"))