import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "market.settings")
application = get_wsgi_application()
from bills.models import Discountrule
import csv

RULES_CSV = "discount_rules.csv"

def save_discount_rules(csv_file):
	with open(csv_file) as _csv_file:
		csv_reader = csv.reader(_csv_file, delimiter=',')
		i = -1
		for row in csv_reader:
			i += 1
			if i == 0:
				continue
			try:
				min_purchased_item_required = row[2] if row[2] else None
				discounted_price = row[4] if row[4] else None
				discount_percent = row[5] if row[5] else None
				discounted_item_limit = row[6] if row[6] else None
				discounted_item_limit_percent = row[7] if row[7] else None
				Discountrule(
					coupon = row[0],
					purchased_item_code = row[1],
					min_purchased_item_required = min_purchased_item_required,
					discounted_item_code = row[3],
					discounted_price = discounted_price,
					discount_percent = discount_percent,
					discounted_item_limit = discounted_item_limit,
					discounted_item_limit_percent = discounted_item_limit_percent
				).save()
				print("Saved row:",str(i))
			except Exception as e:
				print("Error on row "+str(i)+" : ",str(e))
	print("Completed.")


if __name__ == '__main__':
	Discountrule.objects.all().delete()
	save_discount_rules(RULES_CSV)