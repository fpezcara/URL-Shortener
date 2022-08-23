from flask import Blueprint, request, render_template, redirect
from ..database.db import db
from ..models.url import Url
import pyshorteners

main_routes = Blueprint("main", __name__)

@main_routes.route("/", methods=["GET", "POST"])
def index():
   
    if request.method == "GET":

        return render_template("index.html")
    else:
        url = request.form['url']  
        s=pyshorteners.Shortener()
        shorter=s.tinyurl.short(url)
        # db.session.add()
        shortened_url = Url(original_url=url, shortened_url=shorter)
        db.session.add(shortened_url)
        db.session.commit()
        print('***********************')
        urls = Url.query.all()
     
        return render_template("index.html", shorter=shorter)

        # else:
        #     return render_template("index.html")
   
@main_routes.route("/<string:url>")
def lookup(url):
    found_original_url = Url.query.filter_by(original_url=url).first()
    found_shortened_url = Url.query.filter_by(shortened_url=url).first()
    print('*******************', str(url))
    print('###########', url)

    if found_original_url.original_url != None:
        return redirect('https://'+found_original_url.original_url)
    # if found_shortened_url.shortened_url != None:
    #     print("you are in the elif - line 39")
    #     return redirect(found_shortened_url.shortened_url)
        # if 'https:' in found_url.original_url:
        #     print("somethingggggggg")
        #     return redirect(found_url.original_url)
        # else:
        #     print("im workiiiiiingggg")
        #     # return redirect(f'https//:{found_url.original_url}')
        #     return redirect(f'https//:{found_url.original_url}')

    
    # return redirect('/')
    # return redirect("/")
    # if found_url == None:
    #     return redirect("/404")
    # else:
    #     print("do i even exist?", url.original_url)
    #     return redirect(url.original_url)
    #     # db.session.add(new_listing)
    #     # db.session.commit()

    #     # urls = Url.query.all()