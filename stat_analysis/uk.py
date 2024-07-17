"""statistical analysis for several united kingdom general elections"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def turnout_graph():
    """graph for turnout in united kingdom general elections from 1918 to 2024"""
    df = pd.read_csv(
        "../stats/United Kingdom general election voter turnout - Sheet1.csv"
    )
    x_list = df["Year"].tolist()
    y_list = list(map(lambda x: float(x[:-1]), df["Turnout"].tolist()))
    fixed_df = pd.DataFrame({"Year": x_list, "Turnout": y_list})

    sns.set_theme()

    sns.lineplot(data=fixed_df, x="Year", y="Turnout")

    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig("uk_turnout_graph.png")
    plt.close()


def twenty_fifteen_graph():
    """graph for votes per mp in the 2015 united kingdom general election"""
    df = pd.read_csv("../stats/2015 United Kingdom general election - Sheet1.csv")
    vote_list = df["Votes"].tolist()
    mps_list = df["MPs"].tolist()
    votes_per_mp_list = []
    for vote, mps in zip(vote_list, mps_list):
        votes_per_mp_list.append(vote / mps)
    dfl = pd.DataFrame(
        {"Party": df["Party"].tolist(), "Votes per MP": votes_per_mp_list}
    )

    sns.set_theme()

    sns.lineplot(data=dfl, x="Party", y="Votes per MP")

    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig("uk_twenty_fifteen_votes_per_mp.png")
    plt.close()


def twenty_twenty_four_graph():
    """graph for votes per mp in the 2024 united kingdom general election"""
    df = pd.read_csv("../stats/2024 United Kingdom general election - Sheet1.csv")
    vote_list = df["Votes"].tolist()
    mps_list = df["MPs"].tolist()
    votes_per_mp_list = []
    for vote, mps in zip(vote_list, mps_list):
        votes_per_mp_list.append(vote / mps)
    dfl = pd.DataFrame(
        {"Party": df["Party"].tolist(), "Votes per MP": votes_per_mp_list}
    )

    sns.set_theme()

    sns.lineplot(data=dfl, x="Party", y="Votes per MP")

    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig("uk_twenty_twenty_four_votes_per_mp.png")
    plt.close()


turnout_graph()
twenty_fifteen_graph()
twenty_twenty_four_graph()
