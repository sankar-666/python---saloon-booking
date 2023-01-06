from flask import *
from database import *

customer=Blueprint('customer',__name__)


@customer.route("/customerhome")
def customerhome():
    data={}

    return render_template("customerhome.html",data=data)