from flask import Flask, Response, render_template, request, render_template
import json
from country_list import countries_for_language

app = Flask(__name__)


@app.route('/auto', methods=['GET', 'POST'])
def autocomplete():
    countries = dict(countries_for_language('en'))
    country = ['Unites States Of America', 'India', 'Australia', 'China', 'Japan']
    key = request.args.get('term')
    print(key)
    results = []
    if key:
        coun = countries.get((key.replace("'", '')).upper())
        print(coun)
        if coun:
            results.append(coun)
        else:
            results = country
    else:
        results = country
    return Response(json.dumps(results), mimetype='application/json')


@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
