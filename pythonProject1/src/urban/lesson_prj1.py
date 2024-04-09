print('Hello World')

var_data_1 = float(23891471923807487.142352314353455)
var_data_2 = 23891471923807487.142352314356734
var_data_3 = 23891471923843245.142352314334563
var_data_4 = 23891471923843245.142352314334553

sum_var_1_3 = var_data_1 + var_data_3
sum_var_2_4 = var_data_2 + var_data_4

result = sum_var_1_3 > sum_var_2_4
# print("--->>> <<< ---")
# print("--->>> РЕЗУЛЬТАТ: ", result)
# print("--->>> <<< ---\n")

# print("--->>> <<< ---")
# print("--->>> <<< ---\n")

# print("--->>> Число 1 = ", var_data_1.normalize())
print("Число 1 = ", var_data_1)
print("Число 2 = ", var_data_2)
print("Число 3 = ", var_data_3)
print("Число 4 = ", var_data_4)

# print(f'---->>> {var_data_1:.10f}')
print(f'---->>> {var_data_1}')

print("Сумма чисел 1 и 3 = ", sum_var_1_3)
# print("\n")
print("Сумма чисел 2 и 4 = ", sum_var_2_4)
# print("\n")

if sum_var_1_3 > sum_var_2_4:
    # print("\n")
    print("Сумма чисел 1 и 3 БОЛЬЩЕ суммы 2 и 4 ")
    # print("\n")
    # print("TRUE (ПРАВДА)")
else:
    # print("\n")
    print("Сумма чисел 2 и 4 БОЛЬЩЕ суммы 1 и 3 ")
    # print("\n")
    # print("TRUE (ПРАВДА)")

    # print("\n")
    print("--->>> <<< ---\n")
print("--->>> <<< ---")
print("--->>> РЕЗУЛЬТАТ: ", result)
print("--->>> <<< ---\n")