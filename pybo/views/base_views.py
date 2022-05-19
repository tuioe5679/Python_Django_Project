from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question


def index(request):
    # pybo 목록 출력
    # 입력 인자
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('create_date')

    paginator = Paginator(question_list, 10)  # 페이지 당 질문 10개 보여 주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)