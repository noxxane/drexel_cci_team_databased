"""statistical analysis of elections"""

import pathlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def read_and_fix_percentages(in_path: pathlib.Path) -> pd.DataFrame:
    """reads the given csv and removes percentage signs allowing conversions to floats and
     therefore graphing"""
    df = pd.read_csv(in_path)
    x_list = df["Year"].tolist()
    y_list = list(map(lambda x: float(x[:-1]), df["Turnout"].tolist()))
    fixed_df = pd.DataFrame({"Year": x_list, "Turnout": y_list})
    return fixed_df


def turnout_graph(in_path: pathlib.Path, out_path: pathlib.Path):
    """graphs turnout from a csv file containing election turnout"""
    df = read_and_fix_percentages(in_path)

    sns.set_theme()

    sns.lineplot(data=df, x="Year", y="Turnout")

    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def vs_graph(
    first_path: pathlib.Path,
    first_country: str,
    second_path: pathlib.Path,
    second_country: str,
    out_path: pathlib.Path,
):
    """compares two turnout graphs"""
    first_df = read_and_fix_percentages(first_path)
    second_df = read_and_fix_percentages(second_path)

    first_df.insert(2, "Country", first_country)
    second_df.insert(2, "Country", second_country)

    combined_df = pd.concat([first_df, second_df])

    sns.set_theme()

    sns.lineplot(data=combined_df, x="Year", y="Turnout", hue="Country")

    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()
