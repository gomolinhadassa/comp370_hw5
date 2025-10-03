#!/usr/bin/env python3

import argparse
import csv
from datetime import datetime
from collections import defaultdict

# parse command line arguments
def parse_args():
    parser = argparse.ArgumentParser(
        description="Count complaint types per borough in a given date range."
    )
    parser.add_argument("-i", "--input", required=True, help="Input CSV file")
    parser.add_argument("-s", "--start", required=True, help="Start date (YYYY-MM-DD)")
    parser.add_argument("-e", "--end", required=True, help="End date (YYYY-MM-DD)")
    parser.add_argument("-o", "--output", help="Optional output CSV file")
    return parser.parse_args()

def main():
    args = parse_args()

    # convert start and end dates to datetime
    start_date = datetime.strptime(args.start, "%Y-%m-%d")
    end_date = datetime.strptime(args.end, "%Y-%m-%d")

    # dictionary to store counts like: (complaint_type, borough) -> count
    counts = defaultdict(int)

    # open and read csv
    with open(args.input, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                # parse the created date
                created_date = datetime.strptime(row["Created Date"], "%m/%d/%Y %I:%M:%S %p")
            except Exception:
                continue  # skip bad rows

            # check if in range
            if start_date <= created_date <= end_date:
                complaint = row["Complaint Type"]
                borough = row["Borough"]
                counts[(complaint, borough)] += 1

    # prepare results as a list of rows
    results = [("complaint type", "borough", "count")]
    for (complaint, borough), c in counts.items():
        results.append((complaint, borough, c))

    # output to file if -o given, else print
    if args.output:
        with open(args.output, "w", newline="", encoding="utf-8") as out:
            writer = csv.writer(out)
            writer.writerows(results)
    else:
        for row in results:
            print(",".join(map(str, row)))

if __name__ == "__main__":
    main()