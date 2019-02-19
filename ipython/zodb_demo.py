import ZODB
import ZODB.FileStorage
import transaction

filestorage = ZODB.FileStorage.FileStorage("zodb_filestorage.db")

db = ZODB.DB(filestorage)

conn = db.open()

root = conn.root()

root['list'] = ['this', 'is', 'a', 'list']

root['dict'] = {"this":"is", "a":"dict"}

transaction.commit()

conn.close()