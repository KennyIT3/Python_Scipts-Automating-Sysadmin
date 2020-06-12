#Making Bar Chart
#python

number= [4,12,19,21,7] # List

print("Listing the numbers for the bar chart", "\n")
print(f'Index{"Value":>8}  Bar')

for index, value in enumerate(number):
    print(f'{index:>5}{value:>8}  {"*" * value}')
