income = int(input())
# Took an input for income on which tax is to be calculated
# lets take an example of income 5500000

if income <= 250000:
    tax = 0

elif income <= 500000:
    tax = (income - 250000) * 0.05

#                          👆
# if income is lower than this segment then there will be no tax from prev segments

elif income <= 750000:
    tax = (income - 500000) * 0.10 + 12500
# tax from prev seg=(500000 - 250000)*0.05=12500

elif income <= 1000000:
    tax = (income - 750000) * 0.15 + 37500
# tax from prev segs=12500+(750000 - 500000)*0.10=12500+25000=37500

elif income <= 1250000:
    tax = (income - 1000000) * 0.20 + 75000
# tax from prev segs=37500+(1000000 - 750000)*0.15=37500+37500=75000

elif income <= 1500000:
    tax = (income - 1250000) * 0.25 + 125000
# tax from prev segs=75000+(1250000- 1000000)*0.20=75000+50000=125000

else:
    tax = (income - 1500000) * 0.30 + 187500
# tax from prev segs=125000+(1500000- 1250000)*0.25=125000+62500=187500

# tax for income 5500000 will be 1387500. ((5500000 - 1500000) * 0.30 + 187500)

# Whatever amount is added in the taxes of a segment is the total sum of prev tax segments
# and this is how tax paying works

# This is for surcharge segment
if income < 5000000:
    tax += 0
elif income > 5000000 and income <= 10000000:  # between 5000000 and 10000000
    tax += tax * 0.10
elif income > 10000000 and income <= 20000000:
    tax += tax * 0.15
elif income > 20000000 and income <= 50000000:
    tax += tax * 0.25
else:
    tax += tax * 0.37

# tax will be tax * 1.10 because income > 5000000 and income <= 10000000
print(tax)

# Let's say there is an additional charge of 4% on tax
# for health and education cess purpose
print(tax*1.04)
