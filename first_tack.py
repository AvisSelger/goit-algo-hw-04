file_path = '/mnt/data/developer_salaries.txt'
salaries_data = """Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000"""

with open(file_path, 'w') as file:
    file.write(salaries_data)

file_path

def total_salary(path):
    total = 0
    count = 0
    with open(path, 'r') as file:
        for line in file:
            _, salary = line.strip().split(',')
            total += int(salary)
            count += 1

    average = total / count if count > 0 else 0
    return (total, average)

total_salary_result = total_salary(file_path)
total_salary_result
