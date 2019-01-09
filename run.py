"""Init script."""
from flask import Flask
from flask import send_file

app = Flask(__name__)


@app.route('/')
def index():
    """RETURN: landing page message."""
    return "PuPPy API is live!"


@app.route('/pup')
def get_pup():
    """RETURN: corgi picture."""
    try:
        return send_file(
            "static/corgi.jpg",
            mimetype='image/jpeg',
        ), 200
    except KeyError as err:
        return 'I\'m sorry, your corgi could not be retrieved at the moment'.format(err), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
