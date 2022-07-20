import datetime
import os
import re
import time
from selenium import webdriver
from pageobjects.pesas_mancuernas import *
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

initial_time = time.time()


def before_all(context):
    options = Options()
    options.add_argument("start-maximized")
    # self.driver.maximize_window()
    options.add_argument("no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.headless = False
    # options.add_argument("--headless")
    options.add_argument("--allow-running-insecure-content")
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def before_feature(context, feature):
    context.current_feature = feature.name


def before_scenario(context, scenario):
    context.current_scenario = scenario.name
    context.tag = scenario.tags

    # To simulate different speeds and bandwidth
    # network_conditions = {"offline": True, "latency": 5, "download_throughput": 500 * 1024, "upload_throughput": 500 * 1024}
    # context.driver.set_network_conditions(**network_conditions)


def before_tag(context, tag):
    pass


def before_step(context, step):
    context.current_step = step.name


def after_all(context):
    context.driver.close()
    context.driver.quit()
    total_time = time.time() - initial_time
    print(50 * '-')
    print(
        'The complete test set took: {tt} (real time)'.format(tt=str(datetime.timedelta(seconds=total_time))[:-3]))
    print(50 * '-')


def after_scenario(context, scenario):
    test_status = scenario.status.name if hasattr(scenario.status, 'name') else scenario.status

    if test_status == 'failed':
        custom_path = os.path.abspath(os.path.join('_output', 'failed_tests.text'))
        # We open the file, if the file exists before, the data is appending at the end of the file without truncating it.
        txt = open(custom_path, "a")
        for item in get_jira_ids_from_scenario(scenario):
            txt.write(item + '\n')
            context.logger.debug("Writing on failed_tests.text case: %s" % item)
        txt.close()


def after_step(context, step):
    context.last_step = step


def after_feature(context, feature):
    pass


def get_jira_ids_from_scenario(scenario):
    """
    Gets the Jira IDs from tags with this format:
      @(\w+)-(\d+)
    :param scenario: behave object containing list of tags (scenario.tags)
    :return: (list) Jira IDs
    """
    jira_regex = re.compile(r'(^[a-zA-Z]+-[\d]+)')
    keys = []
    for tag in scenario.tags:
        match = jira_regex.search(tag)
        # tag.startswith("xxx"): #Another form to locate tag, without regex
        if match:
            keys.append('@' + match.group(1))
    return keys
