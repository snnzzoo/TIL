from django.shortcuts import render
import random

# Create your views here.


def index(request):
    return render(request, 'index.html')

def number(request, _number):
    context = {
        # "템플릿 변수 이름": 값
        "number": _number,
    }
    return render(request, 'number.html', context)

def text(request):
    text = request.GET.get("_text")
    # index.html에서 입력한 text를 받음
    context = {
        # "템플릿 파일(.html)에서 사용할 변수 이름": 값
        "template_text": text,
    }
    return render(request, 'text.html', context)

def math(request):
    return render(request, 'math.html')


def random(request):
    return render(request, 'random.html')


def flower(request):
    name = request.GET.get('flower')
    flowers = ['라일락', '장미', '해바라기', '물망초', '프리지아', '데이지', '할미꽃', '사루비아',
               '국화', '안개꽃', '무궁화', '민들레꽃', '카네이션', '코스모스', '벚꽃', '튤립', '아카시아', ]
    pick = random.choice(flowers)
    context = {
        'name': name,
        'pick': pick,
        'flowers': flowers,
    }
    return render(request, 'flower.html', context)
