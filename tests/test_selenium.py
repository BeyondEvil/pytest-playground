import pytest
from time import sleep


def test_pass(driver):
    driver.get("https://www.duckduckgo.com")
    sleep(2)
    assert "DuckDuckGo" in driver.title


def test_fail(driver):
    driver.get("https://www.duckduckgo.com")
    sleep(2)
    assert "Google" in driver.title


@pytest.mark.skip
def test_skip(driver):
    driver.get("https://www.duckduckgo.com")
    sleep(2)
    assert "DuckDuckGo" in driver.title


@pytest.mark.xfail(reason="Cause I said so!")
def test_xfail(driver):
    driver.get("https://www.duckduckgo.com")
    sleep(2)
    assert "Gulag" in driver.title
