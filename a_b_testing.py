# A-B-Testing-at-Nosh-Mish-Mosh
The Nosh Mish Mosh is a recipe and ingredient meal delivery service. Nosh Mish Mosh wants to run an experiment to see if we can convince more people to purchase meal plans if we use a more artisanal-looking vegetable selection


import noshmishmosh
import numpy as np

all_visitors = noshmishmosh.customer_visits
paying_visitors = noshmishmosh.purchasing_customers

total_visitor_count = len(all_visitors)
paying_visitor_count = len(paying_visitors)

baseline_percent = paying_visitor_count * 100.0 / total_visitor_count 

print baseline_percent

payment_history = noshmishmosh.money_spent
average_payment = np.mean(payment_history)

new_customers_needed = np.ceil(1240/average_payment)
perecentage_point_increase = 100.0 * new_customers_needed / total_visitor_count
print perecentage_point_increase

minimum_detectable_effect = (perecentage_point_increase / baseline_percent) * 100.0
print minimum_detectable_effect
ab_sample_size = 300
