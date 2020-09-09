# Algorithm

알고리즘
문법
===========

python
-------------
### **[class]**
class Person: def init(self): self.finger = 5 self.eye = 2

init : a class 객체를 만들면 알아서 호출되는 함수 -> hwan = Person()로 class 를 만들면 hwan.finger = 5, hwan.eye =2 가 된다.

### **[listNode]**
listNode는 점으로 이어진 list로 현재위치에서의 value와 다음 점(next)에 대한 정보로 나타냄. class listNode(self, val =0, next = None): self.val = val self.next = next

l1 = listNode() 하면 현재 점이 생기고 next는 없는 하나의 header가 생기는 것. l1.val = 2 로 현재 점의 정보에 대해 접근 가능하고 l1.next.val = 5 로 다음 점을 설정 가능 흠 2->5->4이거 넣는건 어떻게 하더라?

class nodelist:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.first = self
    self.final = self
    self.next = next
  def append(self, data):
    new_node = nodelist(data)
    self.final.next = new_node
    self.final = self.final.next
node1 = nodelist(1)
print("node1:",node1.val)
node1.append(3)
node1.append(5)
node1.append(7)
node1.append(9)
what = node1
while(what):
  print(what.val)
  what = what.next

* nodelist class를 만들고 init함수로 노드를 생성해주었다.
append 함수로 노드를 이어주었고 node에 first와 final을 이용해서 node에 어떠한 변경사항 없이 이어줄 수 있었다.

Leet Code
====================
## 2. Add Two Number

### 사용개념

* [class](#class)
* [listNode](#listNode) 여기서는 list를 class listNode(self, val =0, next = None): self.val = val self.next = next 로 정의하였음.

### 풀이
> 두가지 방법으로 풀이 가능(재귀, 반복)
