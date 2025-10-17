# ---------------------------------------------------------
# Wild Rydes Flask Web App
# Developer: Ravi Kiran Koti
# Student ID: 101002870
# ---------------------------------------------------------

# 1️⃣ Import Flask library (this runs your web app)
from flask import Flask

# 2️⃣ Create the Flask application object
app = Flask(__name__)

# 3️⃣ Define what happens when someone visits the main page
@app.route('/')
def home():
    return '''
        <html>
        <head>
            <title>Wild Rydes – DevOps App</title>
        </head>
        <body style="font-family:Arial; background-color:#fafafa; text-align:center; margin-top:60px;">
            <h1>🐎 Welcome to Wild Rydes!</h1>
            <h3>Cloud DevOps Pipeline Demo</h3>
            <p><b>Developer:</b> Ravi Kiran Koti</p>
            <p><b>Student ID:</b> 101002870</p>
            <p><b>Region:</b> Canada Central (ca-central-1)</p>
            <p><b>Repository:</b> wildrydes-repo</p>
            <hr style="width:40%; margin:30px auto;">
            <p><i>Deployed on AWS ECS using GitHub Actions CI/CD</i></p>
        </body>
        </html>
    '''

# 4️⃣ Tell Python to start the web server on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
