#!/usr/bin/env python 

##Solution May 20

def function_one():
	f=open("sites_simple.csv",'r')
	return(f)

def function_two():
    f = function_one()
    line_list = []
    for line in f:     
		line_list.append((line).strip().split(','))
    return(line_list)

def function_three():
    line_obj = function_two()
    with open('out.txt', 'w') as out_file:
        for line in line_obj:
            out_file.write(str(line) + '\n')

function_three()

