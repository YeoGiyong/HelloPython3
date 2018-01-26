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
books_list.append(Book)
books_list.append(Book)
books_list.append(Book)
print(books_list)