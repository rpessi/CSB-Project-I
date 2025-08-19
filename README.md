This is my project for Helsinki University course Cyber Security Base 2025: Project I. The purpose of this project is to introduce security vulnerabilities and to provide fixes for them. Some vulnerabilities in this stem simply from lacking configuration or rather using the configuration that Django provides by default. Others needed purposeful misbehavior, using bad practises during development and/or introducing unsafe ways of communicating with database. The development database is included in this repository for convenience, not as an example of good practise. Similarly, failed_logins.log is included for reference. Zero attention is given to the esthetics of this app.

Besides the Django related installations made during the Cyber Security Base 2025: Securing software -course, you'll be needing python-dotenv. You can install it by running
```bash
pip install python-dotenv
```

To test DEBUG = True vulnerability (flaw-1) and its exploitation (flaw-2), you need to create an .env file to project root with content PW=choosepassword. Optionally, on in linux, run
```bash
export ADMIN_PW=choosepassword
```
on command line to set the ADMIN_PW for the session. Try voting in a poll without making a selection and see what happens.

To run the app, run
```bash
python3 manage.py runserver
```
at the root of the project.
