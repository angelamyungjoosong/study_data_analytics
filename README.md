<details open>

#### [다변수 검증 방법](https://github.com/angelamyungjoosong/study_data_analytics/blob/main/codes/image/%EB%8B%A4%EB%B3%80%EC%88%98%20%EA%B2%80%EC%A6%9D.png)

<summary>Titanic From Disaster</summary>

#### DDA
| Variable | Definition | Key | 분석가 의견 |
| --- | --- | --- | --- |
| survival | Survival | 0 = No, 1 = Yes | 범주형-명목형, 확인 결과 데이터 타입이 결정됨 |
| pclass | Ticket class | 1 = 1st, 2 = 2nd, 3 = 3rd | 범주형-순서형, 확인 결과 class 1,2,3 세개의 등급별 범주로 나누기 때문에 순서의 의미를 갖음 | 
| sex | Sex | | 범주형-명목형, 확인 결과 female, male 두개의 범주이며 순서가 존재하지 않음 |
| Age | Age in years | | 수치형-이산형, 확인 결과 나이 값이 연속으로는 존재하지 않으며 나이는 통계값 내는 데 활용 가능 |
| sibsp | # of siblings / spouses aboard the Titanic | | 수치형-순서형, 확인 결과   |
| parch | # of parents / children aboard the Titanic | | 수치형-순서형, 확인 결과  |
| ticket | Ticket number | |범주형-명목형, | 
| fare | Passenger fare | | 수치형-이산형, 요금은 통계 수치 계산이 가능하며 값이 연속으로 존재하지 않음  |
| cabin | Cabin number | | 범주형-순서형| 
| embarked | Port of Embarkation | C = Cherbourg, Q = Queenstown, S = Southampton | 범주형-명목형|

</details>


<details open>
<summary>Type Of Contract Channel</summary>

#### DDA
| Variable | Definition | Key | 분석가 의견 |
| --- | --- | --- | --- |
| id | 아이디 |   | 범주형-명목형, 숫자로 이루어졌음에도 통계계산을 하는데 이용되지 않으며 해당 고객을 구분하는 목적으로 사용됨, 특정 기준에 따라 순서의 의미를 갖는지 판단 불가  |
| type_of_contract | 계약서 종류 | 렌탈, 멤버십 | 범주형-명목형, 두가지 범주로 나뉘며 순서가 존재하지 않음 | 
| type_of_contract2 | 계약서 종류 | Normal, Promotion, Extension_Rental, Package, TAS| 범주형-명목형, 5가지 범주로 나뉘며 순서가 존재하지 않음
| channel | 계약 경로 | 서비스 방문, R관리방판, 전자랜드, 렌탈총판, 일반, 하이마트,...| 범주형-명목형, 정해진 개수의 범주로 나뉘며 순서가 존재하지 않음  |
| Term | 계약 기간 | 12, 36, 60| 범주형-명목형, 3가지 범주로 나뉘며 순서가 존재하지 않음 |
|payment_type | 결제 방식 | CMS, 카드이체, 무통장 | 범주형-명목형, 3가지 범주로 나뉘며 순서가 존재하지 않음 |
| product | 상품명 | | 범주형-명목형, 상품종류의 개수에 따라 범주가 나뉘며, 숫자가 순서의 의미를 갖는지 확인 여부 불가| 
| amount | 상품금액 |  | 수치형-이산형, 상품금액은 통계수치 계산에 활용할 수 있으며, 연속적인 수치가 아님 |
| state | 계약 상태 | 계약확정, 해약확정 | 범주형-명목형, 2가지 범주로 나뉘며 순서가 존재하지 않음 | 
| overdue_count | 지불 지연 횟수 |   | 수치형-이산형, 통계수치 게산에 활용될 수 있으며,변수의 값을 셀 수 있는 자료임|
| overdue | 지불 지연 여부 | 있음, 없음 |  | 범주형-명목형, 2가지 범주로 나뉘며 순서가 존재하지 않음
| credit rating | 신용 등급 | | 수치형-연속형, 통계수치 계산에 활용될 수 있으며, 등급은 순서가 존재함 | 
| bank | 은행명 | | 범주형-명목형, 은행종류 개수에 따른 범주로 나뉘며 순서가 존재하지 않음 | 
| cancellation | 해약 여부| | 범주형-명목형, state와 겹치는 데이터로 사용하지 않음| 
| age | 나이 | | 수치형-연속형, 통계수치 계산에 활용될 수 있으며 수치가 연속적임 | 
| Mileage | 마일리지 | | 수치형-연속형, 통계수치 계산에 활용될 수 있으며 수치가 연속적임 | 
</details>

https://blog.naver.com/data_station/222493245799


