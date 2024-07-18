"""statistical analysis for new zealand general elections"""

import pathlib
import graphs


def turnout_graph():
    """graph for turnout in new zealand general elections from 1879 to 2023"""
    in_path = pathlib.Path("../stats/New Zealand voter turnout - Sheet1.csv")
    out_path = pathlib.Path("nz_turnout_graph.png")

    graphs.turnout_graph(in_path, out_path)
