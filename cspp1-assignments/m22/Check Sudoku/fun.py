import numpy as np
a= [[8, 4, 5, 6, 3, 2, 1, 2, 9],
[7, 3, 2, 9, 1, 8, 6, 5, 4],
[1, 9, 6, 7, 4, 5, 3, 2, 8],
[6, 8, 3, 5, 7, 4, 9, 1, 2],
[4, 5, 7, 2, 9, 1, 8, 3, 6],
[2, 1, 9, 8, 6, 3, 5, 4, 7],
[3, 6, 1, 4, 2, 9, 7, 8 ,5],
[5, 7, 4, 1, 8, 6, 2, 9, 3],
[9, 2, 8, 3, 5, 7, 4, 6, 1]]

trans = zip(*a)
for row in trans:
	print(row)
#print(trans)
new = np.array(a)
t = new[0].reshape((3,3))
print(t)
u = new[1].reshape((3,3))
v = new[2].reshape((3,3))
print(u)
new = np.array([])
final = np.concatenate((t[0],u[0],v[0]))
final2 = np.concatenate((t[1],u[1],v[1]))
final3 = np.concatenate((t[2],u[2],v[2]))
print(final)
print(final2)
print(final3)
print(len(set(final3)) == 9)