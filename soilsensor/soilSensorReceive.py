import matplotlib.pyplot as plt
import paho.mqtt.subscribe as subscribe


data = []
i = 0
plt.ion()
while True:
    reading = subscribe.simple("agbot/soilsensor", hostname="192.168.65.230", port=1883)
    value = int(reading.payload.decode().rstrip())
    if len(data) <= 100:
        data.append(value)
    else:
        data[i] = value
    i = (i+1)%100
    plt.plot(data)
    plt.draw()
    plt.pause(0.1)
    plt.clf()
