from mpi4py import MPI 
import numpy 

comm = MPI.COMM_WORLD 
rank = comm. Get_rank()

if rank == 0: 
	data = {'a': 1, 'b': 2} 
	comm.send(data, dest=1)
elif rank == 1: 
	data = comm. recv(source=0)
	print('Data received by process 1 is: ', data)
