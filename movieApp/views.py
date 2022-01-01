# -*- coding:utf-8 -*-
from rest_framework import generics
from movieApp.models import movie  # , movieAllInfo
from countryApp.models import country
from ratingApp.models import rating
from movieApp.serializers import MovieSerializer  # , allMovieSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.db.models import Q
from string import Template
from django.db import connection
import random


def template(input: str):
    countryname = 'test'
    t = Template(
        "select movieApp_movie.mid as id,movieApp_movie.title,movieApp_movie.m_intro,movieApp_movie.poster from movieApp_movie  join countryApp_country on movieApp_movie.mid  = countryApp_country.mid where countryApp_country.c_name = $countryname")
    return t.substitute(countryname='"' + input + '"')


@api_view(['GET'])
def getAll(self):
    try:
        firstIndex = 0
        limitIndex = 100
        queryset = movie.objects.all().order_by('-mid')[firstIndex:limitIndex]
        result = MovieSerializer(queryset, many=True)
        response = JsonResponse(result.data, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        print(e)


@api_view(['POST'])
def getMovie(request):
    try:
        print(request.data)
        firstIndex = int(request.data['params'].get('currentPage', 1))
        limitIndex = int(request.data['params'].get('pageLimit', 2000))
        typeList = tuple(request.data['params'].get('typeList'))
        year = str(request.data['params'].get('currentYear',2021))


        limitIndex = limitIndex if limitIndex < 2000 else 2000
        firstIndex = (firstIndex - 1) * limitIndex
        cursor = connection.cursor()
        # movieIDList = list(country.objects.filter(c_name=countryname).values_list('mid', flat=True))
        a = f'''select movieApp_movie.mid as id,movieApp_movie.title,movieApp_movie.m_intro,movieApp_movie.poster
               from (movieApp_movie join typeApp_type on (movieApp_movie.mid = typeApp_type.mid)) join yearApp_year on (movieApp_movie.mid = yearApp_year.mid)
               where typeApp_type.t_name in {typeList} and yearApp_year.y_name = '{year}' 
               order by movieApp_movie.mid 
               offset {firstIndex} rows 
               fetch next {limitIndex} rows only'''

        cursor.execute(a)
        result = []
        columns = [column[0] for column in cursor.description]
        for row in cursor.fetchall():
            result.append(dict(zip(columns, row)))
        response = JsonResponse(result, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        cursor.close()
        print("done")
        return response
    except Exception as e:
        print(e)


@api_view(['GET'])
def getMovieByRating(self):
    try:
        cursor = connection.cursor()
        a = '''select top 100 movieApp_movie.mid,movieApp_movie.title,movieApp_movie.m_intro,movieApp_movie.poster,ratingApp_rating.r_name from movieApp_movie join ratingApp_rating on movieApp_movie.mid = ratingApp_rating.mid order by ratingApp_rating.r_name DESC'''
        cursor.execute(a)
        result = []
        columns = [column[0] for column in cursor.description]
        for row in cursor.fetchall():
            result.append(dict(zip(columns, row)))
        response = JsonResponse(result, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        cursor.close()
        print("done")
        return response
    except Exception as e:
        print(e)


@api_view(['POST'])
def getMovieByCountry(request):
    try:
        print(request.data)
        countryname = str(request.data['params'].get('c_name', None))
        offset = int(request.data['params'].get('pagenumber'))
        items_per_page = int(request.data['params'].get('pagelimit', 2000))
        items_per_page = items_per_page if items_per_page < 2000 else 2000
        offset = (offset - 1) * items_per_page
        cursor = connection.cursor()
        # movieIDList = list(country.objects.filter(c_name=countryname).values_list('mid', flat=True))
        a = f'''select movieApp_movie.mid as id,movieApp_movie.title,movieApp_movie.m_intro,movieApp_movie.poster,countryApp_country.c_name
        from movieApp_movie join countryApp_country on movieApp_movie.mid = countryApp_country.mid
        where countryApp_country.c_name like '%{countryname}%' 
        order by movieApp_movie.mid 
        offset {offset} rows 
        fetch next {items_per_page} rows only'''

        cursor.execute(a)
        result = []
        columns = [column[0] for column in cursor.description]
        for row in cursor.fetchall():
            result.append(dict(zip(columns, row)))
        response = JsonResponse(result, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        cursor.close()
        print("done")
        return response
    except Exception as e:
        print(e)


@api_view(['POST'])
def getMovieByType(request):
    try:
        print(request.data)
        typename = str(request.data['params'].get('t_name', None))
        offset = int(request.data['params'].get('pagenumber'))
        items_per_page = int(request.data['params'].get('pagelimit', 2000))
        items_per_page = items_per_page if items_per_page < 2000 else 2000
        offset = (offset - 1) * items_per_page
        # movieIDList = list(country.objects.filter(c_name=countryname).values_list('mid', flat=True))
        test = template(typename)
        a = "select movieApp_movie.mid as id,movieApp_movie.title,movieApp_movie.m_intro,movieApp_movie.poster from movieApp_movie join typeApp_type on movieApp_movie.mid  = typeApp_type.mid where typeApp_type.t_name like '" + typename + "' order by movieApp_movie.mid offset " + str(
            offset) + " rows fetch next  " + str(items_per_page) + " rows only"
        movieList = movie.objects.raw(a)

        result = MovieSerializer(movieList, many=True)
        response = {}
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        response['data'] = result.data
        return JsonResponse(response)
    except Exception as e:
        print(e)


@api_view(['POST'])
def getMovieByYear(request):
    try:
        print(request.data)
        yearname = str(request.data['params'].get('y_name', None))
        offset = int(request.data['params'].get('pagenumber'))
        items_per_page = int(request.data['params'].get('pagelimit', 2000))
        items_per_page = items_per_page if items_per_page < 2000 else 2000
        offset = (offset - 1) * items_per_page
        # movieIDList = list(country.objects.filter(c_name=countryname).values_list('mid', flat=True))
        test = template(yearname)
        a = "select movieApp_movie.mid as id,movieApp_movie.title,movieApp_movie.m_intro,movieApp_movie.poster from movieApp_movie join yearApp_year on movieApp_movie.mid  = yearApp_year.mid where yearApp_year.y_name like '" + yearname + "' order by movieApp_movie.mid offset " + str(
            offset) + " rows fetch next  " + str(items_per_page) + " rows only"
        movieList = movie.objects.raw(a)

        result = MovieSerializer(movieList, many=True)
        response = {}
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        response['data'] = result.data
        return JsonResponse(response)
    except Exception as e:
        print(e)


@api_view(['POST'])
def getMovieByMid(request):
    try:
        print(request.data)
        mid = int(request.data['params'].get('mid', None))
        # offset = int(request.data['pagenumber'])
        # items_per_page = int(request.data.get('pagelimit', 2000))
        # items_per_page = items_per_page if items_per_page < 2000 else 2000
        # movieIDList = list(country.objects.filter(c_name=countryname).values_list('mid', flat=True))
        cursor = connection.cursor()
        a = '''select movieApp_movie.mid as id,movieApp_movie.title,typeApp_type.t_name,yearApp_year.y_name,countryApp_country.c_name,actorApp_actor.a_name,directorApp_director.d_name,movieApp_movie.m_intro,movieApp_movie.poster,ratingApp_rating.r_name
from (((movieApp_movie join yearApp_year on movieApp_movie.mid  = yearApp_year.mid) join (typeApp_type join actorApp_actor
        on typeApp_type.mid = actorApp_actor.mid) on movieApp_movie.mid = typeApp_type.mid) join (directorApp_director
join ratingApp_rating on directorApp_director.mid = ratingApp_rating.mid) on movieApp_movie.mid = directorApp_director.mid)
join countryApp_country on movieApp_movie.mid = countryApp_country.mid
where movieApp_movie.mid  = %s'''
        cursor.execute(a, (mid,))
        result = []
        columns = [column[0] for column in cursor.description]
        for row in cursor.fetchall():
            result.append(dict(zip(columns, row)))
        response = JsonResponse(result, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        cursor.close()
        print("done")
        return response
    except Exception as e:
        print(e)


@api_view(['POST'])
def getMovieByTitle(request):
    try:
        print(request.data)
        titlename = str(request.data['params'].get('title', None))
        offset = int(request.data['params'].get('pagenumber'))
        items_per_page = int(request.data['params'].get('pagelimit', 2000))
        items_per_page = items_per_page if items_per_page < 2000 else 2000
        offset = (offset - 1) * items_per_page
        # movieIDList = list(country.objects.filter(c_name=countryname).values_list('mid', flat=True))
        # titlename = "%"+titlename+"%"
        # a = "select movieApp_movie.mid as id,movieApp_movie.title,movieApp_movie.m_intro,movieApp_movie.poster from movieApp_movie  where movieApp_movie.title like '"+"%" + titlename +"%" +"' order by movieApp_movie.mid offset " + str(offset) + " rows fetch next  " + str(items_per_page) + " rows only"
        cursor = connection.cursor()
        a = f'''select movieApp_movie.mid as id,movieApp_movie.title,movieApp_movie.m_intro,movieApp_movie.poster
from movieApp_movie
where movieApp_movie.title like '%{titlename}%' 
order by movieApp_movie.mid 
offset {offset} rows 
fetch next {items_per_page} rows only

'''

        cursor.execute(a)
        result = []
        columns = [column[0] for column in cursor.description]
        for row in cursor.fetchall():
            result.append(dict(zip(columns, row)))
        response = JsonResponse(result, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        cursor.close()
        print("done")
        return response
    except Exception as e:
        print(e)


@api_view(['POST'])
def getMovieByDirector(request):
    try:
        print(request.data)
        directorname = str(request.data['params'].get('d_name', None))
        offset = int(request.data['params'].get('pagenumber'))
        items_per_page = int(request.data['params'].get('pagelimit', 2000))
        items_per_page = items_per_page if items_per_page < 2000 else 2000
        offset = (offset - 1) * items_per_page
        # movieIDList = list(country.objects.filter(c_name=countryname).values_list('mid', flat=True))
        # titlename = "%"+titlename+"%"
        # a = "select movieApp_movie.mid as id,movieApp_movie.title,movieApp_movie.m_intro,movieApp_movie.poster from movieApp_movie  where movieApp_movie.title like '"+"%" + titlename +"%" +"' order by movieApp_movie.mid offset " + str(offset) + " rows fetch next  " + str(items_per_page) + " rows only"
        cursor = connection.cursor()
        a = f'''select movieApp_movie.mid as id,movieApp_movie.title,movieApp_movie.m_intro,movieApp_movie.poster,directorApp_director.d_name
from movieApp_movie join directorApp_director on movieApp_movie.mid = directorApp_director.mid
where directorApp_director.d_name like '%{directorname}%' 
order by movieApp_movie.mid 
offset {offset} rows 
fetch next {items_per_page} rows only

'''

        cursor.execute(a)
        result = []
        columns = [column[0] for column in cursor.description]
        for row in cursor.fetchall():
            result.append(dict(zip(columns, row)))
        response = JsonResponse(result, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        cursor.close()
        print("done")
        return response
    except Exception as e:
        print(e)


@api_view(['POST'])
def getMovieBySearch(request):
    try:
        print(request.data)
        search = str(request.data['params'].get('search', None))
        offset = int(request.data['params'].get('pagenumber'))
        items_per_page = int(request.data['params'].get('pagelimit', 2000))
        items_per_page = items_per_page if items_per_page < 2000 else 2000
        offset = (offset - 1) * items_per_page
        # movieIDList = list(country.objects.filter(c_name=countryname).values_list('mid', flat=True))
        # titlename = "%"+titlename+"%"
        # a = "select movieApp_movie.mid as id,movieApp_movie.title,movieApp_movie.m_intro,movieApp_movie.poster from movieApp_movie  where movieApp_movie.title like '"+"%" + titlename +"%" +"' order by movieApp_movie.mid offset " + str(offset) + " rows fetch next  " + str(items_per_page) + " rows only"
        cursor = connection.cursor()
        query = f'''select movieApp_movie.mid as id,movieApp_movie.title,countryApp_country.c_name,actorApp_actor.a_name,directorApp_director.d_name,movieApp_movie.poster
from (((movieApp_movie join yearApp_year on movieApp_movie.mid  = yearApp_year.mid) join (typeApp_type join actorApp_actor
        on typeApp_type.mid = actorApp_actor.mid) on movieApp_movie.mid = typeApp_type.mid) join (directorApp_director
join ratingApp_rating on directorApp_director.mid = ratingApp_rating.mid) on movieApp_movie.mid = directorApp_director.mid)
join countryApp_country on movieApp_movie.mid = countryApp_country.mid
where movieApp_movie.title like '%{search}%' or directorApp_director.d_name like  '%{search}%' or actorApp_actor.a_name like '%{search}%' 
'''

        cursor.execute(query)

        result = []
        columns = [column[0] for column in cursor.description]
        for row in cursor.fetchall():
            result.append(dict(zip(columns, row)))

        # result = map(lambda row: dict(zip(columns, row)), cursor.fetchall())
        cursor.close()
        output = {
            'data': result[offset:offset + items_per_page],
            'Access-Control-Allow-Origin': "*",
            'total': len(result)
        }
        return JsonResponse(output)
        print("done")
    except Exception as e:
        print(e)


@api_view(['GET'])
def getRandomMovie(request):
    try:
        randomList = []
        for i in range(0, 20):
            addMid = random.randint(1, 79349)
            randomList.append(addMid)
        randomList = tuple(randomList)
        cursor = connection.cursor()
        a = f'''select movieApp_movie.mid as id,movieApp_movie.title,movieApp_movie.m_intro,movieApp_movie.poster
            from movieApp_movie 
            where movieApp_movie.mid in {randomList}
'''
        cursor.execute(a)
        result = []
        columns = [column[0] for column in cursor.description]
        for row in cursor.fetchall():
            result.append(dict(zip(columns, row)))
        response = JsonResponse(result, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        cursor.close()
        print("done")
        return response
    except Exception as e:
        print(e)
