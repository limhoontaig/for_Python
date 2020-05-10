# 다음 조건에 따라 재주문 목록을 출력하는 프로그램을 작성하라
# N가지 재료를 사용하여 물건을 생산하는 회사가 있다.
# 이 중 M가지 재료의 재고가 있는 것을 알고 있다.
# 재고가 없는 재료를 재주문을 해야 한다.
# 재료는 1번부터 시작하는 고유번호가 있고, 결번은 없다
# 재고가 있는 재료의 번호가 주어지면
# 재주문 해야하는 재료의 번호를 오름차순으로 출력한다
# 예) 재료가 10가지인데 8가지 재고가 있고
# 그 목록이 3, 2, 5, 10, 9, 6, 1, 4 이면
# 7, 8 번이 재주문 해야 하는 목록이 된다.

# 입력, 출력의 예)
# 첫 줄에 총재료의 수와 재고 재료의 수 N, M이 공백으로 구분되어 입력된다
# 둘째 줄에 재고 재료의 번호가 M개 만큼 공백으로 구분되어 입력된다
# 10 8
# 3 2 5 10 9 6 1 4
# 출력
# 7 8
N, M = map(int, input().split())
a = set( range(1, N+1) )
b = set( map(int, input().split()) )
c = a - b
print(c)
d = sorted(c)
print(*d)   # print(d[0], d[1])
print(' '.join(map(str, d)))
