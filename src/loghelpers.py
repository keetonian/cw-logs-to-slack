"""Collection of functions to deal with CloudWatch logs."""
import base64
import gzip
import json


def extract_log_events(event):
    """Decode and decompress log data."""
    log_data = event['awslogs']['data']
    compressed_data = base64.b64decode(log_data)
    decompressed_data = gzip.decompress(compressed_data)
    json_data = json.loads(decompressed_data)
    log_events = json_data['logEvents']
    return log_events
