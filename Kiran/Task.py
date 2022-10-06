
import requests

page_number = 1
records = []

# total_pages - 5
for i in range (1,6):
    response = requests.get(f"https://jsonmock.hackerrank.com/api/articles?page={page_number}")
    response = response.json()
    records.extend(response["data"])
    page_number += 1

sorted_records = sorted(records, key=lambda x: x["num_comments"] if x["num_comments"] else 0, reverse=True)

print("Top two titles with most number of comments: \n")

for rec in sorted_records[0:2]:
    print(rec["title"] + " - " +  str(rec["num_comments"]))
