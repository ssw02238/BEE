# API 문서

- 참조

    restful api

    [https://devuna.tistory.com/79](https://devuna.tistory.com/79)



### Accounts

**path = "/api/accounts"**

- 회원가입

    `@post`  /signup

    **request**

    ```json
    {
    	"username" : "bee",
    	"email": "bee0302@gmail.com",
    	"password" : "beepassword",
    }
    ```

    **response**

    ```json
    {
    	"message" : "success"
    }
    ```

- 로그인

    `@post`  /api-token-auth

    - django REST framework JWT Token 이용

    **request**

    ```json
    {
    	"email" : "bee0302@gmail.com",
    	"password" : "beepassword",
    }
    ```

    **response**

    ```json
    ResponseBody
    {
      "message": "success",
    }

    Response Header
    {
    	"authorization" : "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbkB0dW1vLmNvbSIsImF1dGgiOiJST0xFX0FETUlOIiwiZXhwIjoxNjI3NDIxNzExfQ.hESzj25QdLGP20Z87hdVuiHPJKT8qca-0o76fDD3fMWX4BspeYdwRQVvhIjNUb1ZtkXoB8KpFZ-LcgnT8nOSxA"
    }
    // 해당 토큰을 로컬 스토리지에 저장 
    // 로그아웃 시 로컬 스토리지에서 삭제 (api x) 
    ```

- 비밀번호변경

    `@put`  /password

    **request**

    ```json
    {
    	"data": {
    		"password": "beepassword",
    	},
    	"headers": {
    		"config": {
    			"Authorization": `JWT ${token}`
    		},
    	},	
    }
    ```

    **response**

    ```json
    ResponseBody
    {
      "message": "success",
    }
    ```

- 프로필 조회

    `@get`  /profile

    **request**

    ```json
    {
    	"headers": {
    		"config": {
    			"Authorization": `JWT ${token}`
    		},
    	},	
    }
    ```

    **response**

    ```json
    ResponseBody
    {
      "message": "success",
    	"data": "user information"
    }
    
    Response Header
    {
    	"authorization" : "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbkB0dW1vLmNvbSIsImF1dGgiOiJST0xFX0FETUlOIiwiZXhwIjoxNjI3NDIxNzExfQ.hESzj25QdLGP20Z87hdVuiHPJKT8qca-0o76fDD3fMWX4BspeYdwRQVvhIjNUb1ZtkXoB8KpFZ-LcgnT8nOSxA"
    }
    
    ```

### Boards

**path = "/api/boards"**

- ESG 총합 순위 전체 리스트 조회

    `@get`  /esg-ranking

    **response**

    ```json
    {
    	"corporates" : [
    		{ "id": 1,
    			"name": "삼성전자",
    			"E_rating": 90.0,
    			"S_rating": 90.0,
    			"G_rating": 90.0,
    			"ESG_rating": 90.0,
    		},
    		{ "id": 2,
    			"name": "현대자동차",
    			"E_rating": 85.0,
    			"S_rating": 85.0,
    			"G_rating": 85.0,
    			"ESG_rating": 85.0,
    		},
    	],
    }
    ```

- ESG 각 항목 별 순위 리스트 조회

    E 순위 리스트 

    `@get`  /e-ranking

    **response**

    ```json
    {
    	"corporates" : [
    		{ "id": 1,
    			"name": "삼성전자",
    			"E_rating": 90.0,
    			"S_rating": 90.0,
    			"G_rating": 90.0,
    			"ESG_rating": 90.0,
    		},
    		{ "id": 2,
    			"name": "현대자동차",
    			"E_rating": 85.0,
    			"S_rating": 95.0,
    			"G_rating": 95.0,
    			"ESG_rating": 91.6,
    		},
    	],
    }
    ```

    S 순위 리스트

    `@get`  /s-ranking

    **response**

    ```json
    {
    	"corporates" : [
    		{ "id": 1,
    			"name": "삼성전자",
    			"E_rating": 90.0,
    			"S_rating": 90.0,
    			"G_rating": 90.0,
    			"ESG_rating": 90.0,
    		},
    		{ "id": 2,
    			"name": "현대자동차",
    			"E_rating": 95.0,
    			"S_rating": 85.0,
    			"G_rating": 95.0,
    			"ESG_rating": 91.6,
    		},
    	],
    }
    ```

    G 순위 리스트

    `@get`  /g-ranking

    **response**

    ```json
    {
    	"corporates" : [
    		{ "id": 1,
    			"name": "삼성전자",
    			"E_rating": 90.0,
    			"S_rating": 90.0,
    			"G_rating": 90.0,
    			"ESG_rating": 90.0,
    		},
    		{ "id": 2,
    			"name": "현대자동차",
    			"E_rating": 95.0,
    			"S_rating": 95.0,
    			"G_rating": 85.0,
    			"ESG_rating": 91.6,
    		},
    	],
    }
    ```

- ESG 1위 기업 조회

    `@get`  /bestcorp

    **response**

    ```json
    {
    	"corporate" : {
    		"id": 1,
    		"name": "삼성전자",
    		"E_rating": 90.0,
    		"S_rating": 90.0,
    		"G_rating": 90.0,
    		"ESG_rating": 90.0,
    	},
    	"environment": {
    		"id": 1,
    		"co2": 10000,
    		"energy": 100000,
    	},
    	"social": {
    		"id": 1,
    		"average_term": 10,
    		"term_ratio": 0.3,
    	},
    	"governance": {
    		"id": 1,
    		"board_ratio": 60.0,
    		"board_independency": 'true',
    		"salary_gap": 1000.0,
    		"dividen_ratio": 10.5,
    		"largest_shareholder": 20.0,
    	},
    }
    ```

- 오늘의 기업 조회

    `@get`  /hottestcorp

    **response**

    ```json
    ResponseBody
    {
      "Corp1":[
    {"Corporate_name": "기업 이름"},
    {"News_link": "뉴스 url"},
    {"News_title": "뉴스 헤드라인 "}
    ],
    	"Corp2":[
    {"Corporate_name": "기업 이름"},
    {"News_link": "뉴스 url"},
    {"News_title": "뉴스 헤드라인 "}
    ],
    	"Corp3":[
    {"Corporate_name": "기업 이름"},
    {"News_link": "뉴스 url"},
    {"News_title": "뉴스 헤드라인 "}
    ],
    }

    ```

- 스크랩 높은 기업 조회 (개수 미정)

    `@get`  /popularcorp

    **response**

    ```json
    {
      "corporates": [
    		{
    			"id": 1,
    			"corp_name": "삼성",
    			"scrap_cnt": 10
    		},
    		{
    			"id": 2,
    			"corp_name": "현대",
    			"scrap_cnt": 5
    		},
    		{
    			"id": 3,
    			"corp_name": "SK",
    			"scrap_cnt": 1
    		},
    	]
    }

    ```

- 전체 뉴스 리스트 조회

    `@get`  /news

    **response**

    ```json
    {
      "news": [
    		{
    			"id": 1,
    			"corp_id": 1,
    			"link": "www.naver.com",
    			"title": "삼성 ESG 개혁 나선다.",
    			"content": "오는 10월 삼성이 대대적인 ... 중략",
    		},
    		{
    			"id": 2,
    			"corp_id": 3,
    			"link": "www.naver.com",
    			"title": "삼성 ESG 개혁 나선다.",
    			"content": "오는 10월 삼성이 대대적인 ... 중략",
    		},
    		{
    			"id": 3,
    			"corp_id": 2,
    			"link": "www.naver.com",
    			"title": "삼성 ESG 개혁 나선다.",
    			"content": "오는 10월 삼성이 대대적인 ... 중략",
    		},
    	]
    }
    
    ```

### Corporates

**path = "/api/corporates"**

- 기업 디테일 조회 (ESG 평가)

    `@get`  /{corp_id}/detail

    **response**

    ```json
    {
    	"corporate" : {
    		"id": 1,
    		"name": "삼성전자",
    		"E_rating": 90.0,
    		"S_rating": 90.0,
    		"G_rating": 90.0,
    		"ESG_rating": 90.0,
    	},
    	"environment": {
    		"id": 1,
    		"co2": 10000,
    		"energy": 100000,
    	},
    	"social": {
    		"id": 1,
    		"average_term": 10,
    		"term_ratio": 0.3,
    	},
    	"governance": {
    		"id": 1,
    		"board_ratio": 60.0,
    		"board_independency": 'true',
    		"salary_gap": 1000.0,
    		"dividen_ratio": 10.5,
    		"largest_shareholder": 20.0,
    	},
    }
    ```

- 기업뉴스 조회

    `@get`  /{corp_id}/news

    **response**

    ```json
    {
      "news": [
    		{
    			"id": 1,
    			"link": "www.naver.com",
    			"title": "삼성 ESG 개혁 나선다.",
    			"content": "오는 10월 삼성이 대대적인 ... 중략",
    		},
    		{
    			"id": 2,
    			"link": "www.naver.com",
    			"title": "삼성 ESG 개혁 나선다.",
    			"content": "오는 10월 삼성이 대대적인 ... 중략",
    		},
    		{
    			"id": 3,
    			**"link": "www.naver.com",
    			"title": "삼성 ESG 개혁 나선다.",
    			"content": "오는 10월 삼성이 대대적인 ... 중략",
    		},
    	]
    }

    ```

- 유사 기업 조회

    `@GET` **** /{corp_id}/similarcorp

    **response**

    - 성공

        ```json
        {
          "corporates": [
        		{
        			"id": 1,
        			"corp_name": "삼성",
        		**},
        		{
        			"id": 2,
        			"corp_name": "현대",
        		},
        		{
        			"id": 3,
        			"corp_name": "SK",
        		},
        	]
        }
        
        ```

- 스크랩 추가

    `@post`  /{corp_id}/scrap

    **request**

    ```json
    {
    	"headers": {
    		"config": {
    			"Authorization": `JWT ${token}`
    		},
    	},	
    }
    ```

    **response**

    ```json
    ResponseBody
    {
      "message": "success",
    }
    ```

- 기업 검색

    `@get` /search/{searchContent}

    **response**

    ```json
    {
      "corporates": [
    		{
    			"id": 1,
    			"corp_name": "삼성",
    		**},
    		{
    			"id": 2,
    			"corp_name": "현대",
    		},
    		{
    			"id": 3,
    			"corp_name": "SK",
    		},
    	]
    }
    
    ```