import os
import subprocess
from distutils.spawn import find_executable
from cement.core import backend, foundation, controller, handler

class BaseController(controller.CementBaseController):
    class Meta:
        label = 'base'
        description = 'Generate and build out your Flask application with one stupid CLI.'

    @controller.expose(hide=True, aliases=['run'])
    def default(self):
        self.app.log.info("You should probably run a command.")
        self.app.log.info("Try running with --help if you're lost.")

    @controller.expose(help="Generate a basic Flask application scaffold.")
    def generate_flask(self):
        print("\nNeat. Let's build you a Flask application.\n")
        print("Checking for virtualenv and pip...")

        venv = find_executable("virtualenv")
        pip = find_executable("pip")

        if pip is None:
            self.app.log.error("Missing pip. You'll need to install that before you can continue. Sorry, friend.\n")
            return

        if venv is None and pip is not None:
            print("Missing virtualenv, but pip is available. Installing virtualenv...")
            subprocess.Popen("pip install virtualenv")

        print("Looking good! Let's do this...\n")

        app_name = raw_input("Name of application: ")
        location = raw_input("What folder should '%s' be installed in (no trailing / please)? " % app_name)

        if os.path.exists(location) == False:
            should_create = (raw_input("That folder doesn't seem to exist... Create it? [y/n] ") == 'y')

            if should_create == True:
                print("Creating folder %s..." % location)
                os.mkdir(location)
        venv_location = location + "/env"
        command = "virtualenv " + location
        subprocess.Popen(command)
