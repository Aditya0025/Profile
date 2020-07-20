from flask import Flask,render_template
 

app = Flask(__name__)

@app.route("/")
def Profile():
    return render_template('Profile.html') 


if __name__ == '__main__':    
    app.run(debug=True) 