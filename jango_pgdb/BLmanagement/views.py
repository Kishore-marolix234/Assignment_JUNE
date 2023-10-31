from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Author, Book, User
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

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

@csrf_exempt
def updateAuthor(request):
    try:
        data = json.loads(request.body)
        authId = data.get('authorId')
        new_name = data.get('changedName')

        if authId is not None and new_name is not None:
            try:
                authObj = Author.objects.get(id=authId)
                old_name = authObj.name
                Author.objects.filter(id=authId).update(name=new_name)

                return JsonResponse({
                    "message": f"{old_name} is replaced by {new_name}"
                })
            except Author.DoesNotExist:
                return JsonResponse({
                    "error": "Author with the given ID does not exist."
                }, status=status.HTTP_404_NOT_FOUND)
        else:
            return JsonResponse({
                "error": "Invalid request body. 'authorId' or 'changedName' field is missing."
            }, status=status.HTTP_400_BAD_REQUEST)
    except json.JSONDecodeError:
        return JsonResponse({
            "error": "Invalid JSON in request body."
        }, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def deleteAuthor(request):
    try:
        data = json.loads(request.body)
        authId = data.get('authorId')

        if authId is not None:
            try:
                authObj = Author.objects.get(id=authId)
                name = authObj.name
                authObj.delete()

                return JsonResponse({
                    "message": f"{name} is deleted from the author table"
                })
            except Author.DoesNotExist:
                return JsonResponse({
                    "error": "Author with the given ID does not exist."
                }, status=status.HTTP_404_NOT_FOUND)
        else:
            return JsonResponse({
                "error": "Invalid request body. 'authorId' field is missing."
            }, status=status.HTTP_400_BAD_REQUEST)
    except json.JSONDecodeError:
        return JsonResponse({
            "error": "Invalid JSON in request body."
        }, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def register(request):
    if request.method != "POST":
        return JsonResponse({
            "error": "Method not supported",
            "status": "Failed"
        }, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    try:
        data = json.loads(request.body)
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')

        if not username or not email or not password:
            return JsonResponse({
                "error": "Input fields should not be empty"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(email=email, username=username, password=password)
        user.save()

        return JsonResponse({
            "message": f"User {username} registered successfully"
        }, status=status.HTTP_201_CREATED)
    except json.JSONDecodeError:
        return JsonResponse({
            "error": "Invalid JSON in request body."
        }, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def login(request):
    if request.method != "POST":
        return JsonResponse({
            "error": "Method not supported",
            "status": "Failed"
        }, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return JsonResponse({
                "error": "Input fields should not be empty"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)

            return JsonResponse({
                "access-token": str(refresh.access_token),
                "refresh-token": str(refresh)
            })
        else:
            return JsonResponse({
                "error": "Invalid username or password."
            }, status=status.HTTP_401_UNAUTHORIZED)
    except json.JSONDecodeError:
        return JsonResponse({
            "error": "Invalid JSON in request body."
        }, status=status.HTTP_400_BAD_REQUEST)