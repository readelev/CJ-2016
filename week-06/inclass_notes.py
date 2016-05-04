import matplotlib.pyplot as plt


# takes two sequences

xvals = [0, 1, 2, 3]
yvals = [23, 48, 65, 80]
plt.plot(xvals, yvals)

# other fun things
plt.savefit('whatever.png')
plt.close()
plt.bar(xvals, yvals)
plt.scatter(xvals, yvals, color="red")
ply.close()

# for examples...
fig, ax = plt.subplots()
ax.pie([12,32])