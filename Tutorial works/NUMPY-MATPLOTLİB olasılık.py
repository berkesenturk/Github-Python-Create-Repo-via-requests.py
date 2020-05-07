

import numpy
import matplotlib.pyplot
import matplotlib
import matplotlib.mlab

m = 0
sigma = 1
x=numpy.random.normal(m,sigma,5000)

matplotlib.pyplot.plot(x,"o")
matplotlib.pyplot.xlabel("smarts")
matplotlib.pyplot.ylabel("PDF")
matplotlib.pyplot.show()

y=numpy.random.normal(m,sigma,50)


matplotlib.pyplot.plot(y,"*",x,"o")
matplotlib.pyplot.xlabel("smarts")
matplotlib.pyplot.ylabel("PDF")

matplotlib.pyplot.show()

num_bins = 5000
num_elli = 50

matplotlib.pyplott.hist(x ,num_bins, histtype="bar", rwidth=1)
matplotlib.pyplot.hist(y,num_elli,histtype="bar", rwidth=1)
matplotlib.pyplot.xlabel("smarts")
matplotlib.pyplot.ylabel("PDF")
matplotlib.pyplot.show()


fig, ax = matplotlib.pyplot.subplots()


n, bins, patches = ax.hist(x, num_bins, normed=1)


y = matplotlib.mlab.normpdf(bins, m, sigma)
ax.plot(bins, y, '--')
ax.set_xlabel('Smarts')
ax.set_ylabel('Probability density')
ax.set_title(r'Histogram of IQ: $\mu=0$, $\sigma=1$')


fig.tight_layout()
matplotlib.pyplot.show()
