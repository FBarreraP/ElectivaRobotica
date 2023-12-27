import time

t1 = time.time()
t2 = 0.0
while t2 <= 20.0:
    print("El tiempo es %f s \n" %t2)
    t2 = time.time() - t1