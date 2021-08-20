import sqlite3

import konlpy
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from django.shortcuts import render
import tensorflow as tf
from tensorflow import keras

# Create your views here.
from django.http import HttpResponse

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

def make_react_data(val):
    if (1 <= val < 4):
        return 'Negative'
    elif (4 <= val < 6):
        return 'Positive'
    else:
        return None

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
    total_data = pd.read_sql('select * from table_total', con=conn)

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

    # pie graph
    x_data = total_data['review']
    y_data = total_data['star grade']
    react_data = y_data.apply(lambda val: make_react_data(val))
    react_total = react_data.value_counts()

    labels_total = ['긍정', '부정']
    values_total = [react_total['Positive'], react_total['Negative']]

    context={'y_group_ov':y_bar,'x_group_1':x_group_list_1,'x_group_2':x_group_list_2,'x_group_3':x_group_list_3,'x_group_4':x_group_list_4,'x_group_5':x_group_list_5,'labels_total':labels_total, 'values_total':values_total}

    return render(request, 'total.html', context)

def tech(request):
    conn = sqlite3.connect('./polls/scraping_db/wadizdb.sqlite3')
    cur = conn.cursor()
    tech_total_data = pd.read_sql('select * from  table_tech', con = conn)
    x_data_tech = tech_total_data['review']
    y_data_tech = tech_total_data['star grade']
## bar graph
    y_data_tech = y_data_tech.apply(lambda val: make_y_data(val))
    rate_data_tech = y_data_tech.value_counts()

    x_tech = ['★☆☆☆☆', '★★☆☆☆', '★★★☆☆', '★★★★☆', '★★★★★']
    y_tech = [rate_data_tech[1], rate_data_tech[2], rate_data_tech[3], rate_data_tech[4], rate_data_tech[5]]
## pie graph
    react_data_tech = y_data_tech.apply(lambda val:make_react_data(val))
    react_tech = react_data_tech.value_counts()

    labels_tech = ['긍정', '부정']
    values_tech = [react_tech['Positive'], react_tech['Negative']]

    result = {'x_tech':x_tech, 'y_tech':y_tech, 'labels_tech':labels_tech, 'values_tech':values_tech}
    return render(request, 'tech.html', context=result)

def fashion(request):
    conn = sqlite3.connect('./polls/scraping_db/wadizdb.sqlite3')
    cur = conn.cursor()
    fash_total_data = pd.read_sql('select * from  table_fashion', con=conn)
    x_data_fash = fash_total_data['review']
    y_data_fash = fash_total_data['star grade']
    ## bar graph
    y_data_fash = y_data_fash.apply(lambda val: make_y_data(val))
    rate_data_fash = y_data_fash.value_counts()

    x_fash = ['★☆☆☆☆', '★★☆☆☆', '★★★☆☆', '★★★★☆', '★★★★★']
    y_fash = [rate_data_fash[1], rate_data_fash[2], rate_data_fash[3], rate_data_fash[4], rate_data_fash[5]]
    ## pie graph
    react_data_fash = y_data_fash.apply(lambda val: make_react_data(val))
    react_fash = react_data_fash.value_counts()

    labels_fash = ['긍정', '부정']
    values_fash = [react_fash['Positive'], react_fash['Negative']]

    result = {'x_fash': x_fash, 'y_fash': y_fash, 'labels_fash': labels_fash, 'values_fash': values_fash}
    return render(request, 'fashion.html', context=result)

def beauty(request):
    conn = sqlite3.connect('./polls/scraping_db/wadizdb.sqlite3')
    cur = conn.cursor()
    beauty_total_data = pd.read_sql('select * from  table_beauty', con = conn)
    x_data_beauty = beauty_total_data['review']
    y_data_beauty = beauty_total_data['star grade']
## bar graph
    y_data_beauty = y_data_beauty.apply(lambda val: make_y_data(val))
    rate_data_beauty = y_data_beauty.value_counts()

    x_beauty = ['★☆☆☆☆', '★★☆☆☆', '★★★☆☆', '★★★★☆', '★★★★★']
    y_beauty = [rate_data_beauty[1], rate_data_beauty[2], rate_data_beauty[3], rate_data_beauty[4], rate_data_beauty[5]]
