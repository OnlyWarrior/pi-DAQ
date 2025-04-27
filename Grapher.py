import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

ser = serial.Serial('COM8', 9600, timeout=1)

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

weight = ser.readline()

while len(weight) < 1:
    weight = ser.readline()

wt = []
t = []

datafile = open("Setup", "w")


def animate(i):
    w = abs(float(ser.readline().decode())/10)
    wt.append(w)
    t.append(len(wt))
    datafile.write(str(w) + ",")
    ax1.clear()
    ax1.plot(t, wt)


ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()
