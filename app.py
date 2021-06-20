from flask import Flask, request, render_template
from password_generator import Password_Generator
import string

# the flask app
app = Flask(__name__)
generator = Password_Generator()
chars = string.ascii_letters + string.digits
chars_special = chars + string.punctuation

current_password = generator.generate_password(15, chars_special)
first_load = True

#index page
@app.route("/", methods=["GET","POST"])
def index():

    return render_template("index.html", password=current_password)

#generate password        
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

#check entropy
@app.route("/check", methods=["POST"])
def check_entropy():
    password = request.form["pass-entropy"]
    entropy = generator.calc_entropy(password)
    print(entropy)
    entropy = round(entropy)

    return str(entropy)

if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)