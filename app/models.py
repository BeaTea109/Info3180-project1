from . import db


class PropertyObject(db.Model):
     __tablename__ = 'properties'
     id = db.Column(db.Integer, primary_key=True)
     propertyTitle = db.Column(db.String(255), nullable=False)
     propertyDescription = db.Column(db.String(255), nullable=False)
     propertyBathrooms = db.Column(db.Integer, nullable=False)
     propertyBedrooms = db.Column(db.Integer, nullable=False)
     propertyType = db.Column(db.String(30), nullable=False)
     propertyPhoto = db.Column(db.String(255), nullable=False)
     propertyPrice = db.Column(db.Float(4), nullable=False)
     propertyLocation = db.Column(db.String(255), nullable=False)

     def __init__(self, propertyTitle, propertyDescription, propertyBathrooms, propertyBedrooms, propertyType, propertyPhoto, propertyPrice, propertyLocation):
         self.propertyBathrooms = propertyBathrooms
         self.propertyDescription = propertyDescription
         self.propertyBedrooms = propertyBedrooms
         self.propertyTitle = propertyTitle
         self.propertyType = propertyType
         self.propertyPhoto = propertyPhoto
         self.propertyPrice = propertyPrice
         self.propertyLocation = propertyLocation
