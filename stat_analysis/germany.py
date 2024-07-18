"""statistical analysis for german federal elections"""

import pathlib
import graphs

CSV_PATH = pathlib.Path("../stats/Germany voter turnout - Sheet1.csv")


def turnout_graph():
    """graph for turnout in german federal elections from 1949 to 2021"""
    turnout_img_path = "germany_turnout_graph.png"
    in_path = pathlib.Path(CSV_PATH)
    out_path = pathlib.Path(turnout_img_path)

    graphs.turnout_graph(in_path, out_path)


def turnout_vs_uk_graph():
    """graph for turnout in german federal elections vs united kingdom general elections"""
    uk_csv_path = pathlib.Path(
        "../stats/United Kingdom general election voter turnout - Sheet1.csv"
    )
    ger_vs_uk_img_path = pathlib.Path("ger_vs_uk_turnout.png")
    graphs.vs_graph(
        CSV_PATH, "Germany", uk_csv_path, "United Kingdom", ger_vs_uk_img_path
    )


turnout_graph()
turnout_vs_uk_graph()
