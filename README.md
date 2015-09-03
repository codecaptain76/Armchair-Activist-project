# Armchair-Activist (Change the world in 5 clicks)

Armchair Activist was created by giving myself "The 5 click challenge". I wanted to create an application to make giving back to the community as easy as possible for the user. By limiting the interface to 5 clicks, a user can go from start to finish in a timeframe that is smaller than a commercial break. This allows the user to have no excuse to change the world. Armchair Activist lets users join the global community through technology. It is an application that allows individuals who are interested in giving back to the community, an opportunity to discover nonprofits that may be inspiring to them. It allows users to search by category and zip code, to identify causes that they may want to become involved with. Through this web application, the public will be able to donate directly to the charity of their choice or discover and join volunteer opportunities in their local area. Not everyone can protest on the front lines, but anyone can be an Armchair Activist. 

# Technology Stack: 
Python, Flask, Flask-login, Html, Javascript, Jinja, SQLAlchemy, SQLite, CSS

# APIs:
Ammado (global donations), All for good (volunteer resources)

# How it works:
Armchair Activist lets users create an account and log in, to begin searching for nonprofits to donate to by keyword. The users information, as well as their search history are stored in the database using SQLite and SQLAlchemy. The donation search uses the "Ammado" API. The search results are displayed by the name of the nonprofit. Once the user chooses a nonprofit, they are directed to Ammado's site to the nonprofit's homepage for more information. There they can push a button to donate directly to the charity of choice, using multiple types of payments, as well as being able to set up single or repeat donation.
Also, by using the "All for good" API, individuals are able to conduct a more specific search of nonprofits by keyword as well as zipcode. This allows users to peruse the home page of the nonprofit for more information, and decide whether or not to give their time. Which they may choose to sign up for a shift directly from the site.

![Home Page](https://cloud.githubusercontent.com/assets/11415852/9655807/a0731b78-51e8-11e5-91d1-8be9550c9fe3.png)
