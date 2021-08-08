import random,math,timeit,numpy,statistics
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")

start = timeit.default_timer()

rate = [0]*90
a = [0]*90
n = 2000                                       #no. of draws
N = 10000                                        #no. of sample
hits = [0]*N
pop = []

for i in range(75):
    rate[i] = 0.006

for i in range(74,90):
    rate[i] = 1/3

for k in range(N):
    x = 0
    j = 0
    while j < n:
        for i in range(90):
            a[i] = random.uniform(0,1)

        for i in range(90):
            if a[i] <= rate[i] or i == 89:
                x += 1
                j += 1
                pop.append(i+1)
                break
            j += 1
            if j == n:
                break
    hits[k] = x

hits.sort()
print("number of hits", statistics.mean(hits))
print(hits)

plt.hist(hits, bins=range(hits[N-1]+1),density='true',align='left',color='skyblue',ec='blue')
plt.title("Distribution of amount of 5 stars in " + str(n) + "draws, with a sample size of " + str(N))
plt.xlim(min(hits)-1,max(hits))
plt.xlabel("No. of 5 stars")
plt.ylabel("Percentage of players")

#pop.sort()

#plt.hist(pop, bins=range(91))
#plt.xticks(numpy.arange(0, 91, 5))


stop = timeit.default_timer()
print('Time: ', stop - start)

plt.grid(axis='y')
plt.show()