time = input("What time is it? :")
hours, minutes = time.split(":")
time = int(hours) + int(minutes)/60
if 7<= time <=8 :
    print("breakfast time")
elif 12 <= time <= 13:
    print("lunch time")
elif 18 <= time <= 19:
    print("dinner time")