###### 7μ 7μΌ

# Git/GitHub 2μΌμ°¨



## π λ³΅μ΅

- λ‘μ»¬μ μ₯μ

```bash
# λ‘μ»¬
$ git init
$ git add .
$ git commit -m 'μ»€λ°λ©μμ§'
$ git status
$ git log
```

> ν­μ λͺ¨λ  λͺλ Ήμ΄ λ€μ `$ git status`λ‘ μνλ₯Ό νμΈνμ!



## 1. pull 

- μκ²©μ μ₯μλ‘λΆν° λ³κ²½λ λ΄μ­μ λ°μμμ μ΄λ ₯μ λ³ν©ν¨

β	`$ git pull <μκ²©μ μ₯μ μ΄λ¦> <λΈλμΉ μ΄λ¦>`



## 2. clone

- μκ²©μ μ₯μλ₯Ό λ³΅μ νμ¬ λ‘μ»¬λ‘ κ°μ Έμ΄

β	`$ git clone <μκ²©μ μ₯μ μ£Όμ>`



## π μμ½

| λͺλ Ήμ΄                            | λ΄μ©                                |
| --------------------------------- | ----------------------------------- |
| git remote add <μκ²©μ μ₯μ> <url> | μκ²©μ μ₯μ μΆκ° (μΌλ°μ μΌλ‘ origin) |
| git remote -v                     | μκ²©μ μ₯μ μ λ³΄ νμΈ                |
| git remote rm <μκ²©μ μ₯μ>        | μκ²©μ μ₯μ μ­μ                      |
| git clone <url>                   | μκ²©μ μ₯μ λ³΅μ                      |
| git push <μκ²©μ μ₯μ> <λΈλμΉ>    | μκ²©μ μ₯μμ push                   |
| git pull <μκ²©μ μ₯μ> <λΈλμΉ>    | μκ²©μ μ₯μλ‘λΆν° pull               |



```bash
# μκ²©
$ git pull origin master
$ git push origin master
$ git remote add origin <repository μ£Όμ>
$ git clone <repository μ£Όμ>
```





## π Git Flow

- Gitμ νμνμ¬ νμνλ νλ¦μΌλ‘ branchλ₯Ό νμ©νλ μ λ΅μ μλ―Ένλ€.

![img](Git_GitHub_Day2.assets/vlan.png)

| branch                        | μ£Όμ νΉμ§                                                    | μμ                                               |
| ----------------------------- | ------------------------------------------------------------ | -------------------------------------------------- |
| master (main)                 | * λ°°ν¬ κ°λ₯ν μνμ μ½λ *μ¬μ©μκ° λ³΄λ νλ©΄                | LOL ν΄λΌμ΄μΈνΈ λΌμ΄λΈ λ²μ  (9.23.298.3143)         |
| develop (main)                | * feature branchλ‘ λλμ΄μ§κ±°λ λ°μλ λ²κ·Έ μμ  λ± κ°λ° μ§ν * κ°λ° μ΄ν release branchλ‘ κ°λΌμ§ | λ€μ ν¨μΉλ₯Ό μν κ°λ° (9.24)                       |
| feature branches (supporting) | * κΈ°λ₯λ³ κ°λ° λΈλμΉ(topic branch) * κΈ°λ₯μ΄ λ°μλκ±°λ λλλλ κ²½μ° λΈλμΉ μ­μ  | κ°λ°μ κΈ°λ₯λ³ μ) μ κ·μ±νΌμΈ μΈλ, λλκ³€ μλ°μ΄νΈ |
| release branches (supporting) | * κ°λ° μλ£ μ΄ν QA/Test λ±μ ν΅ν΄ μ»μ΄μ§ λ€μ λ°°ν¬ μ  minor bug fix λ± λ°μ | 9.24a, 9.24b, ...                                  |
| hotfixes (supporting)         | * κΈ΄κΈνκ² λ°μν΄μΌ νλ bug fix * release branchλ λ€μ λ²μ μ μν κ²μ΄λΌλ©΄ hotfixλ νμ¬ λ²μ μ μν κ² | κΈ΄κΈ ν¨μΉλ₯Ό μν μμ                              |

- Git Flowλ μ ν΄μ§ λ΅μ΄ μλ κ²μ μλλ€.
- Github Flow, Gitlab Flow λ±μ κ° μλΉμ€λ³ μ μλλ νλ¦μ΄ μμΌλ©°, λ³νλμ΄ κ°μμ νλ‘μ νΈ/νμ¬μμ νμ©λκ³  μλ€.



## π Branch

### Branch basic commands

1. λΈλμΉ μμ±

``` bash
(master) $ git branch <branch name>
```

2. λΈλμΉ μ΄λ

```bash
(master) $ git checkout <branch name>
```

3. λΈλμΉ μμ± λ° μ΄λ

```bash
(master) $ git checkout -b <branch name>
```

4. λΈλμΉ λͺ©λ‘

```bash
(master) $ git branch
```

5. λΈλμΉ μ­μ 

```bash
(master) $ git branch -d <branch name>
```



| λͺλ Ήμ΄                          | λ΄μ©                |
| ------------------------------- | ------------------- |
| $ git branch <branch name>      | λΈλμΉ μμ±         |
| $ git checkout <branch name>    | λΈλμΉ μ΄λ         |
| $ git checkout -b <branch name> | λΈλμΉ μμ± λ° μ΄λ |
| $ git branch                    | λΈλμΉ λͺ©λ‘         |
| $ git branch -d <branch name>   | λΈλμΉ μ­μ          |



### Branch merge

