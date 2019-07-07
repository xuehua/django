# django
This repository holds different django projects.

****
## Heroku Deployment Steps
1. Remember to change ALLOWED_HOSTS in settings.py  
   Here we change the setting of ALLOWED_HOSTS
   pages_project/pages_project/settings.py as follwing.  
   ALLOWED_HOSTS = ['*'] 

2. Copy Pipfile, Pipfile.lock under the top directory to the corresponding  
   projects and commit the changes.  
   For pages_project, we copy the files to the directory of pages_project.  

3. Add Procfile in the corresponding project directory.  
   For pages_project, we have Procfile as following.  
   web: gunicorn pages_project.wsgi --log-file -

4. Run "heroku login" to log in.  

5. Run "heroku create".  
   This will create an app with a unique name avaiable. For example,
   damp-crag-81324. 

6. Run "heroku git:remote -a $appname".  
   For the above new app created, we can run "heroku git:remote -a
   damp-crag-81324".   
   This will create a remote of heroku linked to
   https://git.heroku.com/damp-crag-81324.git

7. Rename the remote using "git remote rename" to rename the heroku to
   heroku-$project.  
   For example, we run "git remote rename heroku heroku-pages" for the
   pages_project. 

8. Optional: configure heroku with DISABLE_COLLECTSTATIC=1.  
   For pages_project, static files are not supported, we run this step.  
   Run "heroku config:set DISABLE_COLLECTSTATIC=1 --remote heroku-pages"  
   For mb_project, static files are supported, but not for production usage.
   This step is not needed.  
   For blog_project, static files are supported using whitenoise and can be used
   in production environment. This step is not needed either. 
   

9. Push codes to Heroku.  
   Run "git subtree push --prefix pages_project heroku-pages master"

10. Make heroku run the app at lowest level, web=1, which is free.  
   Run "heroku ps:scale web=1 --remote heroku-pages"

11. Open the website corresponding to the app.  
   Run "heroku open --remote heroku-pages"     
****