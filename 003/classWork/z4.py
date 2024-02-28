list_1 = [{"V": "S001"}, {"V": "S002"}, 
          {"VI": "S001"}, {"VI": "S005"}, 
          {"VII": "S005"}, {" V ":"S009"}, 
          {" VIII ":"S007"}]
my_set = set()
for i in list_1:
    for j in i.keys():
        my_set.add(i[j])
print(my_set)