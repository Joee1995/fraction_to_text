from FractionToText import FractionToText

ftt = FractionToText()


def test_number_to_list():
    print(ftt.number_to_list(number='1234567'))


def test_number_to_english():
    print(ftt.number_to_english(number='123'))


def test_number_to_cardinal():
    print(ftt.number_to_cardinal(number='1314520'))


def test_cardinal_to_ordinal():
    cardinal = ftt.number_to_cardinal(number='950902')
    print(ftt.cardinal_to_ordinal(cardinal=cardinal))


def test_number_to_ordinal():
    print(ftt.number_to_ordinal(number='98765'))


def test_covert():
    print(ftt.convert(fraction='132 3/16'))
