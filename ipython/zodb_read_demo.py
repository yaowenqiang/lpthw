import ZODB
import ZODB.FileStorage
import transaction

file_storage = ZODB.FileStorage.FileStorage('ZODB_filestorage.db')
db = ZODB.DB(file_storage)

conn = db.open()

root = conn.root()
print(root.items())

conn.close()

