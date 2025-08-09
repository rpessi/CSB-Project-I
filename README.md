This is my project for Helsinki University course Cyber Security Base 2025: Project I.

Besides the Django related installations made during the Cyber Security Base 2025: Securing software -course, you'll be needing python-dotenv. You can install it by running
```bash
pip install python-dotenv
```


To test DEBUG = True vulnerability, you need to create an .env file to project root with content PW=choosepassword on in linux, run
```bash
export ADMIN_PW=choosepassword
```
on command line. Try voting in a poll without making a selection and see what happens.
