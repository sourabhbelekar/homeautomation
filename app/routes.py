from app import app,db
from app.models import Device
from flask import request,render_template
import datetime

@app.route('/')
@app.route('/index')
def index():
    ct=datetime.datetime.utcnow()
    lt = ct - datetime.timedelta(seconds=10)
    q=db.session.query(Device).filter(Device.updatetime > lt).all()
    
    urls=q
    #for device in q:
    #    urls.append('http://'+device.ipaddress+'/')
    iframe = "http://www.google.com"

    return render_template('index.html', iframe=iframe,devices=urls)


@app.route('/test')
def test():
	return "haha"

@app.route('/control',methods = ['POST'])
def control():
        if request.method == 'POST':
                result = request.form
                return render_template("control.html",iframe=request.form["devices"])



@app.route('/register', methods=['POST'])
def register():
	data=request.get_json()
	temp_device=db.session.query(Device).filter(Device.devicename==data['name'])
	if(temp_device.count()>0):
		temp_device.first().ipaddress=data['ipaddr']
		temp_device.first().updatetime=datetime.datetime.utcnow()
                db.session.commit()
		return "Updated Device"
	d=Device(devicename=data['name'],ipaddress=data['ipaddr'])
	db.session.add(d)
	db.session.commit()
	return "Added New Device"
