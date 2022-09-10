from requests import get

results = {}

websites = (
    "google.com",
    "https://airbnb.com",
    "twitter.com",
    "https://facebook.com",
    "naver.com",
)

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    if response.status_code == 200:
        results[website] = "SUCCESS"
    else:
        results[website] = "FAILED"

print(results)
