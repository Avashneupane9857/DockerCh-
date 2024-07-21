from flask import Flask, request

app = Flask(__name__)
default_name = 'Joe Bloggs'

@app.route('/', methods=['GET', 'POST'])
def get_identicon():
    name = default_name
    if request.method == 'POST':
        name = request.form.get('name', default_name)

    header = '<html><head><title>Identidock</title></head><body>'
    body = '''<form method="POST">
              Hello <input type="text" name="name" value="{}">
              <input type="submit" value="Submit">
              </form>
              <p>You look like a:
              <img src="/monster/monster.png"/>
              '''.format(name)
    footer = '</body></html>'

    return header + body + footer

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)

