from flask import Flask, request
from dbService import fetchData

app = Flask(__name__)

# Query Params
@app.route("/fetchData", methods=["GET"])
def hello() :
    id = request.args.get('id')
    print(id)
    return fetchData(id)

# Path Params
# @app.route("/fetchData/<id>", methods=["GET"])
# def hello(id) :
#     print(id)
#     return fetchData(id)


if __name__ == "__main__" :
    app.run(port=5000, host="0.0.0.0", debug=True)

