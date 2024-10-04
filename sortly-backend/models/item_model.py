from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    
    def __init__(self, name, location, quantity) -> None:
        self.name = name
        self.location = location
        self.quantity = quantity
    
    def to_dict(self):
        return {'id':self.id,'name': self.name, 'location': self.location, 'quantity': self.quantity}
        
    def json(self):
        return {'id':self.id,'name': self.name, 'location': self.location, 'quantity': self.quantity}

