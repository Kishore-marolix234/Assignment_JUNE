from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Author, Book

# Create your views here.
@csrf_exempt
def createAuthor(request):
    try:
        my_json = json.loads(request.body)
        nameComingFromPostman = my_json['name']
        author = Author(name=nameComingFromPostman)
        author.save()
        return JsonResponse({
            "Message": f"{nameComingFromPostman} saved in author table"
        })
    except KeyError:
        return JsonResponse({
            "Error": "Invalid request body. 'name' field is missing."
        }, status=400)
    except json.JSONDecodeError:
        return JsonResponse({
            "Error": "Invalid JSON in request body."
        }, status=400)

@csrf_exempt
def createBooks(request):
    try:
        requestBodyToDict = json.loads(request.body)
        authorId = requestBodyToDict['author_id']
        author = Author.objects.get(id=authorId)
        Books = requestBodyToDict['title']

        bookLists = []

        for book in Books:
            bookLists.append(book)
            newBook = Book.objects.create(title=book, author=author)

        return JsonResponse({
            "message": f"{bookLists} of {author.name} added successfully"
        })
    except KeyError:
        return JsonResponse({
            "Error": "Invalid request body. 'author_id' or 'title' field is missing."
        }, status=400)
    except json.JSONDecodeError:
        return JsonResponse({
            "Error": "Invalid JSON in request body."
        }, status=400)
    except Author.DoesNotExist:
        return JsonResponse({
            "Error": "Author with the given ID does not exist."
        }, status=404)

def getBooknamesFromAuthor(request):
    try:
        authId = (json.loads(request.body))['authorId']
        author = Author.objects.get(id=authId)
        booksQuerySet = Book.objects.filter(author=author)
        bookLists = []

        for book in booksQuerySet:
            bookLists.append(book.title)

        return JsonResponse({
            "message": f"{bookLists} of {author.name} retrieved successfully"
        })
    except KeyError:
        return JsonResponse({
            "Error": "Invalid request body. 'authorId' field is missing."
        }, status=400)
    except json.JSONDecodeError:
        return JsonResponse({
            "Error": "Invalid JSON in request body."
        }, status=400)
    except Author.DoesNotExist:
        return JsonResponse({
            "Error": "Author with the given ID does not exist."
        }, status=404)


