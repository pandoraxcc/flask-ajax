from flask import Flask
from flask import render_template
from flask import request
from flask import json

from data import squirrels, fruits

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def home():

    if request.method == 'GET':

        return render_template('index.html')
    
    if request.method == 'POST':

        query = request.get_data().decode()
        matches = ""
        num_elements = 0

        for s1, s2 in zip(squirrels, fruits):

            if query in s1:

                matches += s1 + ", "
                num_elements += 1

            if query in s2:

                matches += s2 + ","
                num_elements += 1


        if matches:

            if num_elements >1:

                matches = matches[:-2]

            if num_elements == 1:
                
                matches = matches[:-1]


            composed_response = matches.encode()

            return composed_response

        else:
            return None

if __name__ == "__main__":
    app.run(debug=True)