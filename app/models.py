from app import db
from datetime import datetime

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    devicename = db.Column(db.String(64), index=True)
    ipaddress = db.Column(db.String(120), index=True)
    updatetime = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
        return '<Device {} {}>'.format(self.devicename,self.ipaddress)    
