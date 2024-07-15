""" program to find rep(s) from zip using the house website. caches them for
use in the teenformation (temp name) website. authored by frank furtschool """

import json
import sys
from bs4 import BeautifulSoup
import pandas as pd
import requests

ZIP_FILE = "zips_to_reps.json"


def get_rep_from_zip(user_zip_code: str) -> tuple[str, str] | str:
    """scrapes the house website for the user's rep"""
    link = f"https://ziplook.house.gov/htbin/findrep_house?ZIP={user_zip_code}"
    text = requests.get(link, timeout=10).text
    soup = BeautifulSoup(text, "html.parser")
    rep_div = soup.find_all("div", {"id": "RepInfo"})
    if len(rep_div) == 0:
        reps = soup.find_all("div", {"class": "RepInfo"})
        reps = list(map(lambda x: x.text, reps))
        reps = list(map(lambda x: x.strip(), "".join(reps).splitlines()))
        reps = list(filter(lambda x: len(x) != 0, reps))
        rep_1 = ", ".join(reps[:3])
        rep_2 = ", ".join(reps[3:6])
        return rep_1, rep_2
    user_rep = list(map(lambda x: x.text, rep_div))
    user_rep = list(map(lambda x: x.strip(), user_rep))
    user_rep = ", ".join(list(map(lambda x: x.strip(), "".join(user_rep).splitlines())))
    return user_rep


def print_reps(user_zip_code: str):
    """prints reps from get_rep_from_zip"""
    rep = get_rep_from_zip(user_zip_code)
    if rep is tuple:
        print(f"Your representatives are {rep[0]} and {rep[1]}")
    else:
        print(f"Your representative is {rep}")


def fix_no_leading_zero_zip(user_zip_code: str):
    """some of the zips have no leading zeroes, making their lengths below 5.
    the house website only accepts zips with length 5 or above, so we just pad
    zeroes until the zip is length 5."""
    return user_zip_code.rjust(5, "0")


def fix_no_leading_zero_zips(zip_list):
    """fixes all the zips in a given list"""
    for x in zip_list:
        fix_no_leading_zero_zip(x)
    return zip_list


def filter_for_area_name_zips(zip_df, area_name):
    """filters for zips with the provided area name"""
    return zip_df[zip_df["AREA NAME"] == area_name]


def filter_for_district_name_zips(zip_df, district_name):
    """filters for zips with the provided district name"""
    return zip_df[zip_df["DISTRICT NAME"] == district_name]


def filter_for_city(zip_df, physical_city):
    """filters for zips with the provided city"""
    return zip_df[zip_df["PHYSICAL CITY"] == physical_city]


def zip_codes_to_dict():
    """caches reps from zip codes"""
    file = "/home/nox/Downloads/zips.csv"
    df = pd.read_csv(file)
    df = df[["AREA NAME", "DISTRICT NAME", "PHYSICAL ZIP", "PHYSICAL CITY"]]
    # filtered_df = filter_for_area_name_zips(df, "ATLANTIC")
    filtered_df = filter_for_district_name_zips(df, "DE-PA 2")
    # filtered_df = filter_for_city(df, "PHILADELPHIA")
    filtered_zips = fix_no_leading_zero_zips(
        list(map(lambda x: str(int(x)), filtered_df["PHYSICAL ZIP"].tolist()))
    )
    with open(ZIP_FILE, "r", encoding="utf-8") as f:
        existing_zips = json.load(f)
        existing_keys = existing_zips.keys()
    filtered_zips = list(filter(lambda x: x not in existing_keys, filtered_zips))
    if len(filtered_zips) <= len(existing_zips):
        # hacky asf solution, not entirely sure who designed json, but they should be drawn and
        # quartered for what they have done to my (formerly) immaculate code
        sys.exit(0)
    zips_dict = {}

    total_zips = len(filtered_zips)
    current_zip = 0
    for filtered_zip in filtered_zips:
        zips_dict[filtered_zip] = get_rep_from_zip(filtered_zip)
        print(f"zips remaining: {total_zips - current_zip}")
        current_zip += 1
    print("done getting reps")
    return zips_dict


def cache_zips_as_json(zips_dict):
    """caches zips dict into a json"""
    with open("zips_to_reps.json", "w", encoding="utf-8") as f:
        json.dump(zips_dict, f)
    print("done writing json")


if __name__ == "__main__":
    gen_zips_dict = zip_codes_to_dict()
    cache_zips_as_json(gen_zips_dict)
