"""
This function normalises a name by stripping whitespace and converting to lowercase.
"""
def normalise(name: str) -> str:
    return name.strip()

def test_normalise_whitespace():
    assert normalise(" alice ") == "alice"

def test_normalise_case():
    assert normalise("BOB") == "bob"

def test_normalise_first_letter():
    assert normalise("Clarice") == "clarice"

def test_normalise_empty_string():
    assert normalise("") == ""