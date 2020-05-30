import os.system
p=''
pp=[]
with open("a.J") as f:
    i=f.readlines():
    for w in i:
        pp.append(w.count(' '))
    k=0
    while k<len(pp):
        u=pp[k]
        v=pp[k+1]
        m=pp[k+2]
        n=pp[k+3]
        k+=4
        p+=chr(int(hex((u-1)*4 + v)[2:]+hex((m-1)*4+n),16))
with open("J.py","w+") as f3:
    f3.writelines(p)
            
        
        