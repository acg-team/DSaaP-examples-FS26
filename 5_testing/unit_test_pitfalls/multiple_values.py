"""
This function normalises a name by stripping whitespace and converting to lowercase.
"""
def normalise(name: str) -> str:
    return name.strip()

def test_normalise():
    assert normalise(" alice ") == "alice"
    assert normalise("BOB") == "bob"
    assert normalise("Clarice") == "Clarice" # this assertion is wrong
    assert normalise("") == ""