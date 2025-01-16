def odd_index_sum(numbers):

    return sum(numbers[i] 
    for i in range(1,len(numbers),2))
                                                                                         
print(odd_index_sum([1, 2, 3, 4, 5, 6]))  # აქ დაგვიბრუნდება ციფრების ჯამი(2+4+6)