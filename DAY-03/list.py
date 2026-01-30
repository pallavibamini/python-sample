# # LIST 
# #list allow duplicates,unordered,mutable

#append,insert,pop,remove
# playlist=["shape of you","faded","love it","evvare"]
# fav_food=["biryani","dosa","idly","voda"]
# recen_loc=["hyd","srd","ooty","us"]

# print(playlist)

# playlist.append("perfect")
# print("updated:",playlist)
# playlist.insert(2,"k4u")
# print(playlist)
# playlist.remove("faded")
# print(playlist)
# playlist.pop()
# print(playlist)

#sort,remove , index
# num=[12,33,35,78,90,32,22,33,33]
# num.sort()
# print(num)
# num.reverse()
# print(num)
# print(num.count(33))
# print(num[3])
# print(num[1])
# num[1]=122
# print(num[1])
# print(num)

#indexing
# num=[12,33,35,78,90,32,22,33,33]
# print(num[0:3])
# print(num[-2:])

#iteration

# for n in num:
#     print(num)

playlist=["shape of you","faded","love it","k4u","perfect"]
# if "faded" in playlist: 
#     print("present")  

#with multiple data 

order_summary=["pizza",2,300.09,True]
print(order_summary)

#using enumerate function

for index,item in enumerate(order_summary):
    print(f"Index:{index},item:{item}")