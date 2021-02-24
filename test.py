from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def index():
    if request.method == "POST":
        print("Data recibida")

        if "file" not in request.files:
            return redirect(request.url)
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True, threaded=True)