# სიტყვის რიცხვი ტექსტში
# შექმენი ფუნქცია, რომელიც მიიღებს ტექსტს და გამოითვლის, რამდენი სიტყვაა ამ ტექსტში.


def words(goa):
    words = goa.split()  
    return len(words)  
word = "keygbuvytryuuwgiyguiwg5u"
print(words(word))
