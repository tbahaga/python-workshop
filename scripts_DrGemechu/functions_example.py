# coding: utf-8
def add_together(a, b, c):
    return a + b + c
    
add=add_together(3,4,-1)
add
get_ipython().run_line_magic('save', 'functions_example.py 1-3')
get_ipython().run_line_magic('pwd', '')
def f(exp):
    return 2**exp 
    
for i in range(0,25):
    print(f(i))
    
