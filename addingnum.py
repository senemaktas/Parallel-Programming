#!/usr/bin/python

import numpy
from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

a = 1
b = 1000000

perrank = b//size
summ = numpy.zeros(1)

comm.Barrier()
start_time = time.time()

temp = 0
for i in range(a + rank*perrank, a + (rank+1)*perrank):
    temp = temp + i

summ[0] = temp

if rank == 0:
    total = numpy.zeros(1)
else:
    total = None

comm.Barrier()
#collect the partial results and add to the total sum
comm.Reduce(summ, total, op=MPI.SUM, root=0)

stop_time = time.time()

if rank == 0:
    #add the rest numbers to 1 000 000
    for i in range(a + (size)*perrank, b+1):
        total[0] = total[0] + i
    print ("The sum of numbers from 1 to 1 000 000: ", int(total[0]))
    print ("time spent with ", size, " threads in milliseconds")
    print ("-----", int((time.time()-start_time)*1000), "-----")