import matplotlib.pyplot as plt
steps = [6000, 7000, 8900, 10700, 3460, 11520, 5155]
labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
num_bars = len(steps)
positions = range(1, num_bars+1)
plt.bar(positions, steps, align='center')

plt.xticks(positions, labels)
plt.xlabel('Day')
plt.ylabel('Steps')
plt.title('Number of steps walked')

plt.grid()
plt.show()
