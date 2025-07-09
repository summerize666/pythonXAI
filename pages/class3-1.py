# 連續使用if跟使用if elif else的差別
# elif可以排除前面有判斷成功的情況,所以縮短判斷條件的副雜難度,也解省了時間
# 但是如果是使用東個if來判斷,則每個if都會被執行,所以效率較低
for i in range(5):
    print(i)
    print("Hellow")
for i in range(1, 5):
    print(i)
    print("Hellow")
for i in range(1, 10.2):
    print(i)
