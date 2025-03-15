import requests
from bs4 import BeautifulSoup

forecast= """
    <!DOCTYPE html>
<html>
<head>
    <title>Weather Forecast</title>
</head>
<body>
    <h4>5-Day Weather Forecast</h4>
    <table>
        <thead>
            <tr>
                <th>Day</th>
                <th>Temperature</th>
                <th>Condition</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Monday</td>
                <td>25°C</td>
                <td>Sunny</td>
            </tr>
            <tr>
                <td>Tuesday</td>
                <td>22°C</td>
                <td>Cloudy</td>
            </tr>
            <tr>
                <td>Wednesday</td>
                <td>18°C</td>
                <td>Rainy</td>
            </tr>
            <tr>
                <td>Thursday</td>
                <td>20°C</td>
                <td>Partly Cloudy</td>
            </tr>
            <tr>
                <td>Friday</td>
                <td>30°C</td>
                <td>Sunny</td>
            </tr>
        </tbody>
    </table>

</body>
</html>
"""

soup=BeautifulSoup(forecast, "html.parser")
#displaying data
print(soup.text)

#highest temprature

rows=soup.find('tbody').find_all('tr')
sunny_days= []
day_with_htemp= None
max_temp = float('-inf')
total_temp=0
count=0

for row in rows:
    columns=row.find_all("td")
    days=columns[0].text.strip()
    temp=int(columns[1].text.strip().replace("°C", ""))
    condition = columns[2].text.strip()


    if condition=="Sunny":
        sunny_days.append(days)
    
    if temp>max_temp:
        max_temp=temp
        day_with_htemp=days

    total_temp += temp
    count+=1
avr_temp=total_temp/count

print(f"Sunny days: {sunny_days}")
print(f"Day with highest temprature: {day_with_htemp} with ({max_temp}°C)")
print(f"Average temperature: {avr_temp:.2f}°C")