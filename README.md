# third_world_search_engine

I hope you enjoy this project, it was kind of quick so it obviously can be improved in a lot of ways, have a wonderful day, as usual remember to git clone the project ;)

BTW we use mysql for this project, so if you plan to use this DB locally be sure to have it installed and running in your computer, here is a good tutorial for that https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04

Valar morghulis

### Install with this dependencies
    sudo apt-get install python-mysqldb
    sudo apt-get install libmysqlclient-dev

### Create a virtual enviroment and activate it
    python3 -m venv venv
    source venv/bin/activate

### At this point, you should be inside the project, then install the dependencies from requirements.txt
    pip install -r requirements.txt
    
If you experience any problem installing de dependencies, try manually install this specific dependencies
              
    pip install Flask
    pip install beautifulsoup4
    pip install requests
    pip install flask-sqlalchemy
    pip install flask-migrate
    pip install python-dotenv
    pip install mysqlclient
    
### Create a .env file in the root of the project and follow this example to see what variables do you need there
Remember, this is a file, no code for the terminal

      DB_USER=your_mysql_user
      DB_PSW=your_mysql_user's_password
      DB_URL=localhost_or_server_url
      DB_NAME=a_db_name
Fort this project, you can choose the db name but i propose you to use deltaitest

### How to run
With this command we specify the file to run with flask

    export FLASK_APP=deltai_api.py
    

And then, finally we run our project in local, as default it will run in the port 5000

    flask run

Here a note, the migrations are already in the project, but if you experience any problem with them, first be sure that the database is created, if not do it manually *create database deltaitest;* and just to be sure delete the migrations folder and run the next commands

With this command, we start the migration folder and all the sutff for SQLAlchemy
    
    flask db init
    
With the following commands, we prepare the models migrations and then we created them in the DB

    flask db migrate 
    flask db upgrade

Now it should be running, again enjoy!
