# pollsite

This site is not in production, you have to run it locally

Installation (linux):
----------------
-clone this repo to your local machine

-create .env file to the root folder of the cloned folder and make it say this:

	DATABASE_URL=<*>
 	SECRET_KEY=<**>

	(in my case <*> is postgresql://hyxhyx and <**> is a random key I genereated)

-activate virtual environment and install dependencies with these commands in project folder:

 	$ python3 -m venv venv
	$ source venv/bin/activate
	$ pip install -r ./requirements.txt

-start your database:
	
 	$ start-pg.sh

-define the schema of the project database:
	
 	>option 1 (if your database has no same tables as this project):
		$ psql < schema.sql
	>option 2 (if you know or suspect your database has same tables as this project):
		+run psql and create a new database:
			$ psql
			user=# CREATE DATABASE <new_database>;
			$ psql -d <new_database> < schema.sql
		+in the project folder modify .env to point to this new database
			if you named your database testi, then in .evn:
				DATABASE_URL=portgresql://testi
-run the project:
	
 	$ flask run
		(flask will propt a local address where the site is running)

----------

Completed:

-sign up

-login

-creation of simple one choice polls with limited choices

-database schema for users, polls, choices and answers

-csrf on creation of polls and voting

- management (deletion/hiding) of own polls

TODO:

-user groups (A-D in database but not yet used)

-multiple choice variant of polls

-addition of new choices by voters

-time sentisitive polls

-admin features


----------


Original pitch:

Site where users can make polls and participate on polls.

The site enables users to create polls that other registered users can vote on.
The polls can be multiple choice and can include open text fields for new voting options.
Users can select particular groups who can see their created polls.
Poll creators can set time sensitive expiry of their polls.
The site will have a mandatory login for users.
Site admin can freely edit and delete polls.
All the user data and poll data are stored in a sql database.

