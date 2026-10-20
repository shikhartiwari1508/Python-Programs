# Check karega ki website accessible hai ya nahi.


import urllib.request
import urllib.error

url = input("Enter website URL: ")

if not url.startswith(("http://", "https://")):
    url = "https://" + url

try:
    request = urllib.request.Request(
        url,
        method="GET",
        headers={"User-Agent": "Python Status Checker"}
    )

    with urllib.request.urlopen(request, timeout=10) as response:
        print("Website is reachable")
        print("Status Code:", response.status)

except urllib.error.HTTPError as error:
    print("Website responded with error:", error.code)

except (urllib.error.URLError, TimeoutError, OSError) as error:
    print("Website is unreachable:", error)
