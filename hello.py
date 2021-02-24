from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

# The first initialization
# pybabel extract -F babel.cfg -o messages.pot --input-dirs=.
# The second initialization
# pybabel init -i messages.pot -d translations -l de
# Finally compile your changes
# pybabel compile -d translations
# To merge the changes create a new messages.po file and copy text and run
# pybabel update -i messages.pot -d translations
