import csv


tempatures = []
sum = 0
with open("weather_data.csv", "r", encoding="utf-8") as f:
    data = csv.reader(f, delimiter=',')
    for row in data:
        try:
            temp = int(row[1])
        except ValueError:
            continue
        tempatures.append(temp)
        sum += temp

mean_temp = round(sum / len(tempatures), 2)
print(tempatures)
print(f"Ortalama sıcaklık: {mean_temp}")