## pie graph
    react_data_beauty = y_data_beauty.apply(lambda val:make_react_data(val))
    react_beauty = react_data_beauty.value_counts()

    labels_beauty = ['긍정', '부정']
    values_beauty = [react_beauty['Positive'], react_beauty['Negative']]

    result = {'x_beauty':x_beauty, 'y_beauty':y_beauty, 'labels_beauty':labels_beauty, 'values_beauty':values_beauty}
    return render(request, 'beauty.html', context=result)

def food(request):
    conn = sqlite3.connect('./polls/scraping_db/wadizdb.sqlite3')
    cur = conn.cursor()
    food_total_data = pd.read_sql('select * from  table_food', con=conn)
    x_data_food = food_total_data['review']
    y_data_food = food_total_data['star grade']
    ## bar graph
    y_data_food = y_data_food.apply(lambda val: make_y_data(val))
    rate_data_food = y_data_food.value_counts()

    x_food = ['★☆☆☆☆', '★★☆☆☆', '★★★☆☆', '★★★★☆', '★★★★★']
    y_food = [rate_data_food[1], rate_data_food[2], rate_data_food[3], rate_data_food[4], rate_data_food[5]]
    ## pie graph
    react_data_food = y_data_food.apply(lambda val: make_react_data(val))
    react_food = react_data_food.value_counts()

    labels_food = ['긍정', '부정']
    values_food = [react_food['Positive'], react_food['Negative']]

    result = {'x_food': x_food, 'y_food': y_food, 'labels_food': labels_food, 'values_food': values_food}
    return render(request, 'food.html', context=result)

def living(request):
    conn = sqlite3.connect('./polls/scraping_db/wadizdb.sqlite3')
    cur = conn.cursor()
    living_total_data = pd.read_sql('select * from  table_living', con=conn)
    x_data_living = living_total_data['review']
    y_data_living = living_total_data['star grade']
    ## bar graph
    y_data_living= y_data_living.apply(lambda val: make_y_data(val))
    rate_data_living = y_data_living.value_counts()

    x_living = ['★☆☆☆☆', '★★☆☆☆', '★★★☆☆', '★★★★☆', '★★★★★']
    y_living = [rate_data_living[1], rate_data_living[2], rate_data_living[3], rate_data_living[4], rate_data_living[5]]
    ## pie graph
    react_data_living = y_data_living.apply(lambda val: make_react_data(val))
    react_living = react_data_living.value_counts()

    labels_living = ['긍정', '부정']
    values_living = [react_living['Positive'], react_living['Negative']]

    result = {'x_living': x_living, 'y_living': y_living, 'labels_living': labels_living, 'values_living': values_living}
    return render(request, 'living.html', context=result)

def service(request):
    category = request.GET.get('category',None)
    search = request.GET.get('search',None)

    if category == None or search == None:
        return render(request, 'service.html')
    else:
        path01 = './DeepLearning/files/DL_%s.h5' % category
        loaded_model = tf.keras.models.load_model(path01)
        path02 = './DeepLearning/files/tokenizer_%s.pkl' % category
        tokenizer = pd.read_pickle(path02)
        stopwords = './DeepLearning/files/stopwords.pkl'
        def sentiment_predict(sentence):
            okt = konlpy.tag.Okt()
            new_sentence = [tok for tok in sentence if tok not in stopwords]
            encoded = tokenizer.texts_to_sequences([new_sentence])
            pad_new = tf.keras.preprocessing.sequence.pad_sequences(encoded, maxlen=50)
            score = loaded_model.predict(pad_new)
            return score

        search = request.GET.get('search')
        result = sentiment_predict(search)
        score_max = np.argmax(result)

        negative = (result[0][0] + result[0][1] + result[0][2]) * 100
        positive = (result[0][3] + result[0][4]) * 100
        labels_service = ['negative', 'positive']
        values_service = [negative, positive]
        result01 = {'labels_service': labels_service, 'values_service': values_service}

        return render(request, 'service.html', context=result01)
