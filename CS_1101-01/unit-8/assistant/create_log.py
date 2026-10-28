# A function to create user daily log
def create_log():
    # Import needed libraries
    from datetime import datetime
    import os

    # Format date & time
    today = datetime.now()
    date = today.strftime("%Y-%m-%d")
    day = today.strftime('%a %b %d')
    year = today.strftime('%Y')
    time = today.time().strftime('%H:%M:%S')

    # Use try-except to capture the case of error
    try:
        path = os.path.join(f"{date}", "user_logs")
        # Check if path exists else create
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"{path} created successfully!")
        file = os.path.join(path, f"{day} {year} | activity.log")
        with open(file, 'a') as file:
                file.write(f"Logged-in. ({date} [{time}])\n")
    except OSError as Error:
        print(f"Filesystem error: {Error}")
    else:
        print(f"New activity log recorded on {date} at [{time}] to '{path}' successfully.")

create_log()
