""" program to find rep(s) from zip using the house website. caches them for
use in the teenformation (temp name) website. authored by frank furtschool """

import json
import pathlib
from bs4 import BeautifulSoup
import pandas as pd
import requests

ZIP_FILE = "./stats/zips.csv"


def get_rep_from_zip(user_zip_code: str) -> tuple[str, str] | str:
    """scrapes the house website for the user's rep"""
    link: str = f"https://ziplook.house.gov/htbin/findrep_house?ZIP={user_zip_code}"
    text: str = requests.get(link, timeout=10).text
    soup: BeautifulSoup = BeautifulSoup(text, "html.parser")
    rep_div: list[BeautifulSoup] = soup.find_all("div", {"id": "RepInfo"})
    if len(rep_div) == 0:
        reps: list[BeautifulSoup] = soup.find_all("div", {"class": "RepInfo"})
        reps_text: list[str] = list(map(lambda x: x.text, reps))
        reps_text: list[str] = list(
            map(lambda x: x.strip(), "".join(reps_text).splitlines())
        )
        reps_text: list[str] = list(filter(lambda x: len(x) != 0, reps_text))
        rep_1: str = ", ".join(reps_text[:3])
        rep_2: str = ", ".join(reps_text[3:6])
        return rep_1, rep_2
    user_rep: list[str] = list(map(lambda x: x.text, rep_div))
    user_rep: list[str] = list(map(lambda x: x.strip(), user_rep))
    user_rep_string: str = ", ".join(
        list(map(lambda x: x.strip(), "".join(user_rep).splitlines()))
    )
    return user_rep_string


def print_reps(user_zip_code: str):
    """prints reps from get_rep_from_zip"""
    rep = get_rep_from_zip(user_zip_code)
    if rep is tuple[str, str]:
        print(f"Your representatives are {rep[0]} and {rep[1]}")
    else:
        print(f"Your representative is {rep}")


def fix_no_leading_zero_zip(user_zip_code: str):
    """some of the zips have no leading zeroes, making their lengths below 5.
    the house website only accepts zips with length 5 or above, so we just pad
    zeroes until the zip is length 5."""
    return user_zip_code.rjust(5, "0")


def fix_no_leading_zero_zips(zip_list: list[str]):
    """fixes all the zips in a given list"""
    for x in zip_list:
        fix_no_leading_zero_zip(x)
    return zip_list


def filter_df(
    zip_df: pd.DataFrame, filter_column: str, filter_var: str
) -> pd.DataFrame:
    """filters a df"""
    return pd.DataFrame(zip_df[zip_df[filter_column] == filter_var])


def zip_codes_to_dict():
    """caches reps from zip codes"""
    zip_csv_path: pathlib.Path = pathlib.Path("/home/nox/Downloads/zips.csv")
    df: pd.DataFrame = pd.read_csv(zip_csv_path)
    df: pd.DataFrame = pd.DataFrame(
        df[["AREA NAME", "DISTRICT NAME", "PHYSICAL ZIP", "PHYSICAL CITY"]]
    )
    filtered_df: pd.DataFrame = filter_df(df, "DISTRICT NAME", "DE-PA 2")
    filtered_zips: list[str] = fix_no_leading_zero_zips(
        list(map(lambda x: str(int(x)), filtered_df["PHYSICAL ZIP"].unique().tolist()))
    )
    zips_dict = {}
    with open(ZIP_FILE, "r", encoding="utf-8") as f:
        existing_zips = json.load(f)
        existing_keys: list[str] = existing_zips.keys()
    for key_zip in filtered_zips:
        if key_zip in existing_keys:
            zips_dict[key_zip] = existing_zips[key_zip]
            while key_zip in filtered_zips:
                filtered_zips.remove(key_zip)

    total_zips = len(filtered_zips)
    current_zip = 0
    for filtered_zip in filtered_zips:
        zips_dict[filtered_zip] = get_rep_from_zip(filtered_zip)
        print(f"zips remaining: {total_zips - current_zip}")
        current_zip += 1
    print("done getting reps")
    return zips_dict


def cache_zips_as_json(zips_dict: dict[str, str]):
    """caches zips dict into a json"""
    with open("zips_to_reps.json", "w", encoding="utf-8") as f:
        json.dump(zips_dict, f)
    print("done writing json")


if __name__ == "__main__":
    gen_zips_dict = zip_codes_to_dict()
    cache_zips_as_json(gen_zips_dict)
