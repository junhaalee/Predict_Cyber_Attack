# 트윗을 이용한 그래프와 시계열 기반 사이버 공격 예측

## 프로젝트 소개

트위터를 이용하는 사용자들 중 사이버 공격과 관련된 사용자들 간의 관계 데이터를 그래프 데이터베이스에 저장하고 다양한 그래프 알고리즘을 통해 연관된 사용자들끼리의 그룹을 생성하고, 각 그룹별로 트윗 활동을 표현한 시계열 데이터를 동시에 활용하여 사이버 공격에 대한 예측 방법을 제안.

## Contents

- [Result](https://github.com/junhaalee/Predict_Cyber_Attack/tree/master/Result)
	
	- 사용자 관계 데이터를 이용한 그래프 - Network Graph
	
	- 그룹별 트윗 활동을 표현한 그래프 - Time-Series Graph


- [Code](https://github.com/junhaalee/Predict_Cyber_Attack/tree/master/Code)
	
	- Graph(https://github.com/junhaalee/Predict_Cyber_Attack/tree/master/Code/Graph)
		- Network Graph
		- Time Series Graph

	- News(사이버 공격과 관련된 뉴스 크롤링)(https://github.com/junhaalee/Predict_Cyber_Attack/tree/master/Code/News)

	- Tweet(트윗에서 사이버 공격과 연관된 키워드를 포함한 트윗 필터링)(https://github.com/junhaalee/Predict_Cyber_Attack/tree/master/Code/Tweet)

	- User(트위터 사용자 데이터 수집)(https://github.com/junhaalee/Predict_Cyber_Attack/tree/master/Code/User)