from django.db import models

# Create your models here.
class Question(models.Model):
    Question_text = models.CharField(max_length=150)
    pub_date = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.Question_text   #can see the question on admin


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=150)
    votes = models.IntegerField()


    def __str__(self):
        return self.choice_text             #can see the question

