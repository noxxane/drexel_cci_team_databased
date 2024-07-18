"""statistical analysis for united states presidential elections"""

import pathlib
import graphs


def turnout_graph():
    """graph for turnout in united states presidential elections from 1789 to 2020"""
    in_path = pathlib.Path(
        "../stats/United States presidential election voter turnout - Sheet1.csv"
    )
    out_path = pathlib.Path("us_turnout_graph.png")
    graphs.turnout_graph(in_path, out_path)


turnout_graph()
