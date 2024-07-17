"""takes a state abbrev and returns the state's senators"""

import json

with open("legislators-current.json", "r", encoding="utf-8") as f:
    json_content = f.read()

legislators = json.loads(json_content)
senators = [x for x in legislators if x["terms"][-1]["type"] == "sen"]
senators_dict = {}
for senator in senators:
    name = f"{senator["name"]["first"]} {senator["name"]["last"]}"
    if senator["terms"][-1]["state"] not in senators_dict:
        senators_dict[senator["terms"][-1]["state"]] = []
    senators_dict[senator["terms"][-1]["state"]].append(name)

with open("../states_to_sens.json", "w", encoding="utf-8") as out_file:
    json.dump(senators_dict, out_file)
