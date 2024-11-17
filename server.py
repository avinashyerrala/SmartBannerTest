from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def serve_index():
    return send_file('index.html')

@app.route('/manifest.json')
def serve_manifest():
    # Explicitly set Content-Type to application/json
    return send_file('manifest.json', mimetype='application/json')

@app.route('/<path:path>')
def serve_file(path):
    return send_file(path)

if __name__ == '__main__':
    app.run(debug=True)
