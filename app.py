from flask import Flask, render_template
from numpy.core.numeric import nan
import pandas as pd
import numpy as np

app = Flask(__name__)


@app.route("/")
def index():
    df = pd.read_csv(f"analyze_data/top_3_lecture.csv", encoding="utf-8")
    python_df = df[df.subject == "파이썬"]
    java_df = df[df.subject == "자바"]
    c_df = df[df.subject == "C언어"]

    python_dict = python_df.to_dict("list")
    java_dict = java_df.to_dict("list")
    c_dict = c_df.to_dict("list")
    for index in range(3):
        title = c_dict["title"][index]
        c_dict["title"][index] = title.replace("[c언어]", "")
        title = python_dict["title"][index]
        python_dict["title"][index] = title.replace("[파이썬]", "")
        title = java_dict["title"][index]
        java_dict["title"][index] = title.replace("[자바]", "")

    return render_template(
        "main.html", python_dict=python_dict, java_dict=java_dict, c_dict=c_dict
    )


if __name__ == "__main__":
    app.run(debug=True, port=8089)

