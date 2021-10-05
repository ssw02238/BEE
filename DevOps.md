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
  - public IP : 3.34.142.234
  - port : 22
- url : http://j5a302.p.ssafy.io/



#### BE (django)

> 참고 URL
>
> [공식문서](https://docs.djangoproject.com/ko/3.2/howto/deployment/)
>
> [블로그1](https://nerogarret.tistory.com/45)
>
> [블로그2](https://velog.io/@hsngju/Django-EC2%EC%97%90%EC%84%9C-django-%EB%B0%B0%ED%8F%AC%ED%95%98%EA%B8%B0)

- settings.py 수정

  프로젝트 기본 설정을 배포 환경에 맞게 변경

  - `SECRET KEY` : 비밀 키는 큰 임의 값이어야 하며 기밀로 유지되어야 합니다.

    ```python
    import os
    SECRET_KEY = os.environ['SECRET_KEY']
    ```

    

    ```python
    with open('/etc/secret_key.txt') as f:
        SECRET_KEY = f.read().strip()
    ```

    택 1

  - `DEBUG` : 프로덕션에서 디버그를 사용 가능으로 설정하지 않아야 합니다.

    ```python
    DEBUG = False
    ```

  - `ALLOWED_HOST`

    ```python
    #특정 호스트 설정 《Host》 HTTP 헤더에 대한 자체 검증
    ALLOWED_HOSTS = ['*']
    
    #설정 안함
    server {
        listen 80 default_server;
        return 444;
    }
    ```



- 서버 컴퓨터 접속 (FE와 동일)

  - `ssh -i J5A302T.pem ubuntu@J5A302.p.ssafy.io`
  - srv folder 생성
    - `fileziller` 이용
  - python install
    - `sudo apt-get python3-pip`
  - mysql install
    - sudo apt-get update
    
    - sudo apt-get install mysql-server
    
    - sudo ufw allow mysql
    
    - ```swift
      sudo apt-get install python-dev libmysqlclient-dev
      ```
    
    - ```swift
      sudo apt-get install python3.8-dev
      ```

- git clone 

  - 폴더 소유자 변경
    - `sudo chown -R ubuntu:ubuntu /srv/`

  - ssh 인증키 설정 (ssh 통신 할 경우) / http의 경우 id, pw 입력을 통해 인증하여 진행할 수 있음
    - git bash를 통해 `ssh-keygen`
    - git lab accounts에서 등록
    - 이름 : `gyu_ssh_key`
  - `git clone {project_name}`

- 가상환경
  - `sudo apt-get install python3-venv`
  - `python3 -m venv venv`
  - `source venv/bin/activate`
  - `pip install -r requirements.txt`
  - `sudo apt install libmysqlclient-dev`
  - `pip install wheel`
  
- wsgi (웹 서버 소프트웨어와 파이썬으로 작성된 웹 응용 프로그램 간의 표준 인터페이스입니다) 설치
  - pip install uwsgi
    - 문제시 python-dev 설치
    - `sudo apt-get install python3.8-dev`
    
  - uwsgi initialize 파일 생성 

    > uwsgi는 wsgi와 python project 연결 시켜줌

    - manage.py 경로에 .config/uwsgi 폴더(2개) 생성

    - 해당 폴더 안에 {project_name}.ini 파일 생성

    - 파일 내용은 다음과 같다

      ```
      [uwsgi]
      chdir = /srv/S05P21A302/Backend/
      module = bee.wsgi:application
      home = /home/ubuntu/srv/S05P21A302/Backend/venv/
      
      uid = deploy
      gid = deploy
      
      http = :8000
      
      enable-threads = true
      master = true
      vacuum = true
      pidfile = /tmp/bee.pid
      logto = /var/log/uwsgi/bee/@(exec://date +%%Y-%%m-%%d).log
      log-reopen = true
      ```

  - uwsgi routing error

    ```
    python -m pip install --upgrade pip
    // pip가 최신 버전이 아닌 경우 실행
    
    sudo apt-get install libpcre3 libpcre3-dev
    // 필요 패키지 설치
    
    pip install uwsgi -I --no-cache-dir
    ```

    

  - uwsgi를 통해 서버 실행

    - test ()

      `uwsgi --http :8000 --home /home/ubuntu/srv/S05P21A302/Backend/venv/ --chdir /srv/S05P21A302/Backend/ -w bee.wsgi` 

    - config (설정 저장?)

      `sudo /home/ubuntu/srv/S05P21A302/Backend/venv/bin/uwsgi -i /home/ubuntu/srv/S05P21A302/Backend/.config/uwsgi/bee.ini`

    - wsgi를 통한 서버 실행

      `uwsgi --http :8000 --home /home/ubuntu/srv/S05P21A302/Backend/venv --chdir /srv/S05P21A302/Backend --module bee.wsgi`

- nginx 연결

  - nginx 설치

    `sudo apt-get nginx`

  - nginx 설정

    - `cd /etc/nginx/sites-available`

    - `touch {project_name}`

      ```
      upstream withthai-django {
          server unix:/home/ubuntu/srv/S05P21A302/Backend/run/uwsgi.sock;
      }
      
      server {
              listen 80;
              server_name 3.35.25.101;
      
              location = /favicon.ico { access_log off; log_not_found off; }
      
              location / {
                  include         /etc/nginx/uwsgi_params;
                  uwsgi_pass      django;
              }
      }
      ```

  - 사이트 추가

    - `cd /etc/nginx/sites-enabled`
    - `sudo ln -s /etc/nginx/sites-available/bee /etc/nginx/sites-enabled`

  - nginx 문법 검사 및 재가동

    - sudo nginx -t
    - sudo systemctl restart nginx

  - 방화벽 해제

    - **sudo** ufw delete allow 8000
    - **sudo** ufw allow 'Nginx Full'



#### FE (vue)

- ssh 접속 key

  - cmd 실행
  - pem (key pair) 존재하는 경로에서 다음 명령어 입력
  - `ssh -i J5A302T.pem ubuntu@J5A302.p.ssafy.io`

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

  - local에서 build & 빌드 폴더(`dist`) 생성

    - `npm run build`

  -  `dist` 폴더 remote 저장소로 이동

    - stp 통신

    - filezillar 이용

      유의 : `sudo chmod -R 777 /var/www` 를 통해 폴더 접근 권한 설정 후 진행

  - nginx 재시작

    - `sudo systemctl start nginx`

