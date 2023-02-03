from flask import Blueprint
import os, json
import random
import sys
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flaskr.db import get_db,get_rand_img,get_img,dataClass

DATABASE = get_db()
your_list = dataClass()


bp = Blueprint('views', __name__)

@bp.route('/test')
def home():
    return render_template("test.html", name = DATABASE[str(random.randint(1,151))]["name"])


@bp.route('/index', methods=['GET', 'POST'])
def show_index():
    if request.method == "POST":
        if len(your_list.selection) - 1 < 2:
            your_list.finals(request.form["Location"])
            return render_template('winner.html', 
                                    user_image = get_img(your_list.winner),
                                    name = DATABASE[str(your_list.winner)]["name"])  
        else:
            your_list.tourney(request.form["Location"])
            return render_template("index.html", 
                                    user_image1 = get_img(your_list.sample[0]), 
                                    user_image2 = get_img(your_list.sample[1]), 
                                    remaining = len(your_list.selection), 
                                    name1 = DATABASE[str(your_list.sample[0])]["name"], 
                                    name2 = DATABASE[str(your_list.sample[1])]["name"]) 

    else:
        return render_template("index.html", 
                                user_image1 = get_img(your_list.sample[0]), 
                                user_image2 = get_img(your_list.sample[1]), 
                                remaining = len(your_list.selection), 
                                name1 = DATABASE[str(your_list.sample[0])]["name"], 
                                name2 = DATABASE[str(your_list.sample[1])]["name"]) 

@bp.route('/chosen', methods=['GET', 'POST'])
def show_chosen():
    if request.method == "POST":
        if request.form["location"] == "Delete Front":
            your_list.selection.pop(0)
            return render_template('test.html', your_list=your_list.selection)
        elif request.form["location"] == "Delete Back":
            your_list.selection.pop()
            return render_template('test.html', your_list=your_list.selection)
        else:
            return render_template('test.html', your_list=your_list.reset())

     
    else:
        return render_template('test.html', your_list=your_list.reset())