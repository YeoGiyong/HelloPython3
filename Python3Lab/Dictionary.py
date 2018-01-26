#딕셔너리 : 매핑 자료 구조
#키에 값을 연결시키는 방식으로 데이터를 다루는 방법 제공
#키는 저장된 데이터를 식별하기 위한 번호나 이름
#값은 각 키에 연결되어 저장된 데이터
#따라서, 키만 알면 데이터를 바로 찾을 수 있음
#딕셔너리는 { }에 키:값 형태로 이용
#키:값이 여러 개 존재 할 경우 ,로 구분

menu = {'1':'newSungJuk', 2:'showSungJuk','abc':'modifySungJuk'}    #키는 다양한 자료형으로 사용

Book = {'bookid':'1','bookname':'축구의 역사','publisher':'굿스포츠','price':'7000'}
Order = {'orderid':'1','custid':'1','bookid':'1','saleprice':'6000','orderdate':'2014-07-01'}
Customer = {'custid':'1','name':'박지성','address':'영국맨체스터','phone':'000-5000-0001'}

print(Book)

books_list =[]
books_list.append(Book)     #생성한 딕셔너리를 배열에 저장
books_list.append(Book)
books_list.append(Book)
print(books_list)

# 딕셔너리 처리 메서드
print('1' in Book)          #딕셔너리에 in 연산자는 key를 검색
print('bookid' in Book)

print(Book['bookid'])       #딕셔너리에서 키로 검색
print(Book['bookname'])
print(Book['price'])
#print(Book['orderid'])      #존재하지 않는 키 검색시 오류!

print(Book.get('bookname'))
print(Book.get('orderid'))  #존재하지 않는 키 검색시 None출력

bkname = Book['bookname']   #키로 검색 후 값 출력
print(bkname)

print(Book.get('bookid'))
Book['bookid']=99         #키로 값 수정
print(Book.get('bookid'))

print(Book)
Book.update({'판형':'3x4'})   #새로운 키:값 추가
print(Book)

print(Book)
Book.update({'판형':'6x10'})   #새로운 키:값 수정
print(Book)

del Book['판형']              #기존 키 삭제
print(Book)

#Book.clear()                   #모든 키 삭제

print(Book.keys())             #모든 키를 출력
print(Book.values())           #모든 값을 출력
print(Book.items())            #모든 키:값을 튜플로 출력

items = Book.items()           #모든 키:값을 튜플-리스트로 출력
print(list(items))


