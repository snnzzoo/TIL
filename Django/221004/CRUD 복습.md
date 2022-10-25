###### 10월 4일

# 🤠 Django CRUD

> Django : 파이썬 기반 웹 프레임워크



## 1️⃣ 가상환경 및 Django 설치

> 가상환경 : 프로젝트별 별도 패키지 관리



### 1) 가상환경 생성 및 실행

- 가상환경 폴더를 `.gitignore`로 설정해 둔다.

```bash
$ python -m venv venv
$ source venv/Scripts/activate
(venv)
```



### 2) Django 설치 및 기록

```bash
$ pip install django==3.2.13
$ pip freeze > requirements.txt
```



## 2️⃣ Django 프로젝트 생성

```bash
$ django-admin startproject pjt .
```

```bash
$ python manage.py runserver
```



- settings.py를 통해 세부사항 설정 가능

```python
# pjt/settings.py

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```



## 3️⃣ app 생성 및 등록

> Django : 주요 기능 단위의 App 구조, App 별로 MTV 구조를 가지는 모습 + `urls.py`



### 1) app 생성

```bash
$ python manage.py startapp articles
```



### 2) app 등록

- `settings.py` 파일의 `INSTALLED_APPS`에 추가

```python
# pjt/settings.py

INSTALLED_APPS = [
    'articles',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```



### 3) urls.py 설정

![img](복습.assets/201809040404_11170924002333_1.jpg)

> url은 경로를 의미한다.



```python
# pjt/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```



- articles 앱 하위에 urls.py 파일 생성

```python
# articles/urls.py

from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
]
```

> app 단위로 url을 관리할 수 있다!!



- 활용 : `articles:index` ➡ `/articles/`

  - template에서의 활용 예시

  ```django
  {% url 'articles:index' %}
  ```

  - view에서의 활용 예시

  ```python
  return redirect('articles:index')
  ```



### 4) view 함수 생성

```python
# articles/views.py

from django.shortcuts import render

# 요청 정보를 받아서
def index(request):
    # 페이지를 render
    return render(request, 'articles/index.html')
```



### 5) template 생성

- articles에 templates 폴더 생성
  - templates 폴더 내부에 다시 articles 폴더 생성
    - index.html

```html
<!-- articles/index.html -->

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1>게시판</h1>
    <a href="{% url 'articles:new' %}">글쓰기</a>
  </body>
</html>
```



## 4️⃣ Model

### 1) 모델 정의 (DB 설계)

#### 1. 클래스 정의

```python
# articles/models.py

from django.db import models
from django.forms import DateTimeField

# Create your models here.
'''
게시판 기능
- 제목
- 내용
- 글 작성시간 / 수정시간 (자동으로 기록, 날짜/시간)
'''

# 모델 설계 (DB 스키마 설계)
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```



#### 2. migration 파일 생성 및 DB 반영

```bash
$ python manage.py makemigrations # 마이그레이션 파일 생성
$ python manage.py migrate # DB에 반영
```

> articles 폴더 내의 `migrations` 폴더에 생성된 파일 확인



## 5️⃣ CRUD 기능 구현

### 1) Create

> 사용자에게 HTML Form을 제공, 입력한 데이터를 처리



urls.py

```python
# articles/urls.py

from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    # http://127.0.0.1:8000/articles/new/
    path('new/', views.new, name='new'),
    # http://127.0.0.1:8000/articles/create/
    path('create/', views.create, name='create'),
]
```



views.py

```python
# articles/views.py

from django.shortcuts import render, redirect
from .models import Article

# 요청 정보를 받아서
def index(request):
    # 페이지를 render
    return render(request, 'articles/index.html')

# 구상하기
# 게시글 DB에 생성하고 index 페이지로 redirect
def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    Article.objects.create(title=title, content=content)
    return redirect('articles:index')
```



new.html

```django
<!-- articles/new.html -->

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1>글 작성하기</h1>
    <!-- form : 사용자에게 양식을 제공하고
    값을 받아서 (input : name, value)
    서버에 전송 (form : action, method)하는 역할 -->
    <form action="{% url 'articles:create' %}">
      <label for="title">제목 : </label>
      <input type="text" name="title" id="title" />
      <label for="content">내용 : </label>
      <textarea name="content" id="content" cols="30" rows="10"></textarea>
      <input type="submit" value="글쓰기" />
    </form>
  </body>
</html>
```



### 2) Read

> DB에서 게시글을 가져와서, template에 전달



views.py

```python
# articles/views.py

from django.shortcuts import render, redirect
from .models import Article

# 요청 정보를 받아서
def index(request):
    # 게시글을 가져와서
    articles = Article.objects.order_by('-pk') # 최근 작성된 글이 상단에
    # template에 전달한다.
    context = {
        'articles': articles
    }
    # 페이지를 render
    return render(request, 'articles/index.html', context)

# 구상하기
# 게시글 DB에 생성하고 index 페이지로 redirect
def new(request):
    article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/new.html', context=context)

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    Article.objects.create(title=title, content=content)
    return redirect('articles:index')
```



index.html

```django
<!-- articles/index.html -->

...

<body>
  <h1>게시판</h1>
  <a href="{% url 'articles:new' %}">글쓰기</a>
  {% for article in articles %}
  <h3>{{ article.title }}</h3>
  <p>{{ article.created_at }} | {{ article.updated_at }}</p>
  <hr />
  {% endfor %}
</body>
```



