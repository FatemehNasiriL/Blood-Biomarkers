
# making bed files for each scenario
# example code for scen 1

import timeit

start = timeit.default_timer()


bed={}
from os import walk


above = next(walk('./above6'), (None, None, []))[2]
below = next(walk('./below6'), (None, None, []))[2]

filenames=above+below
betan=''
for fn in filenames:
    f=open('./1/%s'%fn,'r')
    for a in f:
        cho=a[:a.find('\t')]
        a=a[a.find('\t')+1:]
        st=a[:a.find('\t')]
        a=a[a.find('\t')+1:]
        end=a[:a.find('\t')]
        a=a[a.find('\t')+1:]
        beta=a[:a.find('\t')]
        if cho not in bed:
            bed[cho]={}
            bed[cho][st+'-'+end]=[]
            nn=0
            while len(filenames)>nn:
                nn+=1
                bed[cho][st+'-'+end]+=['NA']
            bed[cho][st+'-'+end][filenames.index(fn)]=beta
        elif st+'-'+end not in bed[cho]:
            bed[cho][st+'-'+end]=[]
            nn=0
            while len(filenames)>nn:
                nn+=1
                bed[cho][st+'-'+end]+=['NA']
            bed[cho][st+'-'+end][filenames.index(fn)]=beta
        else:
            bed[cho][st+'-'+end][filenames.index(fn)]=beta
above = next(walk('./above6'), (None, None, []))[2]
for q in above:
    filenames[filenames.index(q)]='above6'
below = next(walk('./below6'), (None, None, []))[2]
for rt in below: 
    filenames[filenames.index(rt)]='below6' 
for t in filenames:
    betan+='%s\t'%t
m=open('merge.bed','w')
m.write('chr\tst\tend\t'+betan+'\n')

for x in bed:
    for p in bed[x]:
        betaarray=''
        for b in bed[x][p]:
            betaarray+='%s\t'%b
        m.write('%s\t%s\t%s\t'%(x,p[:p.find('-')],p[p.find('-')+1:])+betaarray+'\n')
stop = timeit.default_timer()

print('Time: ', stop - start)