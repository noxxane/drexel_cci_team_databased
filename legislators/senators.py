"""takes a state abbrev and returns the state's senators"""

import json

with open("legislators-current.json", "r", encoding="utf-8") as f:
    json_content = f.read()

legislators = json.loads(json_content)
senators = [x for x in legislators if x["terms"][-1]["type"] == "sen"]
senators_dict = {}
for senator in senators:
    name_obj = senator["name"]
    first_name = name_obj["first"]
    last_name = name_obj["last"]
    name = f"{first_name} {last_name}"

    most_recent_term = senator["terms"][-1]
    sen_state = most_recent_term["state"]
    if sen_state not in senators_dict:
        senators_dict[sen_state] = []
    senators_dict[sen_state].append(name)

with open("../states_to_sens.json", "w", encoding="utf-8") as out_file:
    json.dump(senators_dict, out_file)
