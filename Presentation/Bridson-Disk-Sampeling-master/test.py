import timeit
import matplotlib.pyplot as plt
from simple_dskSmp import poisson_disc_samples


width = 1200
height = 700 

min_distance = 9
radious = 2

start = timeit.timeit()
res = [[], []]
# width,height,radious
for i in range (13):
    k = 5  * (1 + i)
    start = timeit.timeit()
    points = poisson_disc_samples(width,height , min_distance, k)
    end = timeit.timeit()
    time = end - start
    if time > 0:
        res[0].append(k)
        res[1].append(time)

plt.plot(res[0],res[1])
plt.show()