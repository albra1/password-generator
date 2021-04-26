from flask import Flask, request, render_template
from password_generator import Password_Generator
import string

app = Flask(__name__)
generator = Password_Generator()
chars = string.ascii_letters + string.digits
chars_special = chars + string.punctuation

current_password = "**********"

@app.route("/", methods=["POST"])
def index():

    return render_template("index.html", password=current_password)

     

@app.route("/generate", methods=["POST"])
def generate():

    global current_password
    password = ""

    print(request.form)
    length = int(request.form["length"])

    if request.form.get("special-chars") == "special":
        current_password = generator.generate_password(length, chars_special)
        
    else:
        current_password = generator.generate_password(length, chars)
            
    return current_password


if __name__ == "__main__":
    app.run(port=1337, debug=True)