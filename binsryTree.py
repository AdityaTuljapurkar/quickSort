
class Node :
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class BinaryTree : 

        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f


        def deptFirst(self,root):
             if root is None :
                  return []
             else :
                    result = []
                    stack= [root]
                    while (len(stack)>0):
                        current = stack.pop()
                        result.append(current.val)
                        if current.right is not None :
                            stack.append(current.right)
                        if current.left is not None :
                             stack.append(current.left)


                    return result
        

        def BreathFirst(self,root):
            if root is None : 
                return []
            else : 
                result= []
                queue = [root]
                while (len(queue)>0):
                    current = queue.pop(0)
                    result.append(current.val)
                    if current.right is not None :
                        queue.append(current.right)
                    if current.left is not None :
                        queue.append(current.left)
            return  result

        def deptFirstrec(self,root):
            if root is None :
                return [] 
            else :
                leftVal = self.deptFirstrec(root.left)
                rightVal = self.deptFirstrec(root.right)
            return [root.val]+leftVal+rightVal


        def includes(self,target,root):
            if root is None :
                 return False
            elif  root.val == target :
                 return True
            else :
                queue =[root]
                while (len(queue)>0):
                    current =  queue.pop(0)
                    if current.val is target :
                         return True
                    else :
                        if current.left is not None :
                              queue.append(current.left)
                        if current.right is not None :
                             queue.append(current.right)
                return False

        def includesRec(self,root,target):
            if root is None :
                return False                           
            if root.val is target : return True

            return self.includesRec(root.left,target) or self.includesRec(root.right,target)
        1

            

bst =BinaryTree()
A = bst.a
red = bst.deptFirst(A)
reb=bst.BreathFirst(A)
rez =bst.deptFirstrec(A)
res =bst.includes('4',A)
resr = bst.includesRec(A,'e')

print(reb)
print(red)
print(rez)
print(res)  #True
print(resr)                
            








    