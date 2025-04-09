# Write your code here
month_bubblegum = 202
month_toffee = 118
month_icecream = 2250
month_milkchocolate = 1680
month_doughnut = 1075
month_pancake = 80
income = round(float(month_bubblegum + month_toffee + month_icecream + month_milkchocolate + month_doughnut + month_pancake), 1)

print(f"""Earned amount:
Bubblegum: ${month_bubblegum},
Toffee: ${month_toffee}
Ice cream: ${month_icecream}
Milk chocolate: ${month_milkchocolate}
Doughnut: ${month_doughnut}
Pancake: ${month_pancake}

Income: ${income}""")
expenses = 0.0
print("Staff expenses:" )
expenses += int(input())
print("Other expenses:")
expenses += int(input())
print(f"Net income: ${income - expenses}")


