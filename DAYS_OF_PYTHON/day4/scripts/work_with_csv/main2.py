tempatures = []
sum = 0

with open("weather_data.csv", "r", encoding="utf-8") as f:
    data = f.readlines()
    for row in data:
        row = row.split(",")
        try:
            temp = int(row[1])
        except ValueError:
            continue
        tempatures.append(temp)
        sum += temp

mean_temp = round(sum / len(tempatures), 2)
print(tempatures)
print(f"Ortalama sıcaklık: {mean_temp}")
