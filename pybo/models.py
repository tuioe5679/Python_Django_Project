from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)   # 계정 삭제시 데이터 전부 삭제
    subject = models.CharField(max_length=200)
    modify_date = models.DateTimeField(null=True, blank=True)     # 수정 일시
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 질문 삭제시 해당 데이터 전부 삭제
    modify_date = models.DateTimeField(null=True, blank=True)          # 수정 일시
    content = models.TextField()
    create_date = models.DateTimeField()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
