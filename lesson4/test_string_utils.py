import pytest
from string_utils import StringUtils

utils = StringUtils()

#capitilize

def test_capitilize():
    #Pozitiv
    assert utils.capitilize("apple") == "Apple" 
    assert utils.capitilize("let's go") == "Let's go"
    assert utils.capitilize("567") == "567"
    #Negativ
    assert utils.capitilize(" ") == " "
    assert utils.capitilize("") == ""
    assert utils.capitilize("56абв") == "56абв"

    #trim

@pytest.mark.parametrize('string, result', [
    #Pozitiv 
    (" apple", "apple"),
    (" let's go ", "let's go "),
    ( "567" ),
    #Negativ
    ("", ""),
    (" ", "")
])
def test_contains(string, result):
    res = utils.trim(string)
    assert res == result

    #to_list
    
@pytest.mark.parametrize('string, delimeter, result', [
    #Positiv                      
    ("собака,кошка,хомяк", ",", ["собака", "кошка", "хомяк"]),
    ("1,2,3,4", ",", ["1", "2", "3", "4"]),
    ("%!&!*","!", ["%", "&", "*"]),
])   
def test_to_list(string, delimeter, result):
    res = utils.to_list(string, delimeter)
    assert res == result

@pytest.mark.parametrize('string, delimeter, result', [
     #Negativ
    ("", None, [])
])
def test_to_list(string, delimeter, result):
    res = utils.to_list(string)
    assert res == result

    #contains   

@pytest.mark.parametrize('string, symbol, result', [
    ("хомяк", "х", True),
    ("дерево", "е", True),
    ("бело-красный", "-", True),
    ("56789", "7", True),
    ("", "", True),
    (" ", " ", True),
    ("кошка", "н", False),
    ("Ксюша", "к", False),
    ("$%&!", "-", False),
    ("56789", "f", False),
    ("", "п", False)
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result

    #delete_symbol

@pytest.mark.parametrize('string, symbol, result', [
    #Pozitiv
    ("собака", "б", "соака"),
    ("бело-красный", "-", "белокрасный"),
    ("56789", "6", "5789"),
    ("blue sky", " ", "bluesky"),
     #Negativ
    ("собака", "п", "собака"),
    ("бело-красный", " ", "бело-красный"),
    ("", " ", ""),
    (" ", "", " "),
    ("собака", "", "собака"),
    ("собака", " ", "собака")
])    
def test_deiete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result

    #starts_with

@pytest.mark.parametrize('string, symbol, result', [
    #Pozitiv
    ("хомяк", "х", True),
    ("Черное море", "Ч", True),
    (" хомяк", " ", True),
    ("white", "w", True),
    ("56789", "5", True),
    ("", "", True),
    #Negativ
    ("кошка", "о", False),
    ("Катя", "т", False),
    (" собака", "с", False),
    ("", "т", False),
    ("  ", "b", False)
 ])        
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result

    #end_with

@pytest.mark.parametrize('string, symbol, result', [
    #Pozitiv
    ("хомяк", "к", True),    
    ("Черное море", "е", True),
    ("хомяк ", " ", True),
    ("white", "e", True),
    ("56789", "9", True),
    ("", "", True),
    #Negativ
    ("кошка", "о", False),
    ("Катя", "т", False),
    (" собака", "с", False),
    ("", "т", False),
    ("  ", "b", False)
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result

    #is_empty

@pytest.mark.parametrize('string, result', [ 
   #Pozitiv
   ("", True),
   (" ", True),
   ("  ", True),
   #Negativ
   ("абв", False),
   (" абв", False),
   ("56789", False)
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result

    #list_to_string

@pytest.mark.parametrize('lst, joiner, result', [
    #Pozitiv
    (["собака", "кошка", "хомяк"], ",", "собака,кошка,хомяк"),
    (["a", "b", "c"], ",", "a,b,c"),
    (["а", "б", "в"], ",", "а,б,в"),
    (["красное", "белое"], "", "красноебелое"),  
    (["темный", "лес"], "-", "темный-лес"),                 
     #Negativ      
    ([], ",", ""), 
    ([], "абв", "")          
])    
def test_list_to_string(lst, joiner, result):
    res = utils.list_to_string(lst, joiner)
    assert res == result   

@pytest.mark.parametrize('lst, joiner, result', [
    #Pozitiv
    ([1, 2, 3], None, "1, 2, 3"),
    #Negativ 
    ([], None, "")
])
def test_list_to_string(lst, joiner, result):
    res = utils.list_to_string(lst)   
    assert res == result                