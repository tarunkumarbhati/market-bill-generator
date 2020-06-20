from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from bills import models

# Create your views here.
def home(request):
	context = {}
	items = models.Item.objects.all()
	context['items'] = items
	return render(request, 'home.html', context)


def get_bill(request):
	context = {}
	item_codes = request.POST.getlist('item_code')
	
	# getting counts of items bought
	item_counts = {}
	for item_code in item_codes:
		try:
			item_counts[item_code] += 1
		except:
			item_counts[item_code] = 1

	# finding items on which discounts need to be applied
	discounted_items = {}
	rules = models.Discountrule.objects.filter(purchased_item_code__in=item_codes)
	if rules:
		for rule in rules:
			purchased_item_count = item_counts.get(rule.purchased_item_code, 0)
			if purchased_item_count >= rule.min_purchased_item_required:
				discounted_item_limit = None
				if rule.discounted_item_limit:
					discounted_item_limit = rule.discounted_item_limit
				elif rule.discounted_item_limit_percent:
					discounted_item_limit =  int(purchased_item_count * (rule.discounted_item_limit_percent)/100)
				item_dict = {
					'coupon': rule.coupon,
					'discounted_price': rule.discounted_price,
					'discount_percent': rule.discount_percent,
					'discounted_item_limit': discounted_item_limit
				}
				try:
					discounted_items[rule.discounted_item_code].append(item_dict)
				except:
					discounted_items[rule.discounted_item_code] = [item_dict]

	# getting prices of items bought
	items = models.Item.objects.filter(code__in=item_codes)
	item_prices = {item.code:item.price for item in items}

	# getting bill
	data = []
	for item_code in item_codes:
		item_price = item_prices.get(item_code, 0.0)
		data.append({
			'item':	item_code,
			'coupon':'',
			'price': item_price
		})

		# appending discount if applicable
		if discounted_items.get(item_code):
			discounts = discounted_items[item_code]
			for discount in discounts:
				# if limit is given
				if discount['discounted_item_limit'] is not None:
					# if under limit
					if discount['discounted_item_limit'] > 0:
						discount['discounted_item_limit'] -= 1
						price_discount = 0.0
						if discount['discounted_price']:
							price_discount = item_price - discount['discounted_price']
						elif discount['discount_percent']:
							price_discount = item_price * (discount['discount_percent']/100)
						data.append({
							'item':	'',
							'coupon': discount['coupon'],
							'price': -price_discount
						})
				# if no limit is given
				else:
					price_discount = 0.0
					if discount['discounted_price']:
						price_discount = item_price - discount['discounted_price']
					elif discount['discount_percent']:
						price_discount = item_price * (discount['discount_percent']/100)
					data.append({
						'item':	'',
						'coupon': discount['coupon'],
						'price': -price_discount
					})

	# finding total price
	total_price = 0.0
	for value in data:
		total_price += value['price']

	context['data'] = data
	context['total_price'] = total_price
	return JsonResponse(context)