"""statistical analysis for german federal elections"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def fix_percentages(df: pd.DataFrame) -> pd.DataFrame:
    """removes percentage signs allowing for conversion to floats and therefore graphing"""
    x_list = df["Year"].tolist()
    y_list = list(map(lambda x: float(x[:-1]), df["Turnout"].tolist()))
    fixed_df = pd.DataFrame({"Year": x_list, "Turnout": y_list})
    return fixed_df


def turnout_graph():
    """graph for turnout in german federal elections from 1949 to 2021"""
    df = fix_percentages(pd.read_csv("../stats/Germany voter turnout - Sheet1.csv"))

    sns.set_theme()

    sns.lineplot(data=df, x="Year", y="Turnout")

    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig("germany_turnout_graph.png")
    plt.close()


def turnout_vs_uk_graph():
    """graph for turnout in german federal elections vs united kingdom general elections"""
    germany_df = fix_percentages(
        pd.read_csv("../stats/Germany voter turnout - Sheet1.csv")
    )
    germany_df.insert(2, "Country", "Germany")
    uk_df = fix_percentages(
        pd.read_csv(
            "../stats/United Kingdom general election voter turnout - Sheet1.csv"
        )
    )
    uk_df.insert(2, "Country", "United Kingdom")

    combined_df = pd.concat([germany_df, uk_df])

    sns.set_theme()

    sns.lineplot(data=combined_df, x="Year", y="Turnout", hue="Country")

    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig("germany_vs_uk_turnout_graph.png")
    plt.close()


turnout_graph()
turnout_vs_uk_graph()
