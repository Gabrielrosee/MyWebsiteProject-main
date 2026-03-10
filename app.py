from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index2.html")

@app.route("/ventures")
def ventures():
    return render_template("Ventures.html")

@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/page/<page_name>")
def dynamic_page(page_name):
    try:
        return render_template(f"{page_name}.html")
    except:
        return "<h1>404 - Page not found</h1><p>Sorry, that page doesn't exist.</p>", 404

if __name__ == "__main__":
    print("Starting Flask server... Visit http://127.0.0.1:5000")
    app.run(debug=True)