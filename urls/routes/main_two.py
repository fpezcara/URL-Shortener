from flask import Blueprint, request, render_template
from ..database.db import db
from ..models.url import Url
import pyshorteners

main_routes = Blueprint("main", __name__)

@main_routes.route("/", methods=["GET", "POST"])
def index():
    try:    
        if request.method == "GET":
            print("some printttt")
            return render_template("index.html")
        else:
            url = request.args['url']    
            s=pyshorteners.Shortener()
            shorter=s.tinyurl.short(url)
            print('**************************')
            print(shorter)
            print('**************************')
            return 'ELLIOT'
        # else:
        #     return render_template("index.html")
    except(Exception):
        print("Watch out for error", Exception)
        return "Oh no!"

@main_routes.route("/shorten-url", methods=["GET", "POST"])
# urls = Url.query.all()
def shorten_url():
    if request.method == "POST":
        url = request.args['url']    
        s=pyshorteners.Shortener()
        shorter=s.tinyurl.short(url)
        print('**************************')
        print(shorter)
        print('**************************')
        # print(f'SHORTER: {shorter}')
        # print('**************************')

    #     print(request.args["url"])
    #     url = request.form["url"]
    #     print(url)
    #     # body = request.form["body"]
    #     # email = request.form["email"]
        
    #     # new_listing = Url(title=title, body=body, email=email)
    #     # db.session.add(new_listing)
    #     # db.session.commit()

    #     # urls = Url.query.all()
