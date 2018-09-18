from django.contrib import admin
from .models import Question, Choice


# 표로 보기 TabularInline
# 줄로 보기 StackedInline

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2 # 2개의 여유빈칸 생성

class QuestionAdmin(admin.ModelAdmin):
    # 순서 바꾸기
    # fields = ['pub_date', 'question_text']
    #나눠보기 질문, 날짜별로 큰 이름 나누기
    fieldsets= [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline] # 선택란 같이 보기
    list_display = ('question_text','pub_date') # 레코드 리스트 질문,날짜
    list_filter = ['pub_date'] # 날짜 필터 생성
    search_fields = ['question_text'] # 검색박스 추가


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)