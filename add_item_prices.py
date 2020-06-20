import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "market.settings")
application = get_wsgi_application()
from bills.models import Item
import csv

ITEMS_CSV = "item_prices.csv"

def save_item_prices(csv_file):
	with open(csv_file) as _csv_file:
		csv_reader = csv.reader(_csv_file, delimiter=',')
		i = -1
		for row in csv_reader:
			i += 1
			if i == 0:
				continue
			try:
				Item(
					code = row[0],
					name = row[1],
					price = row[2],
				).save()
				print("Saved row:",str(i))
			except Exception as e:
				print("Error on row "+str(i)+" : ",str(e))
	print("Completed.")


if __name__ == '__main__':
	Item.objects.all().delete()
	save_item_prices(ITEMS_CSV)