import requests

page_number = 1
records = []

# total_pages - 2

for i in rnge (1,3):
    response = requests.get(f"https://jsonmock.hackerrank.com/api/article_users?page={page_count}")
    response = response.json()
    records.extend(response["data"])
    page_number += 1

sorted_records = sorted(records, key=lambda x: x["submission_count"] if x["submission_count"] else -1, reverse=True)



print("Top two users with most number of submissions: \n")

for rec in sorted_records[0:3]:
    print(rec["username"] + "-" +  str(rec["submission_count"]))

