import multiprocessing

def clc_squure(numbers):
    for n in numbers:
        print("The square is: ", n*n)
def clc_cube(numbers):
    for n in numbers:
        print("The cube is: ", n*n*n)

if __name__ == "__main__":
	arr = [1,2,3,4,5]

	p1 = multiprocessing.Process(target=clc_squure, args=(arr,))
	p2 = multiprocessing.Process(target=clc_cube, args=(arr,))
	p1.start()
	p2.start()

	p1.join() # Join means is wait for finish the first thread and then execute second one
	p2.join()

