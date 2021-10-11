arr = []

with open ("nyc_weather.csv",'r') as f:
    for line in f:
        tokens = line.split(',')
        try:
            temperature = int(tokens[1])
            arr.append(temperature)
        except:
            print('invalid temperature.ignore the row')
arr
sum(arr[0:7]) / len(arr[0:7])
max(arr[0:10])



weather_dict ={}

with open("nyc_weather.csv",'r') as f:
    for line in f:
        tokens = line.split(',')
        day =tokens[0]
        try:
            temperature = int(tokens[1])
            weather_dict[day] = temperature
        except:
            print('Invalid temperature.ignore the row')

weather_dict
weather_dict['jan 9']
weather_dict['jan 4']


