# Market Bill Generator

Generates a bill for items purchased by applying coupon rules as you keep on adding the items.

## Getting Started

1. Clone this repo.
2. Add/Update items & their prices in 'item_prices.csv', if required.
3. Add/Update rules for discount & coupons in 'discount_rules.csv', if required.
4. Run start.sh file, it will add the prices & rules and start the container.
```
bash start.sh
```
Open this url on browser to add items in basket & generate bill:-

```
http://127.0.0.1:8000
```
### Prerequisites

Install docker to run the project.
A Linux system will be required, preferebly Ubuntu 16.04.

## Item Prices CSV Format

You can add/update the prices if you want.

* Item Code - The Code of item.
* Name - Name of item.
* Price - Price of the item.


Following prices for items are already added in the csv:-

```
+--------------|--------------|---------+
| Product Code |     Name     |  Price  |
+--------------|--------------|---------+
|     CH1      |   Chai       |  $3.11  |
|     AP1      |   Apples     |  $6.00  |
|     CF1      |   Coffee     | $11.23  |
|     MK1      |   Milk       |  $4.75  |
|     OM1      |   Oatmeal    |  $3.69  |
+--------------|--------------|---------+
```


## Discount Rules CSV Format

You can add/update the rules if you want.


* Coupon - The coupon code.
* Purchased Item Code - Code of the item required to buy for coupon to be valid.
* Min Purchased Item Required - Minimum items required to buy for the coupon to be applicable. Default is 1, if left blank.
* Discounted Item Code - Code of item on which discount will be applied.
* Discounted Price - New price of item on which discount will be applied. Leave blank if not applicable.
* Discounted Percent - Percent off on the orignal price of item on which discount will be applied. Leave blank if not applicable.
* Discounted Item Limit - Limit on number of items a discount/coupon can be applied. Leave blank if you want no limit.
* Discounted Item Limit Percent - Precent limit on number of items a discount/coupon can be applied, with respect to purchased item. Limit is calculated by multiplying it to purchased item count.


Following Rules are already added in the csv:-

1. BOGO -- Buy-One-Get-One-Free Special on Coffee. (Unlimited)
2. APPL -- If you buy 3 or more bags of Apples, the price drops to $4.50.
3. CHMK -- Purchase a box of Chai and get milk free. (Limit 1)
4. APOM -- Purchase a bag of Oatmeal and get 50% off a bag of Apples
