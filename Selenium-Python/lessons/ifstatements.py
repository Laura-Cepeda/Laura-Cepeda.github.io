customer = {
    "Name": "bob smith",
    "age": 17,
    "valid_id": False
}

if customer['age'] >= 18 and  customer['valid_id'] == True:
    print('you are old enough')
elif customer['age'] >= 18 and  customer['valid_id'] == False:
    print('your ID is fake')
else:
    print('you are not old enough,you are only ' + str(customer['age']))

'''
if a condition is true:
take an action
elif second condition is true
 take some action
elif third condition is true
  take some action
elif fourth condition is true
  take some action
'''
