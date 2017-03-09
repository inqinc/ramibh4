
m mpi4py import MPI

comm = MPI.COMM.WORLD
size = comm.Get_size()
rank = comm.Get_rank()
stat = comm.Get_status()

if rank == 0:
	array = [x**2 for x in range(1,257)]
	comm.scatter(array, root = 0)
	comm.barrier(
		comm.gather(sum, tag=MPI.ANY_TAG)
		comm.reduce(sum, op=MPI.SUM, root=0)
		print sum)

elif rank == 1:
	sum = comm.recv(source=0, tag=MPI.ANY_TAG)
	sum = 0
	for x in range((len(array)/size):
		sum = sum+x
		comm.send(sum, dest = 0, tag = 1)

elif rank == 2:
	sum = comm.recv(source=0, tag=MPI.ANY_TAG)
	for x in range((len(array)/size):
		sum = sum+x
		comm.send(sum, dest = 0, tag = 2)
elif rank == 3:
	sum = comm.recv(source=0, tag=MPI.ANY_TAG)
	sum = 0
	for x in range((len(array)/size):
		sum = sum+x
		comm.send(sum, dest = 0, tag = 3)
elif rank ==4:
	sum = comm.recv(source=0, tag=MPI.ANY_TAG)
	sum = 0
	for x in range((len(array)/size):
		sum = sum+x
		comm.send(sum, dest = 0, tag = 4)
