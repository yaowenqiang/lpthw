import book_pb2
book = book_pb2.Book()
book.isbn = '9780262510875'
book.title = 'Structure and Interpretation of Computer Programs - 2nd Edition'
print(book.SerializeToString())
