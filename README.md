<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="Playground" />

&#xa0;

  <!-- <a href="https://playground.netlify.app">Demo</a> -->
</div>

<h1 align="center">Playground</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/Gustaf26/playground?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/Gustaf26/playground?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/Gustaf26/playground?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/Gustaf26/playground?color=56BEB8">

</p>

<!-- Status -->

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/Gustaf26" target="_blank">Author</a>
</p>

<br>

## :dart: About

CREATE A DJANGO PROJECT WITH BETTER KNOWLEDGE

Create a root folder from scratch in your computer and open it with VSCode

Before running Django, you need to set up a virtual environment (venv) in the root folder and activate it with:

python -m venv ./venv

Then you can start the project running this command on the root folder

django-admin startproject mysite

In manage.py you may find the following standard variable and value:

if **name** == '**main**':
main()

It is there so that this root folder where manage.py is, will be considered as a script that can be reused and that will be the main folder of the project as well.

Now that your environment (a "project") has been set up, you're ready to get to work.

What we want to do is to create an application that does something inside our project

Every application you write in Django consists of a Python package that follows a certain convention. Django has a utility that automatically generates the basic directory structure of an application, so you can focus on writing code instead of creating directories.

In orfer to create an app inside our project. We run the following command:

python manage.py startapp my_app_name

What we get is a bunch of files that will be used as a python-package with submodules (the python files belonging to the app).

The **init**.py file inside the app is nothing but an initializer of the app that tells the main folder of the project that all files inside this folder are to be considered as a python-package (with the python files-submodules we talked about). It can stay empty and the app will run as well!

Setting up environmental variables

As stated above, Django runs with SQLite by default, that is, a sqlite database file will be automatically added to the root folder because that is what is stated in the settings.py file in the project folder.

In this file you will find a SECRET_KEY variable to run the db, with a value that is not to be exposed, for instance in Github.

In order to keep the secret key ‘secret’ we need to install a Python package that allows the key to be imported to settings.py without compromising the project, so that settings.py can be pushed to your Git repository. Python-dotenv allows us to do this, so run this command

    pip install python-dotenv

…and then import to the settings.py the dotenv package as follows:

from dotenv import load_dotenv

Create a file named .env in the root folder, and add there the variable

SECRET_KEY = ”your_database_secret_key”.

Now in settings.py you can just write SECRET_KEY=load_dotenv() and you are ready to go!

But one last thing: add your .env file to your .gitignore file before pushing any code to Git

## :sparkles: Features

:heavy_check_mark: Feature 1;\
:heavy_check_mark: Feature 2;\
:heavy_check_mark: Feature 3;

## :rocket: Technologies

The following tools were used in this project:

- [Django](https://docs.djangoproject.com/)
- [Python](https://docs.python.org/)

## :white_check_mark: Requirements

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) installed.

## :checkered_flag: Starting

```bash
# Clone this project
$ git clone https://github.com/Gustaf26/playground

# Access
$ cd playground

# Install dependencies
$ yarn

# Run the project
$ yarn start

# The server will initialize in the <http://localhost:3000>
```

## :memo: License

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.

Made with :heart: by <a href="https://github.com/Gustaf26" target="_blank">Gustaf26</a>

&#xa0;

<a href="#top">Back to top</a>
