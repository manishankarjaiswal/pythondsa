lis = [[1,2,3], [20], [2,4,8], [1,1], [15], [11,2,4], [40], [1,2], [1,3,2], [48]]
class Book:
    def __init__(self, ch):
        self.ch = ch
        self.total_q = sum(ch)

    @staticmethod
    def print_book_obj(book_lis):
        for i in book_lis:
            print(i.ch)

book_obj_lis = [Book(i) for i in lis]
# Book.print_book_obj(book_obj_lis)

sorted_book_obj_lis = sorted(book_obj_lis, key=lambda x : x.total_q, reverse=True)
Book.print_book_obj(sorted_book_obj_lis)



new_book_lis = []
n = len(sorted_book_obj_lis)
# print('---> n', n)
for i in range(n):
    if sorted_book_obj_lis[i].total_q == -1:
        continue
    # print(sorted_book_obj_lis[i].ch)
    if sorted_book_obj_lis[i].total_q > 30 :
        new_book_lis.append(sorted_book_obj_lis[i].ch)
        # del(book_obj_dic[i.total_q])
        sorted_book_obj_lis[i].total_q = -1
    else:
        new_book_obj = []
        new_book_obj.extend(sorted_book_obj_lis[i].ch)
        # sorted_book_obj_lis[i].total_q = -1
        
        if sorted_book_obj_lis[i].total_q < 30 :
            # book_obj_dic_lis = sorted(list(book_obj_dic.keys()), reverse = True)
            # print(i,)
            for j in range(i+1,n) :
                # print(i,j)
                if sorted_book_obj_lis[j].total_q != -1 and sorted_book_obj_lis[j].total_q + sorted_book_obj_lis[i].total_q < 30:
                    new_book_obj.extend(sorted_book_obj_lis[j].ch)
                    sorted_book_obj_lis[i].total_q += sorted_book_obj_lis[j].total_q
                    sorted_book_obj_lis[j].total_q = -1
            
            # break
            
        new_book_lis.append(new_book_obj)   
        sorted_book_obj_lis[i].total_q = -1
print('-------------> new book', new_book_lis)
# new_book_lis