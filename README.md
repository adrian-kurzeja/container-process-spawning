# Requirements
I have build this project on django and right now it requires two heroku apps:

- heroku postgres app 
- heroku Data for Redis

It is possible to ommit heroku paid apps. I have to install them during build and start extra process for free.

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


