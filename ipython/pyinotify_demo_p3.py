import pyinotify
wm = pyinotify.WatchManager()
notifier = pyinotify.Notifier(wm)

wm.add_watch('/tmp/', pyinotify.ALL_EVENTS, rec=True)
notifier.loop()
