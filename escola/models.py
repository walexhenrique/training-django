from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Team(BaseModel):
    name = models.CharField('Nome da turma', max_length=150)
    number = models.IntegerField(verbose_name='Número da sala')

    def __str__(self) -> str:
        return self.name


class Teacher(BaseModel):
    name = models.CharField('Nome do professor', max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Student(BaseModel):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name