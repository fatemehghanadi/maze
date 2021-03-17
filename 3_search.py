import emoji

class node:
  father=0
  def __init__(self, x, y , h):
    self.x = int(x)
    self.y = int(y)
    self.h = bool(h)
    self.d = 0
    if h: self.emj=':seedling:'
    if not h:self.emj=':cactus:'
  def child(self):
        c = set()
        if self.x + 1 <= 19 and self.x + 1 >= 0 and t[self.x + 1][self.y].h:
            c.add(t[self.x + 1][self.y])
        if self.x - 1 <= 19 and self.x - 1 >= 0 and t[self.x - 1][self.y].h:
            c.add(t[self.x - 1][self.y])
        if self.y - 1 <= 19 and self.y - 1 >= 0 and t[self.x][self.y - 1].h:
            c.add(t[self.x][self.y - 1])
        if self.y + 1 <= 19 and self.y + 1 >= 0 and t[self.x][self.y + 1].h:
            c.add(t[self.x][self.y + 1])
        return c

  def hur(self):
      return abs(self.x-ne.x) + abs(self.y-ne.y)

t=[[node(0,0,True) for i in range(0,20)] for j in range(0,20)]
for i in range (0,20):
    for j in range (0,20):
        t[i][j]=(node(i,j,True))

cntr = 0
while (cntr < 200):
    bx, by = input("black node x, y | end end : ").split()
    if bx=="end" and by=="end":
        break
    else:
        t[int(bx)][int(by)]=node(bx,by,False)

sx,sy=input("start node x, start node y : ").split()
ex,ey=input("end node x, end node y : ").split()

ns=node(sx,sy,True)
ne=node(ex,ey,True)

print("--------ITTERATIVE DEPTH FIRST--------")
frt1=[ns]
exp1=[]
original_depth=int(input("DEPTH "))
#depth=original_depth
def frt1_exist(nn):

    for i in frt1:
        if i.x==nn.x and i.y==nn.y:return True
    else: return False

def snail_show():
    f=(ne.x,ne.y)
    family = []
    while (True):
        family.append(f)
        if f == (ns.x, ns.y):
            break
        ff = father[f]
        f = ff
    for u in range(0, family.__len__()):
        t[family[u][0]][family[u][1]].emj = ':snail:'
    t[ns.x][ns.y].emj = ':round_pushpin:'
    t[ne.x][ne.y].emj = ':round_pushpin:'
    for iii in range(19,-1,-1):
        for jjj in range(0, 20):
            print(emoji.emojize(t[jjj][iii].emj), end='')
        print("\n")
    print("way : ",end='')
    print(family)


def rec(nod):
  global ex_cost
  if (nod.x==ne.x) and (nod.y==ne.y):
      exp1.append((nod.x,nod.y))
      print("successful in depth : ",nod.d)
      snail_show()
      return 1
  else:
    if (nod.x, nod.y) not in exp1:
      exp1.append((nod.x, nod.y))
    if frt1.__len__()>=0 and nod.d<depth:
            if nod==ns:
                frt1.pop()
            for ch in nod.child():
                if ((ch.x,ch.y) not in exp1) and (not frt1_exist(ch)):
                    ch.d = nod.d + 1
                    frt1.append(ch)
                    ch_c=(ch.x,ch.y)
                    nod_c=(nod.x,nod.y)
                    father[ch_c]=nod_c

            if frt1.__len__()==0:
                ##print("cutoffff---76")
                return 0
            b=frt1.pop()
            if (b.x,b.y) not in exp1:
                if rec(b): return 1


    elif frt1.__len__()>0 and depth==nod.d:

                b = frt1.pop()
                if (b.x, b.y) not in exp1:
                    if rec(b)==1:return 1
                    else :return 0


    else :
        ##print("cutofffffff")
        ex_cost=ex_cost+exp1.__len__()
        return 0


trace=False
ex_cost=0
for ddd in range(1,original_depth+1):
    depth=ddd
    frt1=[ns]
    exp1=[]
    father = dict()

    if rec(ns)==1:
        trace=True

        print ("total explored size : "+str(ex_cost))
        break

if not trace:
    print("---itterative dfs search cutoff---")

for i in range (0,20):
    for j in range (0,20):
        if t[i][j].emj==':snail:':
            t[i][j].emj = ':seedling:'

exp=[]
def h_min(n):
    a=dict()
    for ch in n.child():
        if ch not in exp and ch.h:
          a[int(ch.hur())]=ch
    if a.__len__()!=0:
        #cnt_bast= cnt_bast+1
        nn=a[min(a.keys())]
        nn.father=n
        return nn
    else: return -1

def a_star():
    cnt_bast = 0
    print("_______ A * _______")
    print("way : ", end='')
    cnt = 0
    nod=ns
    while (nod.x!=ne.x) or (nod.y!=ne.y):
        cnt=cnt+1
        t[nod.x][nod.y].emj=':snail:'
        print((nod.x,nod.y),end='')
        exp.append(nod)
        if h_min(nod)!=-1:
            cnt_bast=cnt_bast+1
            nod=h_min(nod)
        else:
            print("backkk"+str((nod.x,nod.y)),end='')
            nod.emj=':seedling:'
            nod=nod.father
    if (nod.x==ne.x) and (nod.y==ne.y):
        print("\n TOTAL COST :  " + str(cnt))
        print(" EXPANDED : " + str(cnt_bast))
        return "succ"

print(a_star())
t[ns.x][ns.y].emj=':round_pushpin:'
t[ne.x][ne.y].emj=':round_pushpin:'
for i in range(19,-1,-1):
    for j in range(0,20):
        print(emoji.emojize(t[j][i].emj),end='')
    print("\n")



for i in range (0,20):
    for j in range (0,20):
        if t[i][j].emj==':snail:':
            t[i][j].emj = ':seedling:'

print("--------BREADTH FIRST SEARCH--------")

def first(ns,ne):
    first_search_cost=0
    frt = []
    exp = []
    frt.append(ns)
    father=dict()
    while(True):
        a=frt.pop(0)

        if (a.x!=ne.x or a.y!=ne.y) and a.h and (a not in exp):
            exp.append(a)
            n=False
            for ch in a.child():
                if ch not in exp and ch.h:
                    n=True
                    if ch not in frt:
                        frt.append(ch)
                        ch_s=(ch.x,ch.y)
                        a_s=(a.x,a.y)
                        father[ch_s]=a_s

            if n: first_search_cost = first_search_cost + 1

        elif a.x==ne.x and a.y==ne.y:

            f=(ne.x,ne.y)
            family=[]
            while(True):
                ff=father[f]
                family.append(f)

                if f==(ns.x,ns.y):
                   ## print(family)
                    break
                f=ff
            for u in range(0,family.__len__()):
                t[family[u][0]][family[u][1]].emj=':snail:'

            t[ns.x][ns.y].emj=':round_pushpin:'
            t[ne.x][ne.y].emj = ':round_pushpin:'
            for iii in range(19,-1,-1):
                for jjj in range(0,20):
                    print(emoji.emojize(t[jjj][iii].emj), end='')
                print("\n")


            return str(family)+"\n"+"search cost : "+str(first_search_cost)+"  explored : "+str(exp.__len__())


ns=node(sx,sy,True)
ne=node(ex,ey,True)
print(first(ns,ne))







