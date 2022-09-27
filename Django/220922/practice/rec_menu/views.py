from random import random
from turtle import ScrolledCanvas
from django.shortcuts import render
import random

# Create your views here.
def index(request):
    # 식사 메뉴를 추천해준다.
    foods_list = [
      {'food': '한식', 'src': "https://d12zq4w4guyljn.cloudfront.net/pre_20220613080113_photo1_5a3cb6fd4c6f.jpg"},
      {'food': '양식', 'src': "https://sitem.ssgcdn.com/21/49/21/item/1000044214921_i1_1200.jpg"},
      {'food': '일식', 'src': "https://sjnfzdfjrjgl1655541.cdn.ntruss.com/goods/3/2019/07/145_tmp_f7c8f96eb1c66d3e1381d4b53400033a3540view.jpg"},
      {'food': '분식', 'src': "https://oneroommaking.com/web/product/big/202007/3d339eb5bed5d80a3e3aa5cbe7f916b0.jpg"},
      {'food': '동남아 음식', 'src': "https://s3.ap-northeast-2.amazonaws.com/meesig/v3/prod/image/item/main/558/76869e84936143ef90f404b62c81c63f20180327102629"},
      {'food': '패스트푸드', 'src': "https://cdn.hkbs.co.kr/news/photo/201707/f73f50cc829b583c00104e7b83a3dbfe083924.jpg"},
      {'food': '멕시코 음식', 'src': "https://post-phinf.pstatic.net/MjAxODEyMTlfNDgg/MDAxNTQ1MTg0MzUzODA3.ya0LaPX7eIa3EZG4yJ2kk799kErRuXGYvc-GYIddijAg.aEDZfb2IE_6a58jGTvaq7VtbfVUbGr6bSf3C7e-t6Xsg.PNG/2018-12-18_17%3B20%3B58.PNG?type=w1200"},
      {'food': '가볍게', 'src': "https://health.chosun.com/site/data/img_dir/2021/05/06/2021050601029_0.jpg"},
    ]
    food = random.choice(foods_list)
    context = {
        # '변수명': value
        'food': food
    }
    return render(request, 'index.html', context)


def korean(request):
    # 한식을 추천해준다.
    korean_list = [
        {'name': '고등어정식', 'src': "https://t1.daumcdn.net/cfile/tistory/9905C4425F656D2A24"},
        {'name': '족발이랑 보쌈', 'src': "https://post-phinf.pstatic.net/MjAxOTA4MTlfMjgy/MDAxNTY2MTkzNDgyMDU5.k8dyis-tMy0GSiPkQDLveNQ8WEnpDpUg6fzAd-SAmXsg.LqfuUotXOPuObkao5cMb1Iqczzu2osIILHcjP3Vgf78g.JPEG/image_2219871881566193468342.jpg?type=w1200"},
        {'name': '솥밥', 'src': "https://www.smlounge.co.kr/upload/woman/article/202005/thumb/44963-412993-sampleM.jpg"},
    ]
    korean = random.choice(korean_list)
    context = {
        # '변수명': value
        'korean': korean
    }

    return render(request, 'korean.html', context)
