from app import app,db
from app.models import Device
from flask import request

@app.route('/')
@app.route('/index')
def index():
	return "haha"


@app.route('/register', methods=['POST'])
def register():
	data=request.get_json()
	temp_device=db.session.query(Device).filter(Device.devicename==data['name'])
	if(temp_device.count()>0):
		temp_device.first().ipaddress=data['ipaddr']
		db.session.commit()
		return "Updated device details"
	d=Device(devicename=data['name'],ipaddress=data['ipaddr'])
	db.session.add(d)
	db.session.commit()
	return "Registered new Device"
