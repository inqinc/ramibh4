#!/bin/bash

#BATCH -o testing%j.out
#SBATCH -e testing%j.err 
#SBATCH -N 4
#SBATCH -p allgpu-noecc
#SBATCH -J ramimidterm
#SBATCH -t 00:0:10
#SBATCH --mail-type=ALL
#SBATCH --mail-user=ramibh4@gwu.edu
             
module load python
module load openmpi/gcc/64/1.8
mpirun -N 4 -B 16 ./midterm.py
