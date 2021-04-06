# Create your views here.


from django.http import JsonResponse
from django.shortcuts import render


def index_view(request):
    if request.method == "POST":

        # 柱状图的数据
        datas = [5, 20, 36, 10, 10, 20]

        # 返回数据
        return JsonResponse({'bar_datas': datas})
    else:
        return render(request, 'index.html', )

