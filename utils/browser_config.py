class BrowserConfig:
    PAGE_VIEWPORT_SIZE = {'width': 1680, 'height': 920} # set desired resolution
    # ENV = 'stage'
    IS_HEADLESS = False # do not change
    SLOW_MO = 50
    LOCALE = 'en-US'
    DEFAULT_TIMEOUT = 25 * 1000 # for slow connection
    SUPPORTED_BROWSER = ["chrome"] # select "chrome" or/and "firefox"