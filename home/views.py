import sqlite3
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def main_home(request):
    result={}
    return render(request, 'main_home.html', context=result)

def total(request):
    # 100% stacked barh graph
    conn = sqlite3.connect('./polls/scraping_db/wadizdb.sqlite3')
    cur = conn.cursor()
    tech_total_data = pd.read_sql('select * from table_tech', con=conn)
    food_total_data = pd.read_sql('select * from table_food', con=conn)
    fashion_total_data = pd.read_sql('select * from table_fashion', con=conn)
    living_total_data = pd.read_sql('select * from table_living', con=conn)
    beauty_total_data = pd.read_sql('select * from table_beauty', con=conn)

    def make_y_data(val):
        if (1 <= val < 2):
            return 1
        elif (2 <= val < 3):
            return 2
        elif (3 <= val < 4):
            return 3
        elif (4 <= val < 5):
            return 4
        elif (5 <= val < 6):
            return 5
        else:
            return None

    ## beauty
    beauty_y_data = beauty_total_data['star grade'].apply(lambda val: make_y_data(val))
    beauty_rate_data = beauty_y_data.value_counts()
    beauty_rate = (beauty_rate_data/len(beauty_total_data))*100
    ## fashion
    fashion_y_data = fashion_total_data['star grade'].apply(lambda val: make_y_data(val))
    fashion_rate_data = fashion_y_data.value_counts()
    fashion_rate = (fashion_rate_data/len(fashion_total_data)) * 100
    ## food
    food_y_data = food_total_data['star grade'].apply(lambda val: make_y_data(val))
    food_rate_data = food_y_data.value_counts()
    food_rate = (food_rate_data / len(food_total_data)) * 100
    ## living
    living_y_data = living_total_data['star grade'].apply(lambda val: make_y_data(val))
    living_rate_data = living_y_data.value_counts()
    living_rate = (living_rate_data / len(living_total_data)) * 100
    ## tech
    tech_y_data = tech_total_data['star grade'].apply(lambda val: make_y_data(val))
    tech_rate_data = tech_y_data.value_counts()
    tech_rate = (tech_rate_data / len(tech_total_data)) * 100

    y_bar = ['beauty', 'fashion', 'food','living','tech']
    x_group_list_1 = [beauty_rate[1], fashion_rate[1], food_rate[1], living_rate[1], tech_rate[1]]
    x_group_list_2 = [beauty_rate[2], fashion_rate[2], food_rate[2], living_rate[2], tech_rate[2]]
    x_group_list_3 = [beauty_rate[3], fashion_rate[3], food_rate[3], living_rate[3], tech_rate[3]]
    x_group_list_4 = [beauty_rate[4], fashion_rate[4], food_rate[4], living_rate[4], tech_rate[4]]
    x_group_list_5 = [beauty_rate[5], fashion_rate[5], food_rate[5], living_rate[5], tech_rate[5]]

    y_group_ov = y_bar
    x_group_1 = x_group_list_1
    x_group_2 = x_group_list_2
    x_group_3 = x_group_list_3
    x_group_4 = x_group_list_4
    x_group_5 = x_group_list_5

    context={'y_group_ov':y_bar,'x_group_1':x_group_list_1,'x_group_2':x_group_list_2,'x_group_3':x_group_list_3,'x_group_4':x_group_list_4,'x_group_5':x_group_list_5}

    return render(request, 'total.html', context)

def tech(request):
    category = request.GET.get('category')
    conn = sqlite3.connect('./polls/scraping_db/wadizdb.sqlite3')
    cur = conn.cursor()
    tech_total_data = pd.read_sql('select * from  table_tech', con = conn)
    x_data = tech_total_data['review']
    y_data = tech_total_data['star grade']

    def make_y_data(val):
        if (1 <= val < 2):
            return 1
        elif (2 <= val < 3):
            return 2
        elif (3 <= val < 4):
            return 3
        elif (4 <= val < 5):
            return 4
        elif (5 <= val < 6):
            return 5
        else:
            return None

    y_data = y_data.apply(lambda val: make_y_data(val))
    rate_data = y_data.value_counts()

    x = ['☆☆☆☆★', '☆☆☆★★', '☆☆★★★', '☆★★★★', '★★★★★'],
    y = [rate_data[1], rate_data[2], rate_data[3], rate_data[4], rate_data[5]]

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
    result = {'x':x, 'y':y, 'labels':labels, 'values':values}
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

def analysis(request):  ## html 파일 하나로 처리 (total 제외)
    category = request.GET.get('category')
    conn = sqlite3.connect('../polls/scraping_db/wadizdb.sqlite3')
    cur = conn.cursor()
    df = pd.read_sql_query("SELECT * FROM table_"+category+"", conn) # 해당 카테고리의 DB를 불러옴
# 시각화 자료 데이터 첨부

    result={}
    return render(request, 'analysis.html', context=result)