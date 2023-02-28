import json

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/data')
def test_data():
    print(request.args)
    print(request.headers)
    return "success"


@app.route("/uesr_template")
def uesr_Template():
    datas = [(1, "name1"), (2, "name2"), (3, "name3")]
    title = "学生信息"
    return render_template("ues_template.html", datas=datas, title=title)


def read_pvuv_data():
    data = []
    with open("./data/pvuv.txt") as fin:
        is_first_line = True
        for line in fin:
            if is_first_line:
                is_first_line = False
                continue
            line = line[:-1]
            pdate, pv, uv = line.split("\t")
            data.append((pdate, pv, uv))
    return data


@app.route("/pvuv")
def pvuv():
    data = read_pvuv_data()
    return render_template("pvuv.html", data=data)


@app.route('/getjson')
def getjson():
    data = read_pvuv_data()
    return json.dumps(data)


if __name__ == '__main__':
    app.run()
