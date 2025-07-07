def parse_logs(logs):
    parsed = []
    for log in logs:
        parts = log.strip().split(" - ")
        if len(parts) == 3:
            timestamp, event_type, description = parts
            parsed.append({
                "timestamp": timestamp,
                "event_type": event_type,
                "description": description
            })
    return parsed
