class JSActions:
    def __init__(self, driver_):
        self.driver = driver_

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(element))
