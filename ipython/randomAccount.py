import ZODB
import ZODB.FileStorage
import transaction
import Custom_zodb_engine
FileStorage = ZODB.FileStorage.FileStorage('zodb_filestorage.db')
db = ZODB.DB(FileStorage)
conn = db.open()
root = conn.root()
noah = Custom_zodb_engine.Account('noah', 1000)
print(noah)
root['noah'] = noah
jack = Custom_zodb_engine.Account('jack', 2000)
print(jack)
root['jack'] = jack
transaction.commit()
conn.close()
