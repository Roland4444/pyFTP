import pickle
class A:
    mem1 = 1
    mem2 = 2

class B(A):
    c=A()

exem = B()
print("DUMPED ! =)")
with open('entry.pickle', 'wb') as f:
   pickle.dump(exem,  f)

with open('entry.pickle', 'rb') as f:
   entry = pickle.load(f)

print(entry.c.mem1)