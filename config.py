import os

basedir = os.path.abspath(os.path.dirname(__file__))
REGIONS_API = "https://restcountries-v1.p.rapidapi.com/all"
REGIONS_API_KEY = "e3c72e9959mshb15ebe3aa08ae7fp14b65bjsne9efb150883b"
COUNTRIES_API = "https://restcountries.eu/rest/v2/region/"

class Config(object):
    SECRET_KEY = "Challenge-Python-L1"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
