from threading import Thread
from generator import simulate_logs
from monitor import monitor_logs

def run_siem():
    print("Starting Python SIEM with real-time monitoring...\n")
    
    generator_thread = Thread(target=simulate_logs, daemon=True)
    monitor_thread = Thread(target=monitor_logs, daemon=True)

    generator_thread.start()
    monitor_thread.start()

    # Keep the main thread alive
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nSIEM stopped by user.")

if __name__ == "__main__":
    run_siem()
