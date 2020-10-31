# print 출력

### 1. ,를 사용하여 스트링을 연결해 출력할 수 있다.
### 2. sep를 사용하여 스트링간 구분자를 설정할 수 있다.
### 3. end를 사용하여 끝나는 문자를 설정할 수 있다.
-- sep와 end는 잘 사용하지 않는다.

~~~python
print('Hi')
print('Hi', 'Mike')
print('Hi', 'Mike', sep=',')
print('Hi', 'Mike', sep=',', end='.\n')
~~~

~~~python
Hi
Hi Mike
Hi,Mike
Hi,Mike.

~~~