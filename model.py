"""Tables and database functions for Armchair Activist project"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from flask.ext.login import UserMixin

##############################################################################

# Model definitions- Tables for holding info
#db.API
# class Nonprofit():
# 	""" Searchable nonprofits"""

# 	__tablename__ = "nonprofits"

# 	beneficiary_name = db.Column(db.String(50), nullable= False, primary_key=True)
# 	benficiary_id = db.Column(db.Integer(100), nullable= False)
# 	zipcode = db.Column(db.Integer, nullable= False)
# 	city = db.Column(db.String(50), nullable=False)
# 	categories = db.Column(db.String(50), nullable=False)
# 	strapline = db.Column(db.String(50), nullable= True)
# 	country = db.Column(db.String(5) nullable= False)
	
# 	def __repr__(self):
# 		""" Provides representation when printed """

# 		return "<Nonprofit beneficiary_name=%s strapline= %s city= %s zipcode=%d categories= %s" % (
# 			self.beneficiary_name, self.strapline, self.city, self.zipcode, self.categories )


class User(db.Model, UserMixin):

	__tablename__ = "users"

	id = db.Column("user_id", db.Integer, autoincrement=True, primary_key=True)
	username = db.Column(db.String(50), nullable=False)
	email = db.Column(db.String(50), nullable=False)
	password = db.Column(db.String(50), nullable=False)
	age = db.Column(db.Integer, nullable=True)
	zipcode = db.Column(db.Integer, nullable=False)

	def __repr__(self):

		return "<User username=%s email=%s age=%s zipcode=%s>" % (self.username, self.email, self.age, self.zipcode)

##########################################################################################

def connect_to_db(app):
#     """Connect the database to our Flask app."""

#     # Configure to use our SQLite database
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///armchair.db'
	app.config['SQLALCHEMY_ECHO'] = True
	db.app = app
	db.init_app(app)


if __name__ == "__main__":
#     # As a convenience, if we run this module interactively, it will leave
#     # you in a state of being able to work with the database directly.
	from server import app
	connect_to_db(app)
#     print "Connected to DB."

