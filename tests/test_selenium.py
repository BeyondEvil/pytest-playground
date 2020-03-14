from time import sleep


def test_base():
    assert True


def test_selenium1(driver):
    driver.get("https://www.google.com")
    sleep(5)
    assert "Google" in driver.title


def test_selenium2(driver):
    driver.get("https://www.google.com")
    sleep(5)
    assert "Google" in driver.title


def test_selenium3(driver):
    driver.get("https://www.google.com")
    sleep(5)
    assert "Google" in driver.title


def test_selenium4(driver):
    driver.get("https://www.google.com")
    sleep(5)
    assert "Google" in driver.title
