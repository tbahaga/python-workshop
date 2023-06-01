#!/bin/bash
#PBS -l nodes=1:ppn=12
#PBS -l walltime=01:00:00
#PBS -A RegCM_Sens
#PBS -M gemechufanta@gmail.com 
#PBS -o RegCM_test	
module load openmpi/3.0.1/gnu/4.8.5 
module load netcdf/4.4.0/gnu/4.8.5

#You may need to login
cd /scratch/gemechuf/REGCM/
#Run the job
mpirun -np 4 ./bin/regcmMPI Ethiopian_domain.in

