import json
from pathlib import Path
import pytest

REPORT_PATH = Path("/app/report.json")

@pytest.fixture(scope="module")
def report():
    assert REPORT_PATH.exists(), "report.json not found at /app/report.json"
    content = REPORT_PATH.read_text()
    assert content.strip(), "report.json is empty"
    return json.loads(content)

def test_report_is_valid_json(report):
    assert isinstance(report, dict), "report.json must be a JSON object"

def test_total_requests(report):
    assert "total_requests" in report, "report.json missing key 'total_requests'"
    assert report["total_requests"] == 6, f"Expected total_requests=6, got {report['total_requests']}"

def test_unique_ips(report):
    assert "unique_ips" in report, "report.json missing key 'unique_ips'"
    assert report["unique_ips"] == 3, f"Expected unique_ips=3, got {report['unique_ips']}"

def test_top_path(report):
    assert "top_path" in report, "report.json missing key 'top_path'"
    assert report["top_path"] == "/index.html", f"Expected top_path='/index.html', got {report['top_path']!r}"
