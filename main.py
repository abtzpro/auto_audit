import json
import schedule
import time
from audit import Audit

def load_config():
    with open("config.json") as f:
        return json.load(f)

def run_audit():
    try:
        config = load_config()
        audit = Audit(config)
        audit.perform_audit()
        audit.send_notification("Security audit completed", "The security audit has been completed successfully.")
    except Exception as e:
        audit.send_notification("Security audit failed", f"The security audit has failed: {e}")

def main():
    config = load_config()
    schedule.every().day.at(config["audit_schedule"]).do(run_audit)

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
