from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseNotFound
import random
from . import models
from . serializers import WordSerializator
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


class RandomWord(APIView):
    def get(self, *args, **kwargs):
        all_words = models.Words.objects.all()
        random_word = random.choice(all_words)
        s_random_word = WordSerializator(random_word, many=False)
        return Response(s_random_word.data)


class NextWord(APIView):
    def get(self, request, pk, format=None):
        word = models.Words.objects.filter(pk__gt=pk).first()
        if not word:
            return HttpResponseNotFound()
        s_next_word = WordSerializator(word, many=False)
        return Response(s_next_word.data)


class GetAllWords(APIView):
    def get(self, *args, **kwargs):
        all_words = models.Words.objects.all()
        s_all_words = WordSerializator(all_words, many=True)
        return Response(s_all_words.data)


class AddWord(APIView):
    def post(self, request):
        data_to_db = JSONParser().parse(request)
        s_new_word = WordSerializator(data=data_to_db)
        if s_new_word.is_valid():
            s_new_word.save()
            return JsonResponse('Добавлено новое слово!', safe=False)
        return JsonResponse('Не удалось добавить новое слово!')