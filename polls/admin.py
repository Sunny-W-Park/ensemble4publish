from django.contrib import admin
from polls.models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    pass

class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
            'question',
            'choice_text',
            'votes',
            )
    pass

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)

# Register your models here.
