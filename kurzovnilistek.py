import requests
import json
from dateutil import parser  #dobra knihovna na datumy
from flask import Flask, Response

url = "http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"
def download_rates():
    response= requests.get(url)
    if not response.ok:
        return{}
    lines = response.text.split("\n")
    date = parser.parse(lines[0].split("#")[0].strip())

    data = {
        "datum": date.strftime("%Y-%n-%d"),
        "kurzy": []
    }

    keys = [k for k in lines[1].split("|")]

    for line in lines[2:]:
        if not line:
            continue

        values = [v for v in line.split("|")]
        data["kurzy"].append(dict(zip(keys, values)))

    return data

data = json.dumps(download_rates())
app = Flask(__name__)

@app.route("/")
def kurzy():
    return Response(data, mimetype="application/json")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

   # data = download_rates()
   # print(json.dumps(data, indent=4, ensure_ascii=False))