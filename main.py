import time
import random
from datetime import datetime
import pytz
import matplotlib.pyplot as plt
import pandas as pd

# Set IST timezone
ist = pytz.timezone("Asia/Kolkata")

actions = ["used someother application", "used AI for classwork", "attends class", "submitted assignment"]

log_stream = []

for i in range(15):  # simulate 15 events
    user = "User{random.randint(100,999)}"
    action = random.choice(actions)
    timestamp = datetime.now(ist)
    duration = random.randint(5, 60)  # minutes spent

    log_stream.append({"timestamp": timestamp, "user": user, "action": action, "duration": duration})
    print(f"[{timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {user} → {action} ({duration} minutes)")
    time.sleep(1)

# Convert to DataFrame
df = pd.DataFrame(log_stream)

# Trend: total time spent per action
trend = df.groupby('action')['duration'].sum()

print("\n=== Trend Analysis ===")
for action, total in trend.items():
    print(f"- More time was spent on {action}: {total} minutes")

# Find activity with max time
max_action = trend.idxmax()
print(f"\nResult: '{max_action}' consumed the most time ({trend[max_action]} minutes).")

# Visualization: Bar Chart
plt.figure(figsize=(8,5))
plt.bar(trend.index, trend.values, color='purple')
plt.title(" Time Spent per Activity ")
plt.xlabel("Activity")
plt.ylabel("Minutes")
plt.xticks(rotation=30)
plt.show()
