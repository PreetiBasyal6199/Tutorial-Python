# Write a Python program to print all unique values in a dictionary. Go to the editor
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, 
# {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}


sample_data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, 
        {"V":"S009"},{"VIII":"S007"}]

new_list = [list(item.values())for item in sample_data]
print(set(([new_list1[0] for new_list1 in new_list])))

# {'S009', 'S002', 'S005', 'S007', 'S001'}

print(set( item for dict1 in sample_data for item in dict1.values()))
# {'S002', 'S005', 'S007', 'S001', 'S009'}



