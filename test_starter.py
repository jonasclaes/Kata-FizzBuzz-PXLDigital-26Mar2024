from fizzbuzzgame import FizzBuzzGame


def test_that_play_returns_1_when_input_int_1():
    assert FizzBuzzGame().play(1) is 1


def test_that_play_returns_2_when_input_int_2():
    assert FizzBuzzGame().play(2) is 2


def test_that_play_returns_string_fizz_when_given_int_3():
    assert FizzBuzzGame().play(3) is "Fizz"


def test_that_play_returns_int_4_when_given_int_4():
    assert FizzBuzzGame().play(4) is 4


def test_that_play_returns_string_buzz_when_given_int_5():
    assert FizzBuzzGame().play(5) is "Buzz"


def test_that_play_returns_string_fizz_when_given_int_6():
    assert FizzBuzzGame().play(6) is "Fizz"


def test_that_play_returns_string_fizz_when_given_int_9():
    assert FizzBuzzGame().play(9) is "Fizz"


def test_that_play_returns_string_buzz_when_given_int_10():
    assert FizzBuzzGame().play(10) is "Buzz"


def test_that_play_returns_string_fizzbuzz_when_given_int_15():
    assert FizzBuzzGame().play(15) is "FizzBuzz"


def test_that_play_returns_string_buzz_when_given_int_20():
    assert FizzBuzzGame().play(20) is "Buzz"


def test_that_play_returns_string_fizzbuzz_when_given_int_30():
    assert FizzBuzzGame().play(30) is "FizzBuzz"


def test_that_play_returns_string_fizzbuzz_when_given_int_45():
    assert FizzBuzzGame().play(45) is "FizzBuzz"