#### [번외] Create - POST로 제출하기

> - **GET**
>   - url
>     - .../articles/create/?title=123&content=123
>   - views.py
>     - request.GET
> - **POST**
>   - url
>     - .../articles/create/
>   - views.py
>     - request.POST



new.html

```html
<!-- articles/new.html -->

...

<body>
  <h1>글 작성하기</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    <label for="title">제목 : </label>
    <input type="text" name="title" id="title" />
    <label for="content">내용 : </label>
    <textarea name="content" id="content" cols="30" rows="10"></textarea>
    <input type="submit" value="글쓰기" />
  </form>
</body>
```



views.py

```python
# articles/views.py

from django.shortcuts import render, redirect
from .models import Article
...

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    Article.objects.create(title=title, content=content)
    return redirect('articles:index')
```



#### \* Django ModelForm

> 선언된 모델에 따른 필드 구성
>
> 1. Form 생성
> 2. 유효성 검사



- articles 하위에 forms.py 파일 생성

```python
# articles/forms.py

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'
        # fields를 통해 필요한 것만 가져올 수 있음
        # 예시 : fields = ['title', 'content']
```



views.py

```python
# articles/views.py

from django.shortcuts import render, redirect
from .models import Article

def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

# new를 제거하고 create에서 전부 처리 가능!!

# def new(request):
#     article_form = ArticleForm()
#     context = {
#        'article_form': article_form
#     }
#     return render(request, 'articles/new.html', context=context)

# 유효성검사도 가능
def create(request):
    if request.method == 'POST':
        # DB에 저장하는 로직
        article_form = ArticleForm(request.POST)
        # 유효한 경우
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
        # 유효하지 않은 경우 => 웹 사이트들은 어떻게 처리할까?
    else:
        article_form = ArticleForm()
    context ={
        'article_form': article_form
    }
    return render(request, 'articles/new.html', context=context)
```



new.html

```django
<!-- articles/new.html -->

...

<body>
  <h1>글 작성하기</h1>

  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %} {{ article_form.as_p }}
    <!-- 기존의 form을 대체한다. -->
    <!-- 각 필드가 단락(<p> 태그)으로 감싸져서 렌더링 -->
    <!--
        <label for="title">제목 : </label>
        <input type="text" name="title" id="title">
        <label for="content">내용 : </label>
        <textarea name="content" id="content" cols="30" rows="10"></textarea> -->
    <input type="submit" value="글쓰기" />
  </form>
</body>
```



### 3) Read - 상세보기

> 특정한 글을 본다.



urls.py

```python
# articles/urls.py

from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    # http://127.0.0.1:8000/articles/new/
    # path('new/', views.new, name='new'),
    # http://127.0.0.1:8000/articles/create/
    path('create/', views.create, name='create'),
    # http://127.0.0.1:8000/articles/<int:pk>
    path('<int:pk>/', views.detail, name="detail"),
]
```



views.py

```python
# articles/views.py

from django.shortcuts import render, redirect
from .models import Article
...

def detail(request):
    article = Article.objecst.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)
```



detail.html

```html
<!-- articles/detail.html -->

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1>{{ article.pk }}번 게시글</h1>
    <p>
      작성 일시 : {{ article.create_at }} | 수정 일시 : {{ article.updated_at }}
    </p>
    <p>{{ article.content }}</p>
    <a href="{% url 'articles:update' article.pk %}">수정하기</a>
  </body>
</html>
```



### 4) 수정하기

> 특정한 글을 수정한다.
> ➡ 사용자에게 수정할 수 있는 양식을 제공하고(GET), 특정한 글을 수정한다(POST).



urls.py

```python
# articles/urls.py

from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    # http://127.0.0.1:8000/articles/new/
    # path('new/', views.new, name='new'),
    # http://127.0.0.1:8000/articles/create/
    path('create/', views.create, name='create'),
    # http://127.0.0.1:8000/articles/<int:pk>
    path('<int:pk>/', views.detail, name="detail"),
    # http://127.0.0.1:8000/articles/<int:pk>/update
    path('<int:pk>/update/', views.update, name="update"),

]
```



views.py

```python
# articles/views.py

from django.shortcuts import render, redirect
from .models import Article
...

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        # POST : input 값을 가져와서, 검증하고, DB에 저장
        article_form = ArticleForm(request.POST, instance=article)
        # 특정한 글을 수정하는 것이기 때문에 인스턴스를 반드시 넘겨주어야 함
        # 유효성 검사 통과하면 => 저장하고, 상세보기 페이지로
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)
        # 유효성 검사를 통과하지 않으면 => context 줄부터 해서 오류메시지가 담긴 article_form을 랜더링
    else:
        # GET : Form을 제공
        article_form = ArticleForm(instance=article)
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/update.html', context)
```



update.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>글 수정하기</h1>
  <form action="{% url 'articles:update' %}" method="POST"></form>
  {% csrf_token %}
  {{ article_form.as_p }}
  <input type="submit" value="수정하기">
  </form>
</body>
</html>
```



### 5) 삭제하기

> 특정한 글을 삭제한다.
> http://127.0.0.1:8000/articles/<int:pk>/delete



urls.py

```python

```



views.py

```python

```



#### 📃 추천 문서

- [HTTP request & response objects](https://docs.djangoproject.com/en/4.1/ref/request-response/)
- [ModelForm](https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/)
- [Django view shortcut functions](https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/)
