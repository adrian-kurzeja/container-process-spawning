# Requirements
I have prepared this project as a "fast copy" of my project in django (python2.7) and right now it requires two heroku apps:

- heroku postgres app 
- heroku Data for Redis

It is possible to ommit heroku paid apps by installing them during build and start extra process for free.
Of course postgres data won't be kept, but using dump before updating image and restore after, would allow it to be free.

# Steps to reproduce
1. Clone project
2. Add heroku Postgres app
3. Add heroku Data for Redis
4. Add `.docker-env` file variables to heroku project
5. Build locally and push:
```
heroku container:push web --app=yourApp
```
6. Release:
```
heroku container:release web --app=yourApp
```
7. Enter dyno
```
heroku ps:exec --dyno=web.1 --app=yourApp
```
8. Use `top` command to check processes


# Processes
You can add any proces you want inside file:
./server_files/daphne.supervisor.conf

Example of new process
```
[program:worker_new_1]
command=python manage.py runworker
directory=/code
autostart=true
autorestart=true
stdout_logfile = /code/server_files/worker.log
logfile_maxbytes=15
logfile_backups=2
redirect_stderr=true
```