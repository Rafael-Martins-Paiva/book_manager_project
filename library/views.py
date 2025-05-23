from django.shortcuts import render

import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .models import Book

def book_management_page(request):
    """Renderiza a página principal de gerenciamento de livros."""
    return render(request, 'library/book_management.html')

@csrf_exempt
@require_http_methods(["GET", "POST"])
def books_api(request):
    """
    API para listar todos os livros (GET) ou adicionar um novo livro (POST).
    GET pode incluir um parâmetro 'search' para filtrar.
    """
    if request.method == "GET":
        search_term = request.GET.get('search', None)
        if search_term:
            books_query = Book.objects.filter(
                Q(title__icontains=search_term) | Q(author__icontains=search_term)
            ).order_by('title')
        else:
            books_query = Book.objects.all().order_by('title')
        
        books_list = [book.to_dict() for book in books_query]
        return JsonResponse({'books': books_list, 'count': len(books_list)})

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            title = data.get('title')
            author = data.get('author')
            isbn = data.get('isbn')
            year_str = data.get('year')

            if not all([title, author, isbn, year_str]):
                return JsonResponse({'error': 'Missing fields'}, status=400)
            
            try:
                year = int(year_str)
            except ValueError:
                return JsonResponse({'error': 'Invalid year format'}, status=400)

            if Book.objects.filter(isbn=isbn).exists():
                return JsonResponse({'error': 'Book with this ISBN already exists'}, status=409)

            book = Book.objects.create(title=title, author=author, isbn=isbn, year=year)
            return JsonResponse({'message': 'Book added successfully!', 'book': book.to_dict()}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            print(f"Error adding book: {e}")
            return JsonResponse({'error': 'An unexpected error occurred'}, status=500)


@csrf_exempt
@require_http_methods(["DELETE"])
def book_detail_api(request, isbn):
    """
    API para remover um livro específico pelo ISBN (DELETE).
    """
    try:
        book = Book.objects.get(isbn=isbn)
        book.delete()
        return JsonResponse({'message': 'Book removed successfully!'})
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)
    except Exception as e:
        print(f"Error deleting book: {e}")
        return JsonResponse({'error': 'An unexpected error occurred'}, status=500)
