import os
import subprocess
from distutils.spawn import find_executable
from clint.textui import puts, prompt, colored

class GenerateFlaskHandler(object):

    def __init__(self, app):
        self.app = app

    def execute(self):
        puts(colored.green("\nNeat. Let's build you a Flask application.\n"))
        puts(colored.green("Checking for virtualenv and pip..."))

        venv = find_executable("virtualenv")
        pip = find_executable("pip")

        if pip is None:
            self.app.log.error("Missing pip. You'll need to install that before you can continue. Sorry, friend.\n")
            return

        if venv is None and pip is not None:
            puts(colored.yellow("Missing virtualenv, but pip is available. Installing virtualenv..."))
            os.system("pip install virtualenv")

        puts(colored.green("Looking good! Let's do this...\n"))

        app_name = prompt.query("Name of application: ")
        location = prompt.query("What folder should '%s' be installed in (no trailing / please)? " % app_name)

        if os.path.exists(location) == False:
            should_create = (prompt.query("That folder doesn't seem to exist... Create it? [y/n] ") == 'y')

            if should_create == True:
                puts(colored.green("\nCreating folder %s..." % location))
                os.mkdir(location)
            else:
                puts(colored.red("Okay. Cancelling installation... Bye!"))
                return

        venv_location = location + "/env"

        puts(colored.green("Generating virtualenv environment..."))
        os.system("virtualenv " + venv_location + " >> " + location + "/installation_log.log")
        puts(colored.green("Done! Installing Flask..."))
        os.system("source " + venv_location + "/bin/activate && pip install flask >> " + location + "/installation_log.log")
        puts(colored.green("Hey it probably kind of worked!"))
