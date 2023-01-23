
def test_verbosity():
    command01 = "Hello all how are you. I am fine. How about others. And others. And others!!!!!!"+\
                "And what a nice day"
    command02 = "Hello all how are you. I am fine. How about others. And others. And others!!!!!!"+\
                "And, what a nice day"
    assert command01 == command02

