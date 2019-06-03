from app import db

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    devicename = db.Column(db.String(64), index=True, unique=True)
    ipaddress = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<Device {} {}>'.format(self.devicename,self.ipaddress)    
