"""margin of victory for united states presidential elections"""

import pathlib
from bs4 import BeautifulSoup
import pandas as pd
import requests

DAT_FILE_PATH = pathlib.Path("mov.dat")


def get_margin_of_victory(given_election_year: int):
    """gets the margin of victory for a given election year"""
    html = requests.get(
        "https://www.archives.gov/electoral-college/" + str(given_election_year),
        timeout=5,
    ).text
    soup = BeautifulSoup(html, "html.parser")

    winner_electoral_votes = int(
        list(filter(lambda x: "Winner" in x.get_text(), soup.find_all("td")))[0]
        .get_text()
        .split(":")[-1]
        .split(",")[0]
        .replace("(", "")
        .replace(")", "")
        .replace("*", "")
        .strip()
    )

    loser_electoral_votes = int(
        list(filter(lambda x: "Main Opponent" in x.get_text(), soup.find_all("td")))[0]
        .get_text()
        .split(":")[-1]
        .split(",")[0]
        .replace("(", "")
        .replace(")", "")
        .replace("*", "")
        .strip()
    )

    margin_of_victory = winner_electoral_votes - loser_electoral_votes

    if DAT_FILE_PATH.exists():
        with open(DAT_FILE_PATH, "a", encoding="utf-8") as out:
            out.write(str(given_election_year) + ": " + str(margin_of_victory) + "\n")
    else:
        with open(DAT_FILE_PATH, "w", encoding="utf-8") as out:
            out.write(str(given_election_year) + ": " + str(margin_of_victory) + "\n")


if __name__ == "__main__":
    # if DAT_FILE_PATH.exists():
    #     DAT_FILE_PATH.unlink()
    election_year_list = [1789, 1792]
    while 2020 not in election_year_list:
        election_year_list.append(election_year_list[-1] + 4)
    # 1872 was invented by the devil (horace greeley died before the meeting of
    # the electors, meaning that he received 0 electoral votes)
    election_year_list.remove(1872)

    for election_year in election_year_list:
        print("getting mov for", election_year)

        get_margin_of_victory(election_year)
    year_to_mov_dict = {}
    with open(DAT_FILE_PATH, "r", encoding="utf-8") as f:
        text = f.read()
        for line in text.splitlines():
            key = line.split(":")[0].strip()
            value = line.split(":")[-1].strip()
            year_to_mov_dict[key] = value

    df = pd.read_csv(
        "../stats/United States presidential election voter turnout - Sheet1.csv"
    )
    df.insert(2, "Margin of Victory", pd.Series(year_to_mov_dict.values()))
    print(df)
