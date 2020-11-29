#!/bin/bash




#python3 /users/sahin/advanced_deep_learning/main_ff.py --epochs 15 > output.txt
#python3 /users/sahin/advanced_deep_learning/main_ff_adam.py --epochs 15 --lr 1e-3 > adam.txt
python3 /users/sahin/advanced_deep_learning/main_ff_adam.py --epochs 15 --lr 1e-1 > adam1.txt
python3 /users/sahin/advanced_deep_learning/main_ff_adam.py --epochs 15 --lr 1e-2 > adam2.txt
python3 /users/sahin/advanced_deep_learning/main_ff_adam.py --epochs 15 --lr 1e-4 > adam4.txt
