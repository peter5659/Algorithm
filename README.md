# Algorithm

알고리즘
문법
===========

python
-------------
### *[String]*
python에서 string은 인덱싱, 붙이기, 검색, 삭제가 가능하다.
string_a = str()로 비어있는 문자열 생성 가능
string_a = "abcdefg"
string_a[1:5] = "bcdef"와 같이 일부분을 추출 가능
string_a = string_b + string_c와 같이 문자열을 이어붙여 새로운 문자열을 만들기도 가능
즉, 문자열의 길이를 신경 안써도 된다.
string_a.find('a') = 검색하려는 문자가 존재한다면 인덱스번호, 없다면 -1을 내놓는다.
len(string_a) : 문자열의 길이


### *[Class]*
~~~python
class Person: 
  def init(self):
    self.finger = 5
    self.eye = 2
~~~
init : a class 객체를 만들면 알아서 호출되는 함수 <br>
hwan = Person()로 객체생성하면 저절로 hwan.finger = 5, hwan.eye =2 가 된다.

### *[ListNode]*
listNode는 점으로 이어진 list로 현재위치에서의 value와 다음 점(next)에 대한 정보로 나타냄.

l1 = listNode() 하면 현재 점이 생기고 next는 없는 하나의 header가 생기는 것. 
<br> 
l1.val = 2 로 현재 점의 정보에 대해 접근 가능하고 l1.next.val = 5 로 다음 점을 설정 가능 
<br>
흠 2->5->4이거 넣는건 어떻게 하더라?
~~~python
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
~~~
* nodelist class를 만들고 init함수로 노드를 생성해주었다.
append 함수로 노드를 이어주었고 node에 first와 final을 이용해서 node에 어떠한 변경사항 없이 이어줄 수 있었다.

* 만든 node객체 자체로 움직이면(node1 = node1->next) 현 위치가 바뀌기 때문에
다른 객체로 접근하는 것이(what -> node1) 좋을듯??

Leet Code
====================
## 2. Add Two Number [(Code)](https://github.com/peter5659/Algorithm/commit/4c0c83262bbe60da3cde7e72e96c642c47f9a056)

### 사용개념

* [class](#class)
* [listNode](#listNode) 여기서는 list를 class listNode(self, val =0, next = None): self.val = val self.next = next 로 정의하였음.

### 풀이
> 두가지 방법으로 풀이 가능(재귀, 반복)

## 3. Longest Substring Without Repeating Characters  [(Code)](https://github.com/peter5659/Algorithm/commit/1d9aba8ce0a1ec48866930cc44f683427be2f862)

### 사용개념

* [string](#string)

### 풀이
> 
python에서 문자열을 다른 언어에 비해 자유롭게 쓸수 있다는 점에서 편하게 생각할 수 있었다.
<br>
문자열 붙이기를 사용하여 반복되지 않은 문자가 추가되었을때는 (기존문자열 + 새로운문자)로 추가
<br>
반복된 문자가 추가 되었을때는 []인덱싱으로 추가해주었다.
* 헷갈린 점
반복된 문자가 추가되었을 시에 인덱싱 범위를 정해주는 것에서 헷갈렸다. 
 -> 처음에는 반복된 문자를 지워주었음.
 -> 이후 반복된 문자 뒤에서부터만 챙기면 된다는 것을 깨닫고 .find로 찾은 인덱스 뒤부터 [+1:]로 새로운 문자열을 생성해주었다.
* 꼼꼼해야 할 점
문자열이 = " "일때.
문자열이 반복되는 것이 없을때.(기본형)

## 4. Median of Two Sorted Arrays  (Code) (https://github.com/peter5659/Algorithm/commit/aa57b17e07297617c931b289508312a61d87aba5)
