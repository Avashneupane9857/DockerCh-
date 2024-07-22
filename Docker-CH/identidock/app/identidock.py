from flask import Flask, Response, request
import requests

app = Flask(__name__)
default_name = 'Joe Bloggs'

@app.route('/', methods=['GET', 'POST'])
def index():
    name = default_name
    if request.method == 'POST':
        name = request.form.get('name', default_name)

    header = '<html><head><title>Identidock</title></head><body>'
    body = '''<form method="POST">
              Hello <input type="text" name="name" value="{}">
              <input type="submit" value="Submit">
              </form>
              <p>You look like a:
              <img src="/monster/{}"/>
              '''.format(name, name)
    footer = '</body></html>'

    return header + body + footer

@app.route('/monster/<name>')
def get_identicon(name):
    try:
        r = requests.get(f'http://dnmonster:8080/monster/{name}?size=80')
        r.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        image = r.content
        return Response(image, mimetype='image/png')
    except requests.RequestException as e:
        # Handle request errors (e.g., dnmonster is down)
        return f"Error fetching identicon: {e}", 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)

