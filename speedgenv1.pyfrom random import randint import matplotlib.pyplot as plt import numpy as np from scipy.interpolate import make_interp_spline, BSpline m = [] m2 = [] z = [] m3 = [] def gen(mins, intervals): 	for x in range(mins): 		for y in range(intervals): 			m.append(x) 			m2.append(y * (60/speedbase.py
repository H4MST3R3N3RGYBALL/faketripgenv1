from random import randint
import matplotlib.pyplot as plt
import numpy as np
m = []
m2 = []
z = []
m3 = []
def gen(mins, intervals):
	for x in range(mins):
		for y in range(intervals):
			m.append(x)
			m2.append(y * (60 / intervals))
			k = randint(0, 65)#Just values for base genration
#Fill the redacted with values of your choice in order to choose the base smoothing
			k = k * <REDACTED> + randint(<REDACTED>, <REDACTED>)
			z.append(k)
gen(15, 3)#TOTAL MINUTES / the amount of intervals per a minute
for t in range(len(m)):
	print(str(m[t]) + ':' + str(m2[t]) + ',' + str(z[t]))
	m3.append(m[t] * 60 + m2[t])
f, ax = plt.subplots()
ax.plot(np.array(m3), np.array(z))
ax.set(xlabel='time (s)', ylabel='Speed MPH',
       title='About as simple as it gets, folks')
ax.grid()

plt.show()
