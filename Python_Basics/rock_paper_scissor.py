
winning_combination = [1, 9, 14, 95, 160, 213, 292, 450, 454]

sums_of_total_combinations = []

all_combinations_sum =[]

does_sum_already_exists = False

sum_combination = 0

total_combination_sum_counter = 0

duplicate_combination_sum_counter = 0

counter = 0

for i in winning_combination:
    
    for j in winning_combination:
        if j == i:
            counter = counter + 1
            print(f'counter: {counter}')
            continue
        else:

            for k in winning_combination:
                counter = counter + 1
                if k == i or k == j:
                    #print(f'counter: {counter}  Combination: {i} + {j} + {k} = {sum_combination}')
                    continue
                else:
                    total_combination_sum_counter = total_combination_sum_counter + 1
                    sum_combination = i + j + k
                    try:
                        sums_of_total_combinations.index(sum_combination)
                        print(f'counter: {counter}  Combination: {i} + {j} + {k} = {sum_combination}')
                        
                       
                    except:
                        sums_of_total_combinations.append(sum_combination)
                        print(f'counter: {counter}  Exception: {i} + {j} + {k} = {sum_combination}')

                   