from flask import Flask, render_template, request
from data.tracking_data import tracking_data
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def track():
    result = None
    error = None
    if request.method == 'POST':
        code = request.form['code'].strip()
        result = tracking_data.get(code)
        if not result:
            error = "Tracking ID not found."
    return render_template('track.html', result=result, error=error)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)