#!/bin/bash

SBATCH --account=project_2000924
SBATCH --partition=gpu
SBATCH --time=00:15:00
SBATCH --ntasks=1
SBATCH --cpus-per-task=10
SBATCH --mem-per-cpu=1000
SBATCH --gres=gpu:v100:1

module load pytorch/1.6
module load pandas

srun python3 /users/student104/advanced_deep_learning/main_ff_adaml1.py --lr 1e-2 --epochs 60
