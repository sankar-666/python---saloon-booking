from flask import *
from database import *
import uuid

admin=Blueprint('admin',__name__)


@admin.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')



@admin.route('/adminmanagestaff',methods=['get','post'])
def adminmanagestaff():
    data={}
    if 'submit' in request.form:
        email=request.form['email']
        password=request.form['password']
        fname=request.form['fname']
        lname=request.form['lname']
        dob=request.form['dob']
        gender=request.form['gender']
        housename=request.form['housename']
        city=request.form['city']
        district=request.form['district']
        pin=request.form['pin']
        phone=request.form['phone']
  

        q="select * from login where username='%s'"%(email)
        res=select(q)
        if res:
            flash("Username Already Exist!")
        else:
            q="insert into login values ('%s','%s','staff','active')"%(email,password)
            insert(q)
            q="insert into staff values (null,'%s','%s','%s','%s',curdate(),'%s','%s','%s','%s','%s','%s','%s','active')"%(email,fname,lname,password,dob,gender,housename,city,district,pin,phone)
            insert(q)
            return redirect(url_for("admin.adminmanagestaff"))

    data={}
    q="select * from staff"
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        uname=request.args['uname']
        stid=request.args['stid']
      
    else:
        action=None

    if action == "active":
        q="update login set status='active' where username='%s' "%(uname)
        update(q)
        q="update staff set s_status='active' where staff_id='%s' "%(stid)
        update(q)
        return redirect(url_for("admin.adminmanagestaff"))
    if action == "inactive":
        q="update login set status='inactive' where username='%s' "%(uname)
        update(q)
        q="update staff set s_status='inactive' where staff_id='%s' "%(stid)
        update(q)
        return redirect(url_for("admin.adminmanagestaff"))

    if action == "update":
        q="select * from staff where staff_id='%s'"%(stid)
        val=select(q)
        data['staff']=val

        if 'update' in request.form:
            # email=request.form['email']
            # password=request.form['password']
            fname=request.form['fname']
            lname=request.form['lname']
            dob=request.form['dob']
            gender=request.form['gender']
            housename=request.form['housename']
            city=request.form['city']
            district=request.form['district']
            pin=request.form['pin']
            phone=request.form['phone']

            q="update staff set s_fname='%s', s_lname='%s', s_dob='%s', s_gender='%s', s_housename='%s', s_city='%s', s_district='%s', s_pin='%s', s_phone='%s' where staff_id='%s' "%(fname,lname,dob,gender,housename,city,district,pin,phone,stid)
            update(q)
            return redirect(url_for("admin.adminmanagestaff"))
    return render_template('adminmanagestaff.html',data=data) 



@admin.route('/adminmanagecaterogy',methods=['get','post'])
def adminmanagecaterogy():
    data={}
    if 'submit' in request.form:
        name=request.form['name']
        desc=request.form['desc']
    
        q="insert into category values (null,'%s','%s','active')"%(name,desc)
        insert(q)
        return redirect(url_for("admin.adminmanagecaterogy"))

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
        return redirect(url_for("admin.adminmanagecaterogy"))
    if action == "inactive":
        q="update category set category_status='inactive' where category_id='%s' "%(cat_id)
        update(q)
        return redirect(url_for("admin.adminmanagecaterogy"))

    if action == "update":
        q="select * from category where category_id='%s'"%(cat_id)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            name=request.form['name']
            desc=request.form['desc']

            q="update category set category_name='%s', category_desc='%s' where category_id='%s' "%(name,desc,cat_id)
            update(q)
            return redirect(url_for("admin.adminmanagecaterogy"))
    return render_template('adminmanagecaterogy.html',data=data) 



@admin.route('/adminmanagesubcategory',methods=['get','post'])
def adminmanagesubcategory():
    data={}

    q="select * from category where category_status='active' "
    data['cat']=select(q)
    if 'submit' in request.form:
        catid=request.form['catid']
        name=request.form['name']
        desc=request.form['desc']
    
        q="insert into subcategory values (null,'%s','%s','%s','inactive')"%(catid,name,desc)
        insert(q)
        return redirect(url_for("admin.adminmanagesubcategory"))


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
        return redirect(url_for("admin.adminmanagesubcategory"))
    if action == "inactive":
        q="update subcategory set subcategory_status='inactive' where subcategory_id='%s' "%(subid)
        update(q)
        return redirect(url_for("admin.adminmanagesubcategory"))

    if action == "update":
        q="select * from subcategory where subcategory_id='%s'"%(subid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            name=request.form['name']
            desc=request.form['desc']

            q="update subcategory set subcategory_name='%s', subcategory_desc='%s' where subcategory_id='%s' "%(name,desc,subid)
            update(q)
            return redirect(url_for("admin.adminmanagesubcategory"))
    return render_template('adminmanagesubcategory.html',data=data) 




@admin.route('/adminmanageservice',methods=['get','post'])
def adminmanageservice():
    data={}

    q="select * from subcategory where subcategory_status='active'"
    data['sub']=select(q)

    if 'submit' in request.form:
        subid=request.form['subid']
        name=request.form['service']
        price=request.form['price']
    
        q="insert into servicemanagement values (null,'%s','0','%s','active','%s')"%(subid,name,price)
        insert(q)
        return redirect(url_for("admin.adminmanageservice"))


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
        return redirect(url_for("admin.adminmanageservice"))
    if action == "inactive":
        q="update servicemanagement set service_status='inactive' where service_id='%s' "%(sid)
        update(q)
        return redirect(url_for("admin.adminmanageservice"))

    if action == "update":
        q="select * from servicemanagement where service_id='%s'"%(sid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            name=request.form['service']
            price=request.form['price']
            q="update servicemanagement set service_name='%s', price='%s'  where service_id='%s' "%(name,price,sid)
            update(q)
           
            return redirect(url_for("admin.adminmanageservice"))
    return render_template('adminmanageservice.html',data=data) 



@admin.route('/adminviewbookings')
def adminviewbookings():
    data={}
    q="SELECT * FROM  `booking_master`, `booking_child`, `servicemanagement`, `customer` WHERE `booking_master`.`bookingmaster_id`=`booking_child`.`bookingmaster_id` AND `booking_child`.`service_id`=`servicemanagement`.`service_id` AND `booking_master`.`customer_id`=`customer`.`customer_id`"
    data['res']=select(q)
    return render_template('adminviewbookings.html',data=data)


@admin.route('/adminviewpayment')
def adminviewpayment():
    data={}
    bmid=request.args['bmid']
    q="SELECT * FROM payment where bookingmaster_id='%s'"%(bmid)
    data['res']=select(q)
    return render_template('adminviewpayment.html',data=data)