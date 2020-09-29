import numpy as np
def gradient_descent(x,y):
    m_curr=b_curr=0
    ite=1000
    n=len(x)
    lr=0.01
    for i in range(ite):
        y_predi=m_curr*x+b_curr
        md=-(2/n)*sum(x*(y-y_predi))
        bd=-(2/n)*sum(y-y_predi)
        m_curr=m_curr-lr*md
        b_curr=b_curr-lr*bd
        print("m{ }, b{ }, ite{ }".format(m_curr,b_curr,i))
        
x=np.array([1,2,3,4,5])
y=np.array([5,7,9,11,13])
gradient_descent(x,y)