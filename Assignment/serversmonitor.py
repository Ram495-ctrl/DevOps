import psutil
import time


def monitor_cpu(threshold=80):
    print("Monitoring CPU usage...")

    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            
            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")

            time.sleep(5)
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
 
 
if __name__== "__main__":
    monitor_cpu()
    
