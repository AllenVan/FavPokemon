from flask import Blueprint
from flask import render_template
from flask import request
from flaskr.db import get_db,get_img,dataClass

DATABASE = get_db()
your_list = dataClass()


bp = Blueprint('views', __name__)

@bp.route('/select', methods=['GET', 'POST'])
def show_index():
    if request.method == "POST":
        if len(your_list.selection) - 1 < 2:
            your_list.finals(request.form["Location"])
            return render_template('winner.html', 
                                    user_image = get_img(your_list.winner),
                                    name = DATABASE[str(your_list.winner)]["name"])  
        else:
            your_list.tourney(request.form["Location"])
            return render_template("select.html", 
                                    user_image1 = get_img(your_list.sample[0]), 
                                    user_image2 = get_img(your_list.sample[1]), 
                                    remaining = len(your_list.selection), 
                                    name1 = DATABASE[str(your_list.sample[0])]["name"], 
                                    name2 = DATABASE[str(your_list.sample[1])]["name"]) 

    else:
        your_list.reset()
        return render_template("select.html", 
                                user_image1 = get_img(your_list.sample[0]), 
                                user_image2 = get_img(your_list.sample[1]), 
                                remaining = len(your_list.selection), 
                                name1 = DATABASE[str(your_list.sample[0])]["name"], 
                                name2 = DATABASE[str(your_list.sample[1])]["name"]) 