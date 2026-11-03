# Website Uptime Checker


import time
import urllib.request
from urllib.error import URLError

SITES = ["https://www.python.org", "https://www.wikipedia.org"]


def check(url: str, timeout: float = 5.0) -> tuple[bool, float, str]:
    """Return (is_up, response_time_seconds, status_or_error)."""
    start = time.perf_counter()
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            return True, time.perf_counter() - start, str(resp.status)
    except (URLError, TimeoutError) as exc:
        return False, time.perf_counter() - start, str(exc)


if __name__ == "__main__":
    for site in SITES:
        up, elapsed, info = check(site)
        status = "UP  " if up else "DOWN"
        print(f"{status} {site:<30} {elapsed*1000:7.0f} ms  ({info})")