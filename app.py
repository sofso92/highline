# Import the Flask class from the flask package.
from flask import Flask, render_template

# Create an instance of the Flask class. This instance is our WSGI application.
# The first argument is the name of the application’s module or package.
# If you are using a single module (as in this example), you should use __name__
# because depending on if it’s started as application or imported as module the
# name will be different ('__main__' versus the actual import name).
app = Flask(__name__)


# The route() decorator tells Flask what URL should trigger the function that follows.
# In this case, when a web browser requests the root URL '/' (i.e., the main page),
# Flask will invoke the home() function.
@app.route('/')
def home():
    # The function returns a string, which is the message that will be displayed
    # on the user's browser when they navigate to the root URL. This is the response
    # that the browser will display.
    return render_template('home.html')
    
    #return "Welcome to Our Painting Company!"


# This block is a Python idiom. When the Python interpreter reads a source file,
# it executes all of the code found in it. Before executing the code, it defines a few
# special variables. For example, if the Python interpreter is running that module
# (the source file) as the main program, it sets the special __name__ variable to
# have a value "__main__". If this file is being imported from another module,
# __name__ will be set to the module's name.
# In the case of this script, we are checking if __name__ was set to "__main__",
# meaning the script is being executed as the main program, and therefore we call
# the app.run() to start the server.
if __name__ == "__main__":
    app.run(debug=True)