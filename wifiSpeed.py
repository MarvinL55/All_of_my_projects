import speedtest
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Step 1: Collect WiFi Metrics
def collect_wifi_metrics():
    wifi_test = speedtest.Speedtest()
    wifi_test.get_best_server()

    ping = wifi_test.results.ping
    download_speed = wifi_test.download() / 1024 / 1024  # Convert to Mbps
    upload_speed = wifi_test.upload() / 1024 / 1024  # Convert to Mbps

    return ping, download_speed, upload_speed

# Rest of the code remains the same...

# Step 2: Label Data
wifi_status = "good"  # or "laggy"

# Step 3: Data Storage
wifi_data = []  # List to store WiFi metrics
wifi_labels = []  # List to store labels
num_sessions = 10

# Collect data and labels for multiple sessions
for _ in range(num_sessions):
    ping, download_speed, upload_speed = collect_wifi_metrics()
    wifi_data.append([ping, download_speed, upload_speed])
    wifi_labels.append(wifi_status)

# Step 4: Split Data
X_train, X_test, y_train, y_test = train_test_split(wifi_data, wifi_labels, test_size=0.2, random_state=42)

# Step 5: Train a Model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Step 6: Evaluate the Model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)
