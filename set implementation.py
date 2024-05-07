class set:
    def __init__(self):
        self.lst=[]
    
    def add(self,element):
        self.lst.append(element)
    
    def contains(self, element):
        for i in self.lst:
            if(i==element):
                return i
        return False
        
    def remove(self, element):
        present=self.contains(element)
        if(present):
            c=0
            for i in self.lst:
                if(i==element):
                    a=self.lst.pop(c)
                c+=1
            return a
        else:
            return False
        
    def size(self):
        return len(self.lst)
    
    def iterator(self):
        for i in self.lst:
            print(i)
    
    def intersection(self,set2):
        set3=set()
        for i in self.lst:
            for j in set2.lst:
                if(i==j):
                    set3.add(i)
        return set3
    
    def union(self,set2):
        set3=set()
        for i in self.lst:
            set3.add(i)
        for i in set2.lst:
            if(i not in set3.lst):
                set3.add(i)
        return set3
    
    def difference(self,set2):
        set3=set()
        for i in self.lst:
            if(i not in set2.lst):
                set3.add(i)
        return set3
    
    def subset(self,set2):
        for i in set2.lst:
            if(i not in self.lst):
                return False
        return True
    
    def input2(self):
        setA=set()
        setB=set()
        l1=int(input("Please enter size of set A: "))
        for i in range(l1):
            x=int(input("Please enter element"+str(i+1)+": "))
            setA.add(x)
        print(setA.lst)
        l2=int(input("Please enter size of set B: "))
        for i in range(l2):
            x=int(input("Please enter element"+str(i+1)+": "))
            setB.add(x)
        print(setB.lst)
        return setA,setB

#main_program
set1=set()
while(True):
    print("-----MENU----")
    print("1.Add an element")
    print("2.Check if set contains an element")
    print("3.Remove an element")
    print("4.Size of set")
    print("5.Iterate set")
    print("6.Perform intersection")
    print("7.Perform union")
    print("8.Perform difference")
    print("9.Check subset")
    print("10.Exit")
    ch=int(input("Please enter your choice of action: "))
    
    if(ch==1):
        x=int(input("Please enter the element to be inserted: "))
        set1.add(x)
        print("Element added successfully")
        
    elif(ch==2):
        x=int(input("Please enter the element to be checked: "))
        if(set1.contains(x)):
            print("Yes, the given element is present in the set.")
        else:
            print("No, the given element is not present in the set.")
        
    elif(ch==3):
        x=int(input("Please enter the element to be removed."))
        a=set1.remove(x)
        if(a):
            print(a,"is deleted from set.")
        else:
            print(x,"is not present in set.")
        
    elif(ch==4):
        size=set1.size()
        print("Size of set is",size)
    
    elif(ch==5):
        set1.iterator()
    
    elif(ch==6):
        setA,setB=set1.input2()
        setC=setA.intersection(setB)
        setC.iterator()
    
    elif(ch==7):
        setA,setB=set1.input2()
        setC=setA.union(setB)
        setC.iterator()
    
    elif(ch==8):
        setA,setB=set1.input2()
        setC=setA.difference(setB)
        setC.iterator()
    
    elif(ch==9):
        setA,setB=set1.input2()
        if(setA.subset(setB)):
            print("Yes, set 2 is subset of set 1.")
        else:
            print("No, set 2 is not subset of set 1.")
            
    else:
        print("Thank You")
        break
