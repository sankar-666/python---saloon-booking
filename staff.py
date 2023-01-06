from flask import *
from database import *
import uuid

staff=Blueprint('staff',__name__)

@staff.route('/staffhome')
def staffhome():
    return render_template('staffhome.html')



@staff.route('/staffmanagecategory',methods=['get','post'])
def staffmanagecategory():
    data={}
    if 'submit' in request.form:
        name=request.form['name']
        desc=request.form['desc']
    
        q="insert into category values (null,'%s','%s','active')"%(name,desc)
        insert(q)
        return redirect(url_for("staff.staffmanagecategory"))

    data={}
    q="select * from category"
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        cat_id=request.args['cat_id']

      
    else:
        action=None

    if action == "active":
        q="update category set category_status='active' where category_id='%s' "%(cat_id)
        update(q) 
        return redirect(url_for("staff.staffmanagecategory"))
    if action == "inactive":
        q="update category set category_status='inactive' where category_id='%s' "%(cat_id)
        update(q)
        return redirect(url_for("staff.staffmanagecategory"))

    if action == "update":
        q="select * from category where category_id='%s'"%(cat_id)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            name=request.form['name']
            desc=request.form['desc']

            q="update category set category_name='%s', category_desc='%s' where category_id='%s' "%(name,desc,cat_id)
            update(q)
            return redirect(url_for("staff.staffmanagecategory"))
    return render_template('staffmanagecategory.html',data=data) 



@staff.route('/staffmanagesubcategory',methods=['get','post'])
def staffmanagesubcategory():
    data={}

    q="select * from category where category_status='active' "
    data['cat']=select(q)
    if 'submit' in request.form:
        catid=request.form['catid']
        name=request.form['name']
        desc=request.form['desc']
    
        q="insert into subcategory values (null,'%s','%s','%s','inactive')"%(catid,name,desc)
        insert(q)
        return redirect(url_for("staff.staffmanagesubcategory"))


    q="select * from subcategory"
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        subid=request.args['subid']

      
    else:
        action=None

    if action == "active":
        q="update subcategory set subcategory_status='active' where subcategory_id='%s' "%(subid)
        update(q) 
        return redirect(url_for("staff.staffmanagesubcategory"))
    if action == "inactive":
        q="update subcategory set subcategory_status='inactive' where subcategory_id='%s' "%(subid)
        update(q)
        return redirect(url_for("staff.staffmanagesubcategory"))

    if action == "update":
        q="select * from subcategory where subcategory_id='%s'"%(subid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            name=request.form['name']
            desc=request.form['desc']

            q="update subcategory set subcategory_name='%s', subcategory_desc='%s' where subcategory_id='%s' "%(name,desc,subid)
            update(q)
            return redirect(url_for("staff.staffmanagesubcategory"))
    return render_template('staffmanagesubcategory.html',data=data) 




@staff.route('/staffmanageservice',methods=['get','post'])
def staffmanageservice():
    data={}
    stid=session['sid']
    q="select * from subcategory where subcategory_status='active'"
    data['sub']=select(q)

    if 'submit' in request.form:
        subid=request.form['subid']
        name=request.form['service']
        price=request.form['price']
    
        q="insert into servicemanagement values (null,'%s','%s','%s','active','%s')"%(subid,stid,name,price)
        insert(q)
        return redirect(url_for("staff.staffmanageservice"))


    q="select * from servicemanagement"
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        sid=request.args['sid']

      
    else:
        action=None

    if action == "active":
        q="update servicemanagement set service_status='active' where service_id='%s' "%(sid)
        update(q) 
        return redirect(url_for("staff.staffmanageservice"))
    if action == "inactive":
        q="update servicemanagement set service_status='inactive' where service_id='%s' "%(sid)
        update(q)
        return redirect(url_for("staff.staffmanageservice"))

    if action == "update":
        q="select * from servicemanagement where service_id='%s'"%(sid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            name=request.form['service']
            price=request.form['price']
            q="update servicemanagement set service_name='%s', price='%s'  where service_id='%s' "%(name,price,sid)
            update(q)
           
            return redirect(url_for("staff.staffmanageservice"))
    return render_template('staffmanageservice.html',data=data) 


@staff.route("/staffviewcustomers")
def staffviewcustomers():
    data={}
    q="select * from customer"
    data['res']=select(q)

    if 'action' in request.args:
        action=request.args['action']
        uname=request.args['uname']
        cid=request.args['cid']
      
    else:
        action=None

    if action == "active":
        q="update login set status='active' where username='%s' "%(uname)
        update(q)
        q="update customer set c_status='active' where customer_id='%s' "%(cid)
        update(q)
        return redirect(url_for("staff.staffviewcustomers"))
    if action == "inactive":
        q="update login set status='inactive' where username='%s' "%(uname)
        update(q)
        q="update customer set c_status='inactive' where customer_id='%s' "%(cid)
        update(q)
        return redirect(url_for("staff.staffviewcustomers"))
    return render_template("staffviewcustomers.html",data=data)


@staff.route('/staffviewbookings')
def staffviewbookings():
    data={}
    q="SELECT * FROM  `booking_master`, `booking_child`, `servicemanagement`, `customer` WHERE `booking_master`.`bookingmaster_id`=`booking_child`.`bookingmaster_id` AND `booking_child`.`service_id`=`servicemanagement`.`service_id` AND `booking_master`.`customer_id`=`customer`.`customer_id`"
    data['res']=select(q)
    return render_template('staffviewbookings.html',data=data)


@staff.route('/staffviewpyments')
def staffviewpyments():
    data={}
    bmid=request.args['bmid']
    q="SELECT * FROM payment inner join bookingmaster using (bookingmaster_id) inner join card using (card_id) where bookingmaster_id='%s'"%(bmid)
    data['res']=select(q)
    return render_template('staffviewpyments.html',data=data)