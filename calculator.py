model_name = "Claude 3.5 Sonnet"
prompt_words = 5000
cost_per_1k_words = 0.015
number_of_users = 10
total_cost = (prompt_words / 1000) * cost_per_1k_words
grand_total_cost = total_cost * number_of_users

print(f"Grand total cost for {number_of_users} users using {model_name} with {prompt_words} prompt words is: ${grand_total_cost}")