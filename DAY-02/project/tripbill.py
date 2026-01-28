
def personal_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def trip_bills(**kwargs):
    total = 0
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        total += value
    print("Total:", total)
