# Exercises to understand how python works

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]

print "A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5))) results in : ",  A0;
print 'A1 = range(10) results in : ',  A1;
print 'A2 = sorted([i for i in A1 if i in A0]) results in : ',  A2, ' where A0 : ', A0;
print 'A3 = sorted([A0[s] for s in A0]) results in : ',  A3, ' where A0 : ', A0 ;
print 'A4 = [i for i in A1 if i in A3] results in : ',  A4, ' where A1: ', A1,' and A3: ', A3;
print 'A5 = [[i,i*i] for i in A1] results in : ',  A5, ' where A1 : ', A1;
print 'A6 = [[i,i*i] for i in A1] results in : ',  A6, ' where A1 : ', A1;
