import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def turnout_graph():
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


def twentyfifteen_graph():
    df = pd.read_csv("../stats/2015 United Kingdom general election - Sheet1.csv")
    vote_list = df["Votes"].tolist()
    mps_list = df["MPs"].tolist()
    votes_per_mp_list = []
    for vote, mps in zip(vote_list, mps_list):
        votes_per_mp_list.append(vote / mps)
    dfl = pd.DataFrame({"Party": df["Party"].tolist(), "Votes per MP": votes_per_mp_list})

    sns.set_theme()

    sns.lineplot(data=dfl, x="Party", y="Votes per MP")

    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


twentyfifteen_graph()
