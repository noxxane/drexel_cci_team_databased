"""statistical analysis for several united kingdom general elections"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import graphs
import pathlib


def turnout_graph():
    """graph for turnout in united kingdom general elections from 1918 to 2024"""
    in_path = pathlib.Path("../stats/United Kingdom general election voter turnout - Sheet1.csv")
    out_path = pathlib.Path("uk_turnout_graph.png")
    graphs.turnout_graph(in_path, out_path)


def votes_per_mp(election_df: pd.DataFrame) -> pd.DataFrame:
    """takes a dataframe with united kingdom general election data and outputs the votes each
    party got per elected mp"""
    vote_list = election_df["Votes"].tolist()
    mps_list = election_df["MPs"].tolist()
    votes_per_mp_list = []
    for vote, mps in zip(vote_list, mps_list):
        votes_per_mp_list.append(vote / mps)
    dfl = pd.DataFrame(
        {"Party": election_df["Party"].tolist(), "Votes per MP": votes_per_mp_list}
    )

    return dfl


def twenty_fifteen_graph():
    """graph for votes per mp in the 2015 united kingdom general election"""
    df = pd.read_csv("../stats/2015 United Kingdom general election - Sheet1.csv")
    dfl = votes_per_mp(df)

    sns.set_theme()

    sns.lineplot(data=dfl, x="Party", y="Votes per MP")

    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig("uk_twenty_fifteen_votes_per_mp.png")
    plt.close()


def twenty_twenty_four_graph():
    """graph for votes per mp in the 2024 united kingdom general election"""
    df = pd.read_csv("../stats/2024 United Kingdom general election - Sheet1.csv")
    dfl = votes_per_mp(df)

    sns.set_theme()

    sns.lineplot(data=dfl, x="Party", y="Votes per MP")

    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig("uk_twenty_twenty_four_votes_per_mp.png")
    plt.close()


def uk_vs_germany():
    """graph comparing general election turnout in the united kingdom to federal election turnout in germany"""
    first_path = pathlib.Path("../stats/United Kingdom general election voter turnout - Sheet1.csv")
    first_country = "United Kingdom"
    second_path = pathlib.Path("../stats/Germany voter turnout - Sheet1.csv")
    second_country = "Germany"
    out_path = pathlib.Path("uk_vs_germany_turnout.png")

    graphs.vs_graph(first_path, first_country, second_path, second_country, out_path)


turnout_graph()
twenty_fifteen_graph()
twenty_twenty_four_graph()
uk_vs_germany()
