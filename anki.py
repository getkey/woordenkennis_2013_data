#!/usr/bin/env python3

import argparse
import requests
from bs4 import BeautifulSoup

API_BASE_URL = "https://en.wiktionary.org/api/rest_v1/page/definition/"
HEADERS = {
    "accept": 'application/json; charset=utf-8; profile="https://www.mediawiki.org/wiki/Specs/definition/0.8.0"'
}

def clean_html(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    return soup.get_text(separator=" ", strip=True)

def fetch_definitions(spelling):
    url = f"{API_BASE_URL}{spelling}?redirect=false"
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            return ([], [])

        data = response.json()
        if "nl" not in data:
            return ([], [])

        definitions = []
        tags = []
        for entry in data["nl"]:
            if "partOfSpeech" in entry:
                tags.append(entry["partOfSpeech"])

            defs = entry.get("definitions", [])

            for d in defs:
                raw_def = d.get("definition", "").strip()
                clean_def = clean_html(raw_def).strip()
                if clean_def:
                    definitions.append(clean_def)

        return (definitions, tags)

    except Exception as e:
        print(f"Error fetching {spelling}: {e}")
        return ([], [])

def main():
    parser = argparse.ArgumentParser(description="Filter a TSV file and query Wiktionary API for definitions.")
    parser.add_argument("input_file", help="Path to the input TSV file")
    parser.add_argument("output_file", help="Path to the output TSV file")
    args = parser.parse_args()

    with open(args.input_file, "r", encoding="utf-8") as infile, open(args.output_file, "w", encoding="utf-8") as outfile:
        next(infile)  # Skip header line

        for line in infile:
            parts = line.strip().split("\t")
            if len(parts) != 5:
                continue

            spelling, bel_str, ned_str, obs_bel_str, obs_ned_str = parts

            try:
                perc_ned = float(ned_str.replace(",", "."))
                obs_bel = int(obs_bel_str)
            except ValueError:
                continue

            if obs_bel >= 200 and perc_ned >= 99.7:
                (definitions, tags) = fetch_definitions(spelling)

                if definitions:
                    definition_text = ", ".join(definitions)
                    tag_text = ", ".join(tags)
                    outfile.write(f"{spelling}\t{definition_text}\t{tag_text}\n")
                    print(f"✓ {spelling} → {len(definitions)} defs")
                else:
                    print(f"✗ {spelling} → No definitions found")

if __name__ == "__main__":
    main()
