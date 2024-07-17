from selenium.webdriver import Firefox


def before_all(context):
     context.browser = Firefox()
     context.browser.get('https://www.jogajuntoinstituto.org/')
    
def After_all(context):
    context.browser.quit()