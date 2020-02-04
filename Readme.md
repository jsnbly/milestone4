# 3lite Design
Milestone 4 Project for Code Institute  
This project is designed to showcase a Fullstack Website for a Graphic Design Company  
It allows them to Showcase their Portfolio and sell there products directly to customers.  

## Travis Build Status
[![Build Status](https://travis-ci.com/jsnbly/milestone4.svg?branch=master)](https://travis-ci.com/jsnbly/milestone4)  

## UX  
This site is developed for use by an imaginary graphic design company called 3lite Design  
They are looking for a way to take graphic design orders from customers all over the world  
They want to take a request from the customer give them a quote on the spot and then revert back  
to gain agreement on what is required. The site will allow the user to send images they would  
like included or modified to the admin and also allow them to send a message to clarify their needs.  
User stories below will give a clear view of what is required.    

Landing Page Wireframe -  https://github.com/jsnbly/milestone4/tree/master/UX/wireframes/index.png  
Admin Landing Wireframe - https://github.com/jsnbly/milestone4/tree/master/UX/wireframes/adminlanding.png  
User Quote Form Wireframe - https://github.com/jsnbly/milestone4/tree/master/UX/wireframes/qform.png   

### User Stories  
- As a site Admin I want a way to sell my graphic design products to customers  
- As a site Admin I want a way to show my previous work to customers  
- As a site Admin I want a way to take order requests, accept them and take payment for them  
- As a site Admin I want a way for users to log in to my site so I can save order information  
- As a user I want to see Previous work by the company  
- As a user I want a way to contact the company regarding an order  
- As a user I want to be able to send in custom orders with images to the company  
- As a user I want a quotation price for work before I pay for an order   
- As a user I want a way to save my orders so I can come back and purchase at a later date   


## Existing Features  
- User Account Registration to allow users to save items for purchase and have a way to see their request updates  
- Portfolio of previous work by the company  
- Showcase showing images of previous work and reviews on a Carousel   
- Request form so the customer can request custom work  
- Image Upload Fuction so the customer can send their ideas to the admin  
- Pre Check out Calculator so the customer can be quoted prior to purchase    
- Admin Panel so admin can see requests from Customer and revert  
- Review Form after customer Purchases giving option to add their image to sites showcase  
- Navbar/Footer/Social Media Links  


## Technologies Used  
The Project was built using the Following Technologies  
Bootstrap 4  
Font Awesome 5  
Simpleline Icons 2.4.1  
Google Fonts    
Python 3.5.3  
Django 2.2.9  
Postgres DB  
dj-database-url - Used to Connect to PostgreSQL Database    
psycopg2 - PostgreSQL Adaptor for Python  
gunicorn 19.10.0  
django-storages 1.8  
botos3 1.11.5  
Stripe API (For Payments)  
Heroku - Hosting Platform  
Amazon Web Services for S3 Hosting  
Balsamiq for Wireframing  
VS Code IDE of choice          

## Testing  

Locally I used the built in django server to run and test the application  
this would allow me to see the changes in real time, I intergated TravisCI  
into my github repository this allowed me test it as it was being pushed to  
github.  

Remotely I used Heroku Logs to see build progress as the project was pushed  
to heroku as the code was running locally and tested locally and on travis  
heroku deployment was usually a mirror of build success. AWS Console gave  
me access to my s3 bucket this allowed me to check all static files so images  
and css are collected correctly when running collectstatic command.  

Automated testing was used by adding to tests.py in individual applications  
as an example of this threeshop tests.py shows how automated testing can be used  
to add a Product to the shop. Along with Travis this kind of testing would allow  
the project to grow larger and keep the main business logic working easily.  

W3 Validators for HTML and CSS was used to try and keep the code clean and valid  

Along with the above extensive manual testing for resposiveness using chrome  
developer tools was done to make sure all users will have a similar experience  
no matter what device they view the site on  .

## Deployment  
To deploy this project I used Heroku for hosting the Application, Amazon  
Web Services S3 Bucket was used to host the static files for the project  
a PostgresDB hosted on Heroku was used to handle the Database requirements  
Below is a run down of the deployment stages.  

### Local Deployment:  
Start a Virtual Enviroment in Python to make sure you only have to work  
with needed requirements and don't get caught with lots of un-needed requirements    

Starting the Django Project:  
pip3 freeze > requirements.txt   
Django-admin startproject milestone4 .    

To start Djangos built in Server Run:  
python3 manage.py runserver

Adding Travis CI for CI Testing:  
Go to travis-ci.org  
Login with Github and Select repository for testing  
Copy Markdown code and added to Readme.md  
Add .travis.yml file to root directory and added project information to file  
Pushed changes to github  
Check to See that build succeeded on github.com/reponame 

As the app matured locally and I added API keys these were turned into os.get.env  
calls and they pointed to an env.py file this is missing from the github repo as  
it contains access keys to stripe,AWS and postgresDB so this will need to be added  
if you wish to run the file locally also you will have the uncomment the import env  
at the top of settings.py in milestone4.  

### Remote Deployment:  
Setup Amazon Web Services S3 Bucket so a Policy was created in the AWS Console  
to allow me to setup static file hosting on amazon  

With the AWS S3 Bucket created I then created a user for that Bucket so I could  
get access keys to allow me to feed that into the application  

On Heroku I setup a new application, setup a postgres db in Heroku addons and  
set up Config Vars to point to my AWS Keys, my Stripe API Keys and the Postgres DB,  
This was then added the the application as os.get.env calls this is required as  
env.py has been gitignored so as not to leave accesskeys and passwords open to the  
world to see. Also the secret key for the django application has been removed from  
the settings.py application and changed from the orginal secret key used in development.   

## Credits  
Codeinstitute for the great content provided  
Landing page was based off a template from  https://startbootstrap.com/themes/  

### Content  
All Content is copyright of its respected owner(s)    

### Media  
All Media was sourced from google image and remains copyright of its orginal owner  
it is used for educational purposes in this repository and every effort was made  
to find free images to use.    

### Acknowledgements
Again Like to thank Codeinsitute for their great course content very enjoyable  
Would Like to thank my Mentor SpencerB for all his guidance over these past 4 projects  


