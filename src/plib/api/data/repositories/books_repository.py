from api.data.models.book import Book

class BookRepository:

    def get_all(self):
        return Book.objects.all()
    
    def get_by_id(self, id):
        return Book.objects.get(id=id)
