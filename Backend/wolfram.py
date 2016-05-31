import wolframalpha as wa
while True:
	input=raw_input("enter ur query ")

	try:
		app_id="PYJU9H-GEXX47RAV9"
		line =raw_input("enter ur query ")
		client= wa.Client(app_id)

		res= client.query(line)
		answer= next(res.results).text
	except:
		print "cant find"