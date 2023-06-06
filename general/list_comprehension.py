test_list = ["Hello" , "World"]
test_list2 = [2,4,5]
test_list3 = [3,4,5]
test_dict = { "test1" : test_list , "test2" : test_list2 , "test3" : test_list3}
another_list = [test * test2 for test,test2 in zip(test_list,test_list2)]
test_dict["test1"]
another_dict = [test2 * test3 for test2,test3 in zip(test_dict["test2"],test_dict["test3"])]
another_dict
list2 = [i**2 if i > 2 else i for i in [1,2,3,4,5]]
list2