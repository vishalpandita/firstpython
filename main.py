from flask import Flask
from flask import request, escape
app = Flask(__name__)
@app.route("/")
def index():
    celsius = str(escape(request.args.get("celsius", "")))
    return (
        """<form action="" method="get">
                <input type="text" name="celsius"
                <br>
                <input type="submit" value="Convert">
               </form>"""
            + celsius + str(request.args)
    )

@app.route("/<int:celsius>")
def faahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degress."""
    try:
        fahrenheit = float(celsius) * 9/5 +32
        fahrenheit = round(fahrenheit,3) # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "Invalid Input"


if __name__ == "__main__":
    app.run("127.0.0.1",port=8080,debug=True)