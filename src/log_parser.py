# src/log_parser.py
import re

def parse_log(file_path):
    with open(file_path, 'r') as file:
        logs = file.readlines()

    parsed_logs = []
    for log in logs:
        match = re.match(r'(\d+-\d+-\d+ \d+:\d+:\d+\.\d+) - (Request) - (\d+\.\d+\.\d+\.\d+) - Method: (\w+), URL: (.*), Headers: (.*), Form Data: (.*), JSON Payload: (.*)', log)
        if match:
            timestamp, log_type, ip, method, url, headers, form_data, json_payload = match.groups()
            parsed_logs.append({
                'timestamp': timestamp,
                'type': log_type,
                'ip': ip,
                'method': method,
                'url': url,
                'headers': headers,
                'form_data': form_data,
                'json_payload': json_payload
            })
    return parsed_logs