from linkedin_api import Linkedin
from random import randint
from re import split

linkedin = Linkedin("noah@livestonetech.com", "twiggyboy3")

companies = []

results = linkedin.stub_people_search("Senior Network Architect", count=49, start=randint(0, 100))["data"]["elements"]
for element in results:
	try:
		for snippet in element["hitInfo"]["snippets"]:
			company = split(' at ', snippet["heading"]["text"])
			companies.append(company[len(company)-1])
	except KeyError:
		continue

try:
	companies.remove("present")
except ValueError:
	pass
print(list(set(companies)))
