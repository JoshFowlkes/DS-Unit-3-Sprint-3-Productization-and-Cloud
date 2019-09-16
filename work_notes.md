# Some General Notes on the ongoing Twitoff Project 
------------------

`FLASK_APP=hello.py flask run` 
*running this^^ from within pipenv shell gets it running locally on a site*


`FLASK_APP=twitoff:APP flask run`
run this from directory that contains twitoff(init & app) and runs like above line

September 16, 2019
What went well? Was able to fly through most of the lecture and through this initial iteration of the project. Some issues, had to conda install flask early on, and handling a rollback error that i'll detail in the third question here, but otherwise, nice smooth running so far. 


What was particularly interesting or surprising about the topics today? Just the fact that I'm actually creating these web applications by hand and from terminal. Several months ago if you told me: make a web app from the terminal on your computer I would have been like: 'lol what?' MIND you its only local, hasn't actually properly been deployed on the web yet for clarification. Oh and populating an SQL database from scratch from the command line, wow super incredible. This is the start of something great. 


What was the most challenging part of the work today and why? Towards the end of today I started to run into an SQLALCHEMY nested rollback error. The way I fixed it was with a session roll back then recommit users and tweets that I had made during a local python session. ALSO, I was running ito this `NOT NULL constraint failed: tweet.id` which has been fixed(at least it appears) when I added the formating and the user_id stuff to the models.py Tweet class.  

