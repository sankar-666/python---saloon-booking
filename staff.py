from flask import *
from database import *
import uuid

staff=Blueprint('staff',__name__)

@staff.route('/staffhome')
def staffhome():
    return render_template('staffhome.html')