from flask import Flask, render_template

app = Flask("First Bootstrap App")

@app.route("/")
def index():
  return render_template('index.html')

app.run(debug=True, port=8000)
