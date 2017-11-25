import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def get_webdriver(browser, browser_version, platform, os_version, resolution):
    USERNAME = "anthonyrozon1"
    PASSWORD = "pyx1xfRY4qqkwpsEqSFM"
    if browser.lower() == 'chrome':
        desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities['os'] = platform
    desired_capabilities['os_version'] = os_version
    desired_capabilities['browser_version'] = browser_version
    desired_capabilities['resolution'] = resolution

    return webdriver.Remote(command_executor='http://%s:%s@hub.browserstack.com:80/wd/hub' % (USERNAME, PASSWORD),
                            desired_capabilities=desired_capabilities)


def test_github_user_search(browser, browserstack_flag, browser_version, platform, os_version, resolution):
    driver = get_webdriver(browser, browser_version, platform, os_version, resolution)
    pass_counter = 0
    checks = 0
    github_user_name = "rozon"
    driver.get('https://github.com/')
    driver.maximize_window()

    # Check for page title
    with pytest.allure.step('Check for page title'):
        if "GitHub" in driver.title:
            pass_counter += 1
        checks += 1

    # Check if github performed a search for given username
    with pytest.allure.step('Check if github performed a search for given username'):
        input_github_search = driver.find_element_by_xpath(".//input[contains(@placeholder, 'Search GitHub')]")
        input_github_search.send_keys(github_user_name)
        input_github_search.submit()

        if github_user_name in driver.title:
            pass_counter += 1
        checks += 1

    # Check if github returns any user
    with pytest.allure.step('Check if github returns any user'):
        label_users_search_result = driver.find_element_by_xpath(".//a[contains(@class, 'UnderlineNav-item') and text()='Users']/span")
        github_user_results_count = int(label_users_search_result.text)

        if github_user_results_count > 0:
            pass_counter += 1
        checks += 1

    # Check if github load users results
    with pytest.allure.step('Check if github load users results'):
        try:
            label_users_search_result.click()
            pass_counter += 1
        except Exception as e:
            print(e)
        checks += 1

    # Check if github results returns same amount of users
    with pytest.allure.step('Check if github results returns same amount of users'):
        label_users_search_count = driver.find_element_by_xpath(".//div[contains(@class, 'three-fourths')]/div[1]/h3")
        label = label_users_search_count.get_attribute('text')
        print(label)
        label_number = label[0:2]
        print(label_number)
        label_to_int = int(label_number)
        print(label_to_int)

        if github_user_results_count == label_to_int:
            pass_counter += 1
        checks += 1

    # Check if github user url appears on results table
    with pytest.allure.step('Check if github user url appears on results table'):
        label_user_profile = driver.find_element_by_xpath(".//em[text()='" + github_user_name + "']")

        try:
            label_user_profile.click()
            pass_counter += 1
        except Exception as e:
            print(e)
        checks += 1

    # Check if github profile is shown on browser
    with pytest.allure.step('Check if github profile is shown on browser'):
        if github_user_name in driver.title:
            pass_counter += 1
        checks += 1

    driver.quit()
    assert pass_counter == checks
