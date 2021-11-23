from automation import __version__
from automation.automation import find_emails,find_phone_number

def test_version():
    assert __version__ == '0.1.0'


test_string = """aaron84@gmail.com
aguilarjoseph@hinton-hardin.org
ajohnson@frazier.com
008-445-7591
026-957-0947
027-008-1146
"""

def test_find_phone_number():
    actual = find_phone_number(test_string)
    expected = ['008-445-7591','026-957-0947','027-008-1146']
    assert actual == expected

def test_find_emails():
    actual = find_emails(test_string)
    expected = ['aaron84@gmail.com','aguilarjoseph@hinton-hardin.org','ajohnson@frazier.com']
    assert actual == expected