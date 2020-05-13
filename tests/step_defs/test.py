chrome = "https://www.google.com/intl/cs/chrome/thank-you.html?statcb=0&installdataindex=empty&defaultbrowser=0"
chrome2 = "https://www.google.com/intl/es-419/chrome/thank-you.html?statcb=0&installdataindex=empty&defaultbrowser=0"

print(chrome[22:])
print(chrome2[:7])
print(chrome.find("/chrome"))
print(chrome2[:chrome2.find("/chrome")])


def test_addition():
    assert 1 + 1 == 2
