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
    python_dict = python_df.to_dict("list")
    java_dict = java_df.to_dict("list")

    return render_template(
        "main.html", python_dict=python_dict, java_dict=java_dict
    )


if __name__ == "__main__":
    app.run(debug=True, port=8089)
