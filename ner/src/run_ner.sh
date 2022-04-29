#!/bin/bash
#SBATCH -J ner
#SBATCH -p gpus
#SBATCH -n 1
#SBATCH -c 4
#SBATCH --gres=gpu:1
#SBATCH -o ner_%j.out
#SBATCH -e ner_%j.err
#SBATCH --mail-user=matirojasga@gmail.com
#SBATCH --mail-type=END,FAIL
#SBATCH --mem-per-cpu=8600
ml CUDA/10.2.89
ml Python/3.7.3
/home/mrojasg/work/falp-ner-code/venv/bin/python main.py