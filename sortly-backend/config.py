import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir,'db.sqlite3') #todo add a new Database here
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    