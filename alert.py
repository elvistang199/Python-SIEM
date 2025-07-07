def check_alerts(logs):
    fail_count = 0
    for log in logs:
        if log["event_type"] == "LOGIN_FAIL":
            fail_count += 1
    
    if fail_count >= 2:
        print("ALERT: Multiple failed login attempts detected!")
