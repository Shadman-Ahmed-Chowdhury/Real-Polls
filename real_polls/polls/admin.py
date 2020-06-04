from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "Real Polls Admin"
admin.site.site_title = "Real Polls Admin Area"
admin.site.index_title = "Welcome to the Real Polls Admin"

# Register your models here.

class choiceInLine(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields':['question_text']}), ('Date Information', {'fields':['pub_date'], 'classes':['collapse']}),]
	inlines = [choiceInLine]

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Question)
#admin.site.register(Choice)

