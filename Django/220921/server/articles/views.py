from django.shortcuts import render
import random

# Create your views here.
def index(request):
    # 환영하는 메인 페이지를 보여준다.
    names = ['안선민', '김수지', '방수경', '임선주', '이주현']
    name = random.choice(names)
    context = {
        # '변수명': value
        'name': name,
        'img': 'https://t3.ftcdn.net/jpg/01/76/98/40/360_F_176984023_8I82qQPmKn8TqNAZXIYMCSiwccoUiPBg.jpg',
    }
    return render(request, 'index.html', context)

def welcome(request, name):
    # 사람들이 /welcome/본인이름 을 입력하면, 환영 인사와 이름을 동시에 보여준다.
    # print(name)
    context ={
        'name': name,
        # list => 반복으로 순회해서 출력
        'greetings': [
            '안녕하세요', 'hello', 'guten tag', 'bon jour'
        ],
        'img': [
            'https://t3.ftcdn.net/jpg/01/76/98/40/360_F_176984023_8I82qQPmKn8TqNAZXIYMCSiwccoUiPBg.jpg',
            'https://t3.ftcdn.net/jpg/01/76/98/40/360_F_176984023_8I82qQPmKn8TqNAZXIYMCSiwccoUiPBg.jpg',
            'https://t3.ftcdn.net/jpg/01/76/98/40/360_F_176984023_8I82qQPmKn8TqNAZXIYMCSiwccoUiPBg.jpg',
        ],
    }
    return render(request, 'welcome.html', context)

def greeting(request):
    foods = ['apple', 'banana', 'coconut',]
    info = {
        'name': 'Alice'
    }
    context = {
        'foods': foods,
        'info': info,
    }
    return render(request, 'greeting.html', context)

def dinner(request):
    foods = ['족발', '햄버거', '치킨', '초밥',]
    pick = random.choice(foods)
    context = {
        'pick': pick,
        'foods': foods,
    }
    return render(request, 'dinner.html', context)