κ° branchμμ μμμ ν μ΄ν μ΄λ ₯μ ν©μΉκΈ° μν΄μλ μΌλ°μ μΌλ‘ merge λͺλ Ήμ΄λ₯Ό μ¬μ©νλ€.

λ³ν©μ μ§νν  λ, λ§μ½ μλ‘ λ€λ₯Έ μ΄λ ₯(commit)μμ λμΌν νμΌμ μμ ν  κ²½μ° μΆ©λμ΄ λ°μν  μ μλ€. μ΄ κ²½μ°μλ λ°λμ μ§μ  μμ μ μ§νν΄μΌ νλ€.

μΆ©λμ΄ λ°μν κ²μ μ€λ₯κ° λ°μν κ²μ΄ μλλΌ μ΄λ ₯μ΄ λ³κ²½λλ κ³Όμ μμ λ°λμ λ°μν  μ μλ κ²μ΄λ€.

#### fast-forward

- κΈ°μ‘΄ master branchμ λ³κ²½μ¬ν­μ΄ μμ΄ λ¨μν μμΌλ‘ μ΄λ

```bash
(master) $ git merge feature-a
Updating 54b9314..5429f25
Fast-forward
```

1. feature-a branchλ‘ μ΄λ ν commit
2. master λ³λ λ³κ²½ μμ
3. master branchλ‘ λ³ν©

#### merge commit

- κΈ°μ‘΄ master branchμ λ³κ²½μ¬ν­μ΄ μμ΄ λ³ν© μ»€λ° λ°μ

```bash
(master) $ git merge feature-a
Already up to date!
Merge made by the 'recursive' strategy.
```

1. feature-a branchλ‘ μ΄λ ν commit
2. master branch commit
3. mater branchλ‘ λ³ν©



## π Github Flow

- Githubμμ μ μνλ λΈλμΉ μ λ΅



### κΈ°λ³Έ μμΉ

1. **master branchλ λ°λμ λ°°ν¬ κ°λ₯ν μνμ¬μΌ νλ€.**
2. **feature branchλ κ° κΈ°λ₯μ μλλ₯Ό μ μ μλλ‘ μμ±νλ€.**
3. **Commit messageλ λ§€μ° μ€μνλ©°, λͺννκ² μμ±νλ€.**
4. **Pull Requestλ₯Ό ν΅ν΄ νμμ μ§ννλ€.**
5. **λ³κ²½μ¬ν­μ λ°μνκ³  μΆλ€λ©΄, master branchμ λ³ν©νλ€.**



### 1. Feature Branch Workflow

- Shared repository model (μ μ₯μμ μμ κΆμ΄ **μλ** κ²½μ°)

![img](https://velog.velcdn.com/images/drata313/post/f13d0d75-b059-451a-87fe-5edab6a6a90f/image.png)

1. κ° μ¬μ©μλ μκ²©μ μ₯μμ μμ κΆμ κ°μ§ μν. λ°λΌμ **clone**μ ν΅ν΄ μ μ₯μλ₯Ό λ‘μ»¬μ λ³΅μ 
2. κΈ°λ₯ μΆκ°λ₯Ό μν΄ branch μμ± λ° κΈ°λ₯ κ΅¬ν
3. κΈ°λ₯ κ΅¬ν ν μκ²©μ μ₯μμ branch λ°μ
4. λ³ν© μλ£ ν λ³ν© μλ£λ branch μ­μ 
5. master branchλ‘ switch
6. λ³ν©λ masterμ λ΄μ©μ pull
7. μκ²©μ μ₯μμμ λ³ν© μλ£λ λ‘μ»¬ branch μ­μ 
8. μλ‘μ΄ κΈ°λ₯ μΆκ°λ₯Ό μν΄ branch μμ± λ° κ³Όμ  λ°λ³΅



### 2. Forking Workflow

- Fork & Pull model (μ μ₯μμ μμ κΆμ΄ **μλ** κ²½μ°)

![img](https://velog.velcdn.com/images/drata313/post/eb07867f-f881-4d15-bea1-aea9a30cd2d1/image.png)

1. μμ κΆμ΄ μλ μκ²©μ μ₯μλ₯Ό forkλ₯Ό ν΅ν΄ λ³΅μ 
2. λ‘μ»¬μ μ₯μλ₯Ό μλ³Έ μκ²©μ μ₯μμ λκΈ°ννκΈ° μν΄ URLμ μ°κ²°
3. κΈ°λ₯ μΆκ°λ₯Ό μν΄ branch μμ± λ° κΈ°λ₯ κ΅¬ν
4. κΈ°λ₯ κ΅¬ν ν μκ²©μ μ₯μμ branch λ°μ
5. μλ³Έ μμ μμκ² Pull Request
6. μλ³Έ μμ μκ° λ³ν©
7. λ³ν© μλ£ ν λ³ν© μλ£λ branch μ­μ 
8. master branchλ‘ switch
9. λ³ν©λ masterμ λ΄μ©μ pull
10. μκ²©μ μ₯μμμ λ³ν© μλ£λ λ‘μ»¬ branch μ­μ 
11. μλ‘μ΄ κΈ°λ₯ μΆκ°λ₯Ό μν΄ branch μμ± λ° κ³Όμ  λ°λ³΅



> Shared Repository Modelκ³Ό Fork & Pull Modelμ κ°μ₯ ν° μ°¨μ΄μ μ μμμκ° ν΄λΉ νλ‘μ νΈ μ μ₯μμ **μ§μ μ μΈ push κΆνμ΄ μλμ§**μ μ¬λΆμ΄λ€.
