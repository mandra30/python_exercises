class A(object):
   def go(self):
       print("go A go!")
   def stop(self):
       print("stop A stop!")
   def pause(self):
       raise Exception("Not Implemented")

class B(A):
   def go(self):
       super(B, self).go()
       print("go B go!")

class C(A):
   def go(self):
       super(C, self).go()
       print("go C go!")
   def stop(self):
       super(C, self).stop()
       print("stop C stop!")

class D(B,C):
   def go(self):
       super(D, self).go()
       print("go D go!")
   def stop(self):
       super(D, self).stop()
       print("stop D stop!")
   def pause(self):
       print("wait D wait!")

class E(B,C):
    def pause(self):
        try:
            super(B,self).pause()
        except Exception as e:
            print e

a = A()
b = B()
c = C()
d = D()
e = E()

a.go()
#a.pause()
a.stop()

b.go()
b.stop()
#b.pause()

c.go()
c.stop()
#c.pause()

d.go()
d.stop()
d.pause()

e.go()
e.stop()
e.pause()
