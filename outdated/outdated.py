months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()
    if "/" in date:
        try:
            mm, dd, yy = date.split("/")

            mm = int(mm)
            dd = int(dd)
            yy = int(yy)

            if 1 <= int(mm) <= 12 and 1 <= int(dd) <= 31:
                break
        except ValueError:
            pass

    elif "," in date:
        try:
            date = date.replace(",", "")
            months_str, day_str, year_str = date.split(" ")
            if months_str in months:
                mm = months.index(months_str) + 1
                dd = int(day_str)
                yy = int(year_str)
                if 1 <= dd <= 31:
                    break
        except (ValueError, IndexError):
            pass

        
print(f"{yy}-{mm:02}-{dd:02}")