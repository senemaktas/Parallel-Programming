''' Every process receives the data from the earlier process. This goes on till the end and 
wraps aroun 1 , so that the first process receives the data from the last process.
Dynamically received data'''

from mpi4py import MPI
import sys

comm=MPI.COMM_WORLD 
rank=comm.rank
size=comm.size

#returns the hostname on which the current process is running.
name=MPI.Get_processor_name()

shared=(rank+1)*(rank+1)
comm.send(shared,dest=(rank+1)%size)
data=comm.recv(source=(rank-1)%size)

#the process with rank 0 (the first process) receive the data from the process with rank 3 (the last process)
sys.stdout.write("Name:%s\n" %name)
sys.stdout.write("Rank:%s\n" %rank)
sys.stdout.write("Data:%s\n come from rank= %d\n"%(data,(rank-1)%size))

