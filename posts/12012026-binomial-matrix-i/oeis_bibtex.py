"""
Generate BibTeX @misc entries for OEIS sequences.

This script queries the OEIS JSON API for a list of OEIS sequence IDs
and writes a BibTeX file containing one entry per sequence, suitable
for use with LaTeX/BibTeX.
"""

import requests
import os
from datetime import datetime

# Map numeric months to BibTeX-style abbreviations
BIBTEX_MONTHS = {
    1: "jan", 2: "feb", 3: "mar", 4: "apr",
    5: "may", 6: "jun", 7: "jul", 8: "aug",
    9: "sep", 10: "oct", 11: "nov", 12: "dec"
}

def oeis_to_bibtex(oeis_id):
    """
    Fetch OEIS metadata for a given sequence ID and
    return a BibTeX @misc entry as a string.
    """
    url = f"https://oeis.org/search?q={oeis_id}&fmt=json"

    # Perform HTTP request with basic error handling
    r = requests.get(url, timeout=10, headers={"User-Agent": "oeis-bibtex/1.0"})
    r.raise_for_status()

    data = r.json()
    entry = data[0]

    # Clean title (BibTeX does not like raw newlines or quotes)
    title = entry.get("name", "").replace("\n", " ").replace('"', "'")

    # Take first listed author; fall back if missing
    author_raw = entry.get("author", "OEIS Foundation")
    author = author_raw.replace("_", "").split(",")[0]

    # Parse creation date (ISO-8601 format)
    created_raw = entry.get("created")
    try:
        created = datetime.fromisoformat(created_raw)
        year = created.year
        month = BIBTEX_MONTHS[created.month]
        day = created.day
    except Exception:
        # Fallback if date is missing or malformed
        year = "????"
        month = None
        day = None

    # Build BibTeX entry
    bibtex = f"""@misc{{OEIS_{oeis_id},
  author = {{{author}}},
  title = {{{title}}},
  howpublished = {{\\url{{https://oeis.org/{oeis_id}}}}},
  note = {{The On-Line Encyclopedia of Integer Sequences (OEIS)}},
  year = {{{year}}}"""

    # Month/day are optional in BibTeX styles
    if month:
        bibtex += f",\n  month = {{{month}}}"
    if day:
        bibtex += f",\n  day = {{{day}}}"

    bibtex += "\n}"

    return bibtex


# List of OEIS sequences to export
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

# Generate BibTeX entries
entries = [oeis_to_bibtex(i) for i in oeis_ids]
entries = [e for e in entries if e]

# Output directory
path = os.path.join("posts", "12012026-binomial-matrix-i")
os.makedirs(path, exist_ok=True)

# Write .bib file
file = os.path.join(path, "oeis_references.bib")
with open(file, "w", encoding="utf-8") as f:
    f.write("\n\n".join(entries))

print("OK →", os.path.abspath(file))
