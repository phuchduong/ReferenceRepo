hub = sbs.get_event_hub('creditHub')
obj = dir(hub)
for thing in obj:
	print(thing)