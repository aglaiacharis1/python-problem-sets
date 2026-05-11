def main():
    answer = input("What time is it? ")
  
    time = convert(answer)

    
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    new_hours = float(hours)
    new_minutes = float(minutes)
    new = new_minutes / 60
    return new_hours + new


if __name__ == "__main__":
    main()