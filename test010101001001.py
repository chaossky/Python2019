my_dict={
    'go':'가다',
    'eat':'먹다',
    'run':'달리다',
    'sing':'노래하다',
    'make':'만들다',
    'ask':'물어보다'
}
#print(my_dict)
#print(my_dict['go'])
#print(my_dict['eat'])
#print(my_dict['run'])

for key in my_dict.keys():
    print(key)

for items in my_dict.items():
    print(items)

for values in my_dict.values():
    print(values)
