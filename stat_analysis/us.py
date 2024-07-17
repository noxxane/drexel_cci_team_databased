"""statistical analysis for united states presidential elections"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def turnout_graph():
    df = pd.read_csv("../stats/United States presidential election voter turnout - Sheet1.csv")
    x_list = df["Year"].tolist()
    y_list = list(map(lambda x: float(x[:-1]), df["Turnout"].tolist()))
    fixed_df = pd.DataFrame({"Year": x_list, "Turnout": y_list})

    sns.set_theme()

    sns.lineplot(data=fixed_df, x="Year", y="Turnout")

    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig("us_turnout_graph.png")
    plt.close()


turnout_graph()
