from flask import Flask
from flask import request
app = Flask(__name__)
@app.route("/")
def index():
    celsius = request.args.get("celsius", "")
    if celsius:
        fahrenheit = fahrenheit_from(celsius)
    else:
        fahrenheit = ""
    return (
        """<form action="" method="get">
                <input type="text" name="celsius"
                <br>
                <input type="submit" value="Convert">
               </form>"""
            + "Fahrenheit: " + fahrenheit
    )

#route decorator has been removed
def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degress."""
    try:
        fahrenheit = float(celsius) * 9/5 +32
        fahrenheit = round(fahrenheit,3) # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "Invalid Input"


if __name__ == "__main__":
    app.run("127.0.0.1",port=8080,debug=True)