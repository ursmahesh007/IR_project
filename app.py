from flask import Flask,jsonify, render_template, request
from elasticsearch import Elasticsearch, RequestsHttpConnection
import warnings
warnings.filterwarnings("ignore")
app = Flask(__name__)
host = 'https://tux-es1.cci.drexel.edu:9200/ms4976_info624_201904_articles/'
es = Elasticsearch(hosts=host,verify_certs=False,http_auth='ms4976:Phooh3ahkei7',connection_class=RequestsHttpConnection,)

@app.route('/')
def home():
    return render_template('search.html')

@app.route('/search', methods=['GET', 'POST'])
def search_request():
    search_term = request.form["keywords"]
    res = es.search(body={"query":{"match" :{"abstract" :{"query" : search_term}}}})
    return jsonify(res['hits']['hits'])

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host='localhost', port=8000)
