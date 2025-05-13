def find_short(s):
    list1 = s.split(" ")


    word_len = len(list1[0])
    for i in list1:
        if len(i) < word_len:                   #ეს კოდი გვიხსნის როგორ ვიპივოთ ყველაზე პატარა სიტყვა წინადადებაში
            word_len = len(i)
    
    # word_len = 3
    return word_len

print(find_short("bitcoin take over the world maybe who knows perhaps"))




list1 = "apple orange banana peach"
split_list1 = list1.split()  
print("list1 split:", split_list1)

list2 = "cat,dog,bird,snake"
split_list2 = list2.split(',') 
print("list2 split:", split_list2)

list3 = "one five  six nine"
split_list3 = list3.split(' ') 
print("list3 split:", split_list3)

list4 = "12:33:46"
split_list4 = list4.split(':')  
print("list4 split:", split_list4)

list5 = "2006-04-20"
split_list5 = list5.split('-') 
print("list5 split:", split_list5)

list6 = "apple|orange|banana"
split_list6 = list6.split('|')  
print("list6 split:", split_list6)

list7 = "file.name.extension"
split_list7 = list7.split('.')  
print("list7 split:", split_list7)

list8 = "home/user/docs"
split_list8 = list8.split('/')  
print("list8 split:", split_list8)

list9 = "orange#banana#cherry"
split_list9 = list9.split('#')  
print("list9 split:", split_list9)

list10 = "name:igor chik age:18"
split_list10 = list10.split(' ')  
print("list10 split:", split_list10)

