import sqlite3
import pandas as pd
import plotly.offline as plo
import plotly.graph_objects as go
import plotly.express as px
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def main_home(request):
    result={}
    return render(request, 'main_home.html', context=result)

def tech(request):
    category = request.GET.get('category')
    conn = sqlite3.connect('./polls/scraping_db/wadizdb.sqlite3')
    cur = conn.cursor()
    tech_total_data = pd.read_sql('select * from  table_tech', con = conn)
    x_data = tech_total_data['review']
    y_data = tech_total_data['star grade']

    def make_react_data(val):
        if (1 <= val < 4):
            return 'Negative'
        elif (4 <= val < 6):
            return 'Positive'
        else:
            return None

    react_data = y_data.apply(lambda val:make_react_data(val))
    react = react_data.value_counts()

    labels = ['긍정', '부정']
    values = [react['Positive'], react['Negative']]
    result = {'labels':labels, 'values':values}
    return render(request, 'tech.html', context=result)

def fashion(request):
    result={}
    return render(request, 'fashion.html', context=result)

def beauty(request):
    result={}
    return render(request, 'beauty.html', context=result)

def food(request):
    result={}
    return render(request, 'food.html', context=result)

def living(request):
    result={}
    return render(request, 'living.html', context=result)

def service(request):
    result={}
    return render(request, 'service.html', context=result)

def analysis(request):  ## html 파일 하나로 처리
    category = request.GET.get('category')
    conn = sqlite3.connect('../polls/scraping_db/wadizdb.sqlite3')
    cur = conn.cursor()
    df = pd.read_sql_query("SELECT * FROM table"+category+"", conn) # 해당 카테고리의 DB를 불러옴
# 시각화 자료 데이터 첨부

    result={}
    return render(request, 'analysis.html', context=result)