"""Utility file to seed ratings database from MovieLens data in seed_data/"""


from model import User, Nonprofit, connect_to_db, db
from server import app


def load_users():
    
    print "users"

    for i, row in enumerate(open(" ")):
        row = row.rstrip()
        
        user_id, user_name, email, password, age, zipcode = row.split("|")

        user = User(user_id=user_id,
                    user_name=user_name
                    email=email
                    password=password
                    age=age,
                    zipcode=zipcode)

        # We need to add to the session or it won't ever be stored
        db.session.add(user)

        # provide some sense of progress
        if i % 100 == 0:
            print i

    # Once we're done, we should commit our work
    db.session.commit()


def load_nonprofits():

    print "nonprofits"

    for i, row in enumerate(open(" ")):
        row = row.rstrip()

        beneficiary_name, benficiary_id, zipcode, city, 
        categories, strapline, country = row.split("|")

        nonprofit = Nonprofit( beneficiary_name= beneficiary_name
                               benficiary_id= benficiary_id
                               zipcode= zipcode
                               city= city 
                               categories= categories
                               strapline= strapline)

        # We need to add to the session or it won't ever be stored
        db.session.add(nonprofit)


    
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    load_users()
    load_nonprofits()


