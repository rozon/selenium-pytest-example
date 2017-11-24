from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def get_webdriver(browser, browser_version, platform, os_version):
    USERNAME = "anthonyrozon1"
    PASSWORD = "pyx1xfRY4qqkwpsEqSFM"
    if browser.lower() == 'chrome':
        desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities['os'] = platform
    desired_capabilities['os_version'] = os_version
    desired_capabilities['browser_version'] = browser_version

    return webdriver.Remote(command_executor='http://%s:%s@hub.browserstack.com:80/wd/hub' % (USERNAME, PASSWORD),
                            desired_capabilities=desired_capabilities)


def test_github_user_search(browser, browserstack_flag, browser_version, platform, os_version):
    driver = get_webdriver(browser, browser_version, platform, os_version)
    pass_counter = 0
    checks = 0
    github_user_name = "rozon"
    driver.get('https://github.com/')

    # Check for page title
    if driver.title == "GitHub":
        pass_counter += 1
    checks += 1

    # Check if github performed a search for given username

    input_github_search = driver.find_element_by_xpath(".//input[contains(@placeholder, 'Search GitHub')]")
    input_github_search.send_keys(github_user_name)
    input_github_search.submit()

    if driver.title == ("Search · " + github_user_name + " · GitHub"):
        pass_counter += 1
    checks += 1

    # Check if github returns any user

    label_users_search_result = driver.find_element_by_xpath(".//a[contains(@class, 'UnderlineNav-item') and text()='Users']/span")
    github_user_results_count = int(label_users_search_result.text)

    if github_user_results_count > 0:
        pass_counter += 1
    checks += 1

    # Check if github results returns same amount of users

    label_users_search_count = driver.find_element_by_xpath(".//div[contains(@class, 'three-fourths')]/div[1]/h3")
    search_count = int(label_users_search_count.text[0:1])

    if github_user_results_count == search_count:
        pass_counter += 1
    checks += 1

    # Check if github user url appears on results table

    label_user_profile = driver.find_element_by_xpath(".//em[text()='" + github_user_name + "']")

    try:
        label_user_profile.click()
        pass_counter += 1
    except Exception as e:
        print(e)
    checks += 1

    #




    driver.quit()
    assert pass_counter == checks
