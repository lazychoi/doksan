# 독산 PLAYDATA 교육

## 1주차 python

### 10/04(화)

- (개인) wsl 설치, git 설치. ssh 등록. doksan repository 만듦
- 아나콘다 설치
- 주피터 노트북 사용법
- 마크다운 문법
- 데이터 타입: 숫자형, 정수형, 실수형
- 연산자: 산술, 비교, 논리, 할당
- 백준 파이썬 배우기(https://www.acmicpc.net/workbook/view/459)

input으로 입력받은 여러 숫자(공백으로 구분)를 split()으로 나눈 후 일괄 수치형으로 변환
- **map(자료형, input().split())**
- map(function, iterable)

나눗셈 몫을 정수로 출력(나눗셈 결과값보다 작은 정수 중에서 가장 큰 정수)
- **// 연산자**
- 4/3 => 1.3333
- 4//3 => 1

### 10/05(수)

- 문자열 타입, 문자열 연산, 인덱싱, 슬라이싱, 내장함수
- 리스트 
- 백준 파이썬 배우기(https://www.acmicpc.net/workbook/view/459)

문자열 => 아스키코드 : ord('A') -> 65
아스키코드 => 문자열 : chr(48) -> '0'
문자열 크기 비교는 ASCII 번호 순(소문자 < 대문자)

print() 출력할 때 쉼표(,)를 붙이기: print( variable, end = ', ' )

간격을 음수로 주면 역순으로 표시: 'hello'[::-1] -> 'olleh

join() : 점(.)왼쪽에 있는 요소를 .join(자료)의 자료 인덱스 사이사이에 입력함. eg. ','.join('abc') -> 'a,b,c'

**날짜 함수**

- time.time() 함수는 컴퓨터의 현재 시각을 구하는 함수 -> 1664957219.9671867
- 보통 사람이 이해하기 쉬운 datetime 모듈 사용
- time.strftime()은 기호로 출력 방식을 지정할 수 있다.
- 참고: https://python.bakyeono.net/chapter-11-3.html

```python
from datetime import date
from time import strftime

today = date.today()
print(today.strftime('%Y-%m-%d'))
```

## 10/06(목)

수업

- 리스트 타입 함수: append(), extend(), insert()
- in 연산자
- 