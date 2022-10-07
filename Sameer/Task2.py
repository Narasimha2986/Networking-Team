import requests

page_count = 1
records = []

# total pages - 2

def sort_by_submission_counts(rec):
    if rec.get("submission_count"):
        return rec.get("submission_count")
    return -1

while page_count < 3:
    response = requests.get(f"https://jsonmock.hackerrank.com/api/article_users?page={page_count}")
    response = response.json()
    records.extend(response["data"])
    page_count += 1

sorted_records = sorted(records, key=sort_by_submission_counts, reverse=True)



print("Top two users with most number of submissions")
print("*********************************************")
for rec in sorted_records[0:2]:
    print(rec["username"] + "-" +  str(rec["submission_count"]))
