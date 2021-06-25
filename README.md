# pyGIT

pyGIT is an unitility that uses github api to handle remote repositories actions like creation, list and deletion right from the terminal. 

# Features
with pyGit you can: 
* Set up your github username and token as environment variables so to browse, create and delete your repositories without leaving the terminal.
* Specify the user for whom you want to browse public repositories. pyGit will tell you the right url for you to clone.

# Dependencies
pyGit only depends on [Rich](https://rich.readthedocs.io/en/latest/introduction.html), a python library for rich text (with color and style) to the terminal.
By the way, this project is awesome! You should really check it out.

# Installation
* Clone the repo and use pip install -e . to install.

# TODO
* Create a TUI for the application
	- Should allow to clone public repositories withouth copy and paste
	- Should allow to make creation and deltion of repositories a bit more interactive
