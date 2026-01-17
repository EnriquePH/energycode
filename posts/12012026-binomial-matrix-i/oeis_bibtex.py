import requests
import os
from datetime import datetime

def oeis_to_bibtex(oeis_id):
    url = f"https://oeis.org/search?q={oeis_id}&fmt=json"
    r = requests.get(url)
    r.raise_for_status()

    data = r.json()

    if not isinstance(data, list) or len(data) == 0:
        print(f"No data for {oeis_id}")
        return None

    entry = data[0]

    title = entry["name"].replace("\n", " ").replace('"', "'")
    year = datetime.now().year

    return f"""@misc{{OEIS_{oeis_id},
  author = {{N. J. A. Sloane and The OEIS Foundation Inc.}},
  title = {{{title}}},
  howpublished = {{\\url{{https://oeis.org/{oeis_id}}}}},
  year = {{{year}}}
}}"""

oeis_ids = [
    "A000027",
    "A000096",
    "A062748",
    "A063258",
    "A062988",
    "A124089",
    "A124090",
    "A165618",
    "A035927"
]

entries = [oeis_to_bibtex(i) for i in oeis_ids]
entries = [e for e in entries if e]

path = os.path.join("posts", "12012026-binomial-matrix-i")
os.makedirs(path, exist_ok=True)

file = os.path.join(path, "oeis_references.bib")

with open(file, "w", encoding="utf-8") as f:
    f.write("\n\n".join(entries))

print("OK →", os.path.abspath(file))


