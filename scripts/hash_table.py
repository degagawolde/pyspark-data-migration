class verifyvalues: 
    def __init__(self):  
        self.new_list=[]  
    #update vales function  
    def update(self, key):  
        found=False  
        for i,k in enumerate(self.new_list):  
            if key==k:  
                self.new_list[i]=key  
                found=True  
                break  
        if not found:  
            self.new_list.append(key)  
      
    #get values function  
    def get(self, key):  
        for k in self.new_list:  
            if k==key:  
                return True  
        return False  
  
    #remove values function  
    def remove(self, key):  
         for i,k in enumerate(self.new_list):  
            if key==k:  
                del self.new_list[i]  

class MyHashSet: 
    #Initialization function  
    def __init__(self):  
        self.key_space = 2096  
        self.hash_table=[verifyvalues() for i in range(self.key_space)]  
    def hash_values(self, key):  
        hash_key=key%self.key_space  
        return hash_key  
    #add function  
    def add(self, key): 
        self.hash_table[self.hash_values(key)].update(key)  
    #remove function  
    def remove(self, key):  
        self.hash_table[self.hash_values(key)].remove(key)  
    #contains function  
    def contains(self, key):    
        return self.hash_table[self.hash_values(key)].get(key)  
    def display(self):  
        ls=[]  
        for i in self.hash_table:  
            if len(i.new_list)!=0:
                ls.append(i.new_list[0])  
        print(ls)  

# Your MyHashSet object will be instantiated and called as such:

obj = MyHashSet()
obj.add(1)
obj.remove(2)
param_3 = obj.contains(3)