from flask import Flask,render_template
from public import public
from admin import admin
from staff import staff
from customer import customer


app=Flask(__name__)

app.secret_key="prayulla"

app.register_blueprint(admin,url_prefix="/admin")
app.register_blueprint(staff,url_prefix="/staff")
app.register_blueprint(customer,url_prefix="/customer")
app.register_blueprint(public)
@app.errorhandler(404)
def not_found(e):
  return render_template("404.html")



app.run(debug=True,port=5007)