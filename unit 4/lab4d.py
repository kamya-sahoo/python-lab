import json

data = [
    {
        "timestamp": "10:00",
        "level": "INFO",
        "message": "Application started"
    },
    {
        "timestamp": "10:05",
        "level": "WARNING",
        "message": "Low memory"
    },
    {
        "timestamp": "10:10",
        "level": "ERROR",
        "message": "Database connection failed"
    },
    {
        "timestamp": "10:15",
        "level": "INFO",
        "message": "User logged in"
    },
    {
        "timestamp": "10:20",
        "level": "ERROR",
        "message": "File not found"
    }
]

# Create JSON file

with open("logs.json", "w") as file:
    json.dump(data, file, indent=4)

try:

    # Read JSON file

    with open("logs.json", "r") as file:
        logs = json.load(file)

    info_count = 0
    warning_count = 0
    error_count = 0

    print("----- APPLICATION LOG RECORDS -----")

    for log in logs:

        print("\nTimestamp:", log["timestamp"])
        print("Level:", log["level"])
        print("Message:", log["message"])

        if log["level"] == "INFO":
            info_count += 1

        elif log["level"] == "WARNING":
            warning_count += 1

        elif log["level"] == "ERROR":
            error_count += 1

    print("\n----- LOG SUMMARY -----")

    print("Total INFO messages:", info_count)
    print("Total WARNING messages:", warning_count)
    print("Total ERROR messages:", error_count)

except FileNotFoundError:
    print("Error: logs.json file not found!")

except json.JSONDecodeError:
    print("Error: Invalid JSON data!")