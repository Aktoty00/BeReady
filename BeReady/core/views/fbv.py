from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from authAB_.models import Student
from ..models import Lesson
from ..serializers import LessonLongSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def lesson_detail(request, pk):
    try:
        lesson = Lesson.objects.get(id=pk)
    except Lesson.DoesNotExist as e:
        return Response({'error': f'{e}'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LessonLongSerializer(lesson)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = LessonLongSerializer(instance=lesson, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'DELETE':
        lesson.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def students_lesson(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    lessons = student.lessons.all()
    serializer = LessonLongSerializer(lessons, many=True)
    return JsonResponse(serializer.data, safe=False)
