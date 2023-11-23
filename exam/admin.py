from django.contrib import admin
from .models import Result
# Register your models here.
@admin.register(Result)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['student', 'exam', 'marks','date','exam_id']