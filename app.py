from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from sql_parser import parse_create_table
app = Flask(__name__)
CORS(app)
@app.route('/get-mermaid',methods=['GET','POST'])
def mermaid():
    if request.method == "POST":
        query = request.json.get('input')
        if(query):
            mermaid_repr = parse_create_table(query)
            res = {'result':mermaid_repr}
            return jsonify(res)
    else:
        return render_template('sql_mermaid.html')
if __name__ == "__main__":
    app.run(port=5000)