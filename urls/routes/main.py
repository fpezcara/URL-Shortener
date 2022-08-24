from flask import Blueprint, request, render_template, redirect
from ..database.db import db
from ..models.urls import Url
import pyshorteners

main_routes = Blueprint("main", __name__)

@main_routes.route("/", methods=["GET", "POST"])
def index():
    try:   
        if request.method == "GET": 
            return render_template("index.html")
        else:
            url = request.form['url']  
            s=pyshorteners.Shortener()
            shorter=s.tinyurl.short(url)
            our_url = shorter[20:]
            shortened_url = Url(original_url=url, app_url=our_url)
            db.session.add(shortened_url)
            db.session.commit()
            url_to_show_user = f'https://resize-it.herokuapp.com/{our_url}'
            return render_template("index.html", shorter=url_to_show_user)
    except:
        return "Ooooooops, there's been an error!!"
   
@main_routes.route("/<string:url>", methods=['GET'])
def lookup(url):
    try:    
        get_url = Url.query.filter_by(app_url=url).first()
        if not 'https://' in get_url.original_url:
            return redirect(f'https://{get_url.original_url}')
        else:
            return redirect(get_url.original_url)
    except:
        return redirect('/')
