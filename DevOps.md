# DevOps 



## Deploy

> [참고](https://daily-life-of-bsh.tistory.com/223)

### DB

- MySQL
- Workbench
  - AWS RDS 
    - hostname: `bee.cjkrtt0iwcwz.ap-northeast-2.rds.amazonaws.com`
    - port : 3306
    - user name : admin
    - pw : 1q2w3e4r5t!@

### Server

#### 환경

- AWS EC2 
  - Ububtu 20.04 LTS
  - SSH 접속 계정 : ubuntu@j5a302.p.ssafy.io
  - 인증키 : J5A302T.pem

  - public IP : 3.35.25.101
  - port : 22
- url : http://j5a302.p.ssafy.io/



#### 절차

- ssh 접속 key

  - cmd 명령어 : `ssh -i J5팀IDT.pem ubuntu@J5A302.p.ssafy.io`

- Niginx 설치

  -  설치된 패키지들의 새로운 버전이 있는지 확인
    - `sudo apt-get update`
  - 설치된 패키지들의 새로운 버전 업그레이드
    - `apt-get upgrade`
  - Nginx 설치
    - `sudo apt-get install nginx`

- Nginx 환경 설정

  - conf 파일 설정

    - `cd /etc/nginx/sites-available`
    - `sudo vi default`

  - frontend 설정

    ```unix
    server {
        listen 80 default_server;
        listen [::]:80 default_server;
    
        root /var/www/html/dist;
        index index.html index.htm;
        server_name _;
    
        location / {
            try_files $url $url/ /index.html;
        }
    }
    ```



- Nginx 시작

  - `sudo systemctl start nginx`

- Vue.js 배포

  - local에서 build

    - `npm run build`

  - 빌드 폴더(`dist`) 생성

  -  `dist` 폴더 remote 저장소로 이동

    - stp 통신

    - filezillar 이용

      유의 : `sudo chmod -R 777 /var/www` 를 통해 폴더 접근 권한 설정 후 진행

  - nginx 재시작

    - `sudo systemctl start nginx`s