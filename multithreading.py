import threading

def clc_squure(numbers):
    for n in numbers:
        print("The square is: ", n*n)
def clc_cube(numbers):
    for n in numbers:
        print("The cube is: ", n*n*n)


arr = [1,2,3,4,5]

t1 = threading.Thread(target=clc_squure, args=(arr,))
t2 = threading.Thread(target=clc_cube, args=(arr,))
t1.start()
t2.start()

t1.join() # Join means is wait for finish the first thread and then execute second one
t2.join()

#clc_squure(arr)
#clc_cube(arr)