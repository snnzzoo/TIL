###### 7월 7일

# Git & GitHub Day 2



## 📝 복습

- 로컬저장소

```bash
# 로컬
$ git init
$ git add .
$ git commit -m '커밋메시지'
$ git status
$ git log
```

> 항상 모든 명령어 뒤에 `$ git status`로 상태를 확인하자!



## 1. pull 

- 원격저장소로부터 변경된 내역을 받아와서 이력을 병합함

​	`$ git pull <원격저장소 이름> <브랜치 이름>`



## 2. clone

- 원격저장소를 복제하여 로컬로 가져옴

​	`$ git clone <원격저장소 주소>`



## 📑 요약

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





## 🌊 Git Flow

- Git을 활영하여 협업하는 흐름으로 branch를 활용하는 전략을 의미한다.

![img](Git_GitHub_Day2.assets/vlan.png)

| branch                        | 주요 특징                                                    | 예시                                               |
| ----------------------------- | ------------------------------------------------------------ | -------------------------------------------------- |
| master (main)                 | * 배포 가능한 상태의 코드 *사용자가 보는 화면                | LOL 클라이언트 라이브 버전 (9.23.298.3143)         |
| develop (main)                | * feature branch로 나뉘어지거나 발생된 버그 수정 등 개발 진행 * 개발 이후 release branch로 갈라짐 | 다음 패치를 위한 개발 (9.24)                       |
| feature branches (supporting) | * 기능별 개발 브랜치(topic branch) * 기능이 반영되거나 드랍되는 경우 브랜치 삭제 | 개발시 기능별 예) 신규챔피언 세나, 드래곤 업데이트 |
| release branches (supporting) | * 개발 완료 이후 QA/Test 등을 통해 얻어진 다음 배포 전 minor bug fix 등 반영 | 9.24a, 9.24b, ...                                  |
| hotfixes (supporting)         | * 긴급하게 반영해야 하는 bug fix * release branch는 다음 버전을 위한 것이라면 hotfix는 현재 버전을 위한 것 | 긴급 패치를 위한 작업                              |

- Git Flow는 정해진 답이 있는 것은 아니다.
- Github Flow, Gitlab Flow 등의 각 서비스별 제안되는 흐름이 있으며, 변형되어 각자의 프로젝트/회사에서 활용되고 있다.



## 🍆 Branch

### Branch basic commands

1. 브랜치 생성

``` bash
(master) $ git branch <branch name>
```

2. 브랜치 이동

```bash
(master) $ git checkout <branch name>
```

3. 브랜치 생성 및 이동

```bash
(master) $ git checkout -b <branch name>
```

4. 브랜치 목록

```bash
(master) $ git branch
```

5. 브랜치 삭제

```bash
(master) $ git branch -d <branch name>
```



| 명령어                          | 내용                |
| ------------------------------- | ------------------- |
| $ git branch <branch name>      | 브랜치 생성         |
| $ git checkout <branch name>    | 브랜치 이동         |
| $ git checkout -b <branch name> | 브랜치 생성 및 이동 |
| $ git branch                    | 브랜치 목록         |
| $ git branch -d <branch name>   | 브랜치 삭제         |



### Branch merge

각 branch에서 작업을 한 이후 이력을 합치기 위해서는 일반적으로 merge 명령어를 사용한다.

병합을 진행할 때, 만약 서로 다른 이력(commit)에서 동일한 파일을 수정할 경우 충돌이 발생할 수 있다. 이 경우에는 반드시 직접 수정을 진행해야 한다.

충돌이 발생한 것은 오류가 발생한 것이 아니라 이력이 변경되는 과정에서 반드시 발생할 수 있는 것이다.

#### fast-forward

- 기존 master branch에 변경사항이 없어 단순히 앞으로 이동

```bash
(master) $ git merge feature-a
Updating 54b9314..5429f25
Fast-forward
```

1. feature-a branch로 이동 후 commit
2. master 별도 변경 없음
3. master branch로 병합

#### merge commit

- 기존 master branch에 변경사항이 있어 병합 커밋 발생

```bash
(master) $ git merge feature-a
Already up to date!
Merge made by the 'recursive' strategy.
```

1. feature-a branch로 이동 후 commit
2. master branch commit
3. mater branch로 병합



## 🌊 Github Flow

- Github에서 제안하는 브랜치 전략



### 기본 원칙

1. **master branch는 반드시 배포 가능한 상태여야 한다.**
2. **feature branch는 각 기능의 의도를 알 수 있도록 작성한다.**
3. **Commit message는 매우 중요하며, 명확하게 작성한다.**
4. **Pull Request를 통해 협업을 진행한다.**
5. **변경사항을 반영하고 싶다면, master branch에 병합한다.**



### 1. Feature Branch Workflow

- Shared repository model (저장소의 소유권이 **있는** 경우)

![img](https://velog.velcdn.com/images/drata313/post/f13d0d75-b059-451a-87fe-5edab6a6a90f/image.png)

1. 각 사용자는 원격저장소의 소유권을 가진 상태. 따라서 **clone**을 통해 저장소를 로컬에 복제
2. 기능 추가를 위해 branch 생성 및 기능 구현
3. 기능 구현 후 원격저장소에 branch 반영
4. 병합 완료 후 병합 완료된 branch 삭제
5. master branch로 switch
6. 병합된 master의 내용을 pull
7. 원격저장소에서 병합 완료된 로컬 branch 삭제
8. 새로운 기능 추가를 위해 branch 생성 및 과정 반복



### 2. Forking Workflow

- Fork & Pull model (저장소의 소유권이 **없는** 경우)

![img](https://velog.velcdn.com/images/drata313/post/eb07867f-f881-4d15-bea1-aea9a30cd2d1/image.png)

1. 소유권이 없는 원격저장소를 fork를 통해 복제
2. 로컬저장소를 원본 원격저장소와 동기화하기 위해 URL을 연결
3. 기능 추가를 위해 branch 생성 및 기능 구현
4. 기능 구현 후 원격저장소에 branch 반영
5. 원본 소유자에게 Pull Request
6. 원본 소유자가 병합
7. 병합 완료 후 병합 완료된 branch 삭제
8. master branch로 switch
9. 병합된 master의 내용을 pull
10. 원격저장소에서 병합 완료된 로컬 branch 삭제
11. 새로운 기능 추가를 위해 branch 생성 및 과정 반복



> Shared Repository Model과 Fork & Pull Model의 가장 큰 차이점은 작업자가 해당 프로젝트 저장소에 **직접적인 push 권한이 있는지**의 여부이다.
