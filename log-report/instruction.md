There is an Apache-style access log at `/app/access.log`.

Analyse it and write a summary to `/app/report.json` as a JSON object with **exactly** these three keys:

- `total_requests` — integer: total number of log lines (one per request)
- `unique_ips` — integer: number of distinct client IP addresses
- `top_path` — string: the URL path that appears most frequently across all requests

**Success criteria:**
1. `/app/report.json` exists and contains a valid JSON object.
2. `total_requests` is the correct integer count of all requests in the log.
3. `unique_ips` is the correct integer count of distinct client IP addresses.
4. `top_path` is the string path with the highest request count.
