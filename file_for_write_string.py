<<<<<<< HEAD
with open('hello.txt','w')as file:
    for i in range(2,10):
        for j in range(1,10):
            file.write('{}X{}={} '.format(i,j,i*j))
        file.write('\n')
        #file.write('Hello, world! {0}\n'.format(i))
my_dict={'eat':'먹다','love':'사랑하다'}
my_dict['go']='가다'
my_dict['sleep']='자다'
my_dict['walk']='걷다'
my_dict['run']='달리다'
my_dict['see']='보다'
my_dict['sleep']='자다'
my_dict['apple']='사과'
#print(my_dict.items())
my_dict.values()

for i in my_dict:
    file.write(i)

#print('\n---------------')
for key,value in my_dict.items():
    print(key)
    #print('\n')
=======
with open('hello.txt','w')as file:
    for i in range(2,10):
        for j in range(1,10):
            file.write('{}X{}={} '.format(i,j,i*j))
        file.write('\n')
        #file.write('Hello, world! {0}\n'.format(i))
my_dict={'eat':'먹다','love':'사랑하다'}
my_dict['go']='가다'
my_dict['sleep']='자다'
my_dict['walk']='걷다'
my_dict['run']='달리다'
my_dict['see']='보다'
my_dict['sleep']='자다'
my_dict['apple']='사과'
#print(my_dict.items())
my_dict.values()

for i in my_dict:
    file.write(i)

#print('\n---------------')
for key,value in my_dict.items():
    print(key)
    #print('\n')
>>>>>>> 18c0589cd863ddd50038bf9d112beb00982f3dfd
    print(value)