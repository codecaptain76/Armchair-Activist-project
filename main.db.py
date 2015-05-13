"""Tables and database functions for Armchair Activist project"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


##############################################################################

# Model definitions- Tables for holding info
#db.API
class Nonprofit():
	""" Searchable nonprofits"""

	__tablename__ = "nonprofits"

	nonprof_name = db.Column(db.String(50), nullable= False, primary_key=True)
	zipcode = db.Column(db.Integer, nullable= False)
	keyword = db.Column(db.String(50), nullable=False)
	#nonprofit_id = db.Column(db.Integer, nullable=True)

	def __repr__(self):
		""" Provides representation when printed """

		return "<Nonprofit nonprof_name=%s zipcode=%d nonprofit_id=%d>" % (
			self.nonprof_name, self.zipcode, self.nonprofit_id)

class Location():

	__tablename__ = "locations"

	zipcode = db.Column(db.Integer, nullable= False, primary_key=True)
	nonprof_name = nonprof_name = db.Column(db.String(50), nullable= False)

	def __repr__(self):

		return "<Location zipcode=%d nonprof_name=%s>" % (self.zipcode, 
			self.nonprof_name)

class User():

	__tablename__ = "users"

	user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	user_name = db.Column(db.String(50), nullable=False)
	email = db.Column(db.String(50), nullable=False)
	password = db.Column(db.String(50), nullable=False)
	age = db.Column(db.Integer, nullable=True)
	zipcode = db.Column(db.Integer, nullable=False)

	def __repr__(self):

		return "<User individuals_name=%s email=%s age=%s zipcode=%s>" % (self.individuals_name, self.email, self.zipcode)

##########################################################################################

#def connect_to_db(app):
#     """Connect the database to our Flask app."""

#     # Configure to use our SQLite database
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ratings.db'
#     db.app = app
#     db.init_app(app)


# if __name__ == "__main__":
#     # As a convenience, if we run this module interactively, it will leave
#     # you in a state of being able to work with the database directly.

#     from server import app
#     connect_to_db(app)
#     print "Connected to DB."

