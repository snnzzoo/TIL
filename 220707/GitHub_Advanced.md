###### 7월 7일

# GitHub 2일차



## 복습

- 로컬저장소

```bash
# 로컬
$ git init
$ git add .
$ git commit -m '커밋메시지'
$ git status
$ git log
```



## 1. pull 

- 원격저장소로부터 변경된 내역을 받아와서 이력을 병합함

​	`$ git pull <원격저장소 이름> <브랜치 이름>`



## 2. clone

- 원격저장소를 복제하여 로컬로 가져옴

​	`$ git clone <원격저장소 주소>`



## 요약

| 명령어                            | 내용                                |
| --------------------------------- | ----------------------------------- |
| git remote add <원격저장소> <url> | 원격저장소 추가 (일반적으로 origin) |
| git remote -v                     | 원격저장소 정보 확인                |
| git remote rm <원격저장소>        | 원격저장소 삭제                     |
| git clone <url>                   | 원격저장소 복제                     |
| git push <원격저장소> <브랜치>    | 원격저장소에 push                   |
| git pull <원격저장소> <브랜치>    | 원격저장소로부터 pull               |



```bash
# 원격
$ git pull origin master
$ git push origin master
$ git remote add origin <repository 주소>
$ git clone <repository 주소>
```

