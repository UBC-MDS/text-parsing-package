"""
Unit tests for the count_unique_words function in the count_unique_words module.
This test file aims to validate the output for this function given some 
expected input data and unexpected edge case input data.
"""

# Import the count_unique_words function from the count_words module in the package
from text_parsing_package.count_words import count_unique_words

def test_expected_input():
    """
    Test count_unique_words with a simple expected inputs.
    """

    normal_input_example_1 = 'I go where I go'
    assert count_unique_words(normal_input_example_1) == {'I': 2, 'go': 2, 'where': 1}

    normal_input_example_2 = 'The the the thing'
    assert count_unique_words(normal_input_example_2, ignore_words=['the']) == {'thing': 1}

    normal_input_example_3 = "I'll be home soon!"
    assert count_unique_words(normal_input_example_3, count_punc=True) == {''}

def test_unexpected_input():
    """
    Test count_unique_words with a simple unexpected inputs.
    """
    ...
    



regular_texts = [
    "I'll be home soon!",
    "Hey can you send me 15$ for the pizza from last night",
    "Can you etransfer me back please, thank you!",
    "We need to go to the grocery store NOW!!!",
    "Yo I just got so much FREE stuff from the garage sale",
    "Hey, checkout this icloud link, it has the photos we took over the weekend!",
]


# text1 = 'I went to UBC today to study WENT.'
# print(count_unique_words(text1,[]))
# print(count_unique_words(text1,['.'],ignore_case=True))
# print(count_unique_words(text1,['.']))
# print(count_unique_words(text1,'.'))

# text2 = "I'd love to watch Interstellar tonight but I can't! I don't know why but I love the black hole scene!!!"
# print(count_unique_words(text2,[',',"'",'!']))
# print(count_unique_words(text2,[',','!'],ignore_case=True))

# def unit_test_count_unique_words():
#     ''' Check that count_unique_words can handle duplicates properly'''
#     assert count_unique_words('was to was',None) == {'was':2,'to':1}
    
#     '''Check that empy string returns empty dict'''
#     assert count_unique_words('',None)=={}
    
#     '''Check ignore case works properly'''
#     assert count_unique_words(text1,'.',ignore_case=True) != count_unique_words('I went to UBC today to study WENT.','.')
#     assert count_unique_words(text1,['.'],ignore_case=True) == {'i': 1, 'went': 2, 'to': 2, 'ubc': 1, 'today': 1, 'study': 1}

#     '''Check case sensitivity for same word'''
#     assert all(val==1 for val in count_unique_words('Blue blue BLuE bLue blUE...','.').values())

#     '''Check multiple punctuation removal functionality'''
#     assert count_unique_words('this, that!, everything?.',[',','!','?','.']) == {'this':1,'that':1,'everything':1}

#     return "All Tests Passed √"

# def demonstrate_error(text, punctuation):
#     try:
#         count_dict = count_unique_words(text,punctuation)
#     except Exception as e: 
#         print(e, type(e))
#         return e
        
# demonstrate_error([2],None)
# demonstrate_error('The greatest Ever.',[1,'.'])

# unit_test_count_unique_words()