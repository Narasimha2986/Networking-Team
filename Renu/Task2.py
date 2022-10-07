page_count = 1
records = []

# total pages - 2

while page_count < 3:
    response = requests.get(f"https://jsonmock.hackerrank.com/api/article_users?page={page_count}")
    response = response.json()
    records.extend(response["data"])
    page_count += 1

sorted_records = sorted(records, key=lambda x: x["submission_count"] if x["submission_count"] else -1, reverse=True)



print("Top two users with most number of submissions")
print("*********************************************")
for rec in sorted_records[0:2]:
    print(rec["username"] + "-" +  str(rec["submission_count"]))
