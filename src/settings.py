    # Crawler info
VERSION = "1.0"
FIRST_USER = "id/MrAnaatti"
SOME_STEAM_ID = 76561198030822246
STEAM_ID_LEN = 17
USER_AGENT = "Custom web crawler for Steam users; +https://www.github.com/AnttiVainio/Steam-crawler"
LANG = "en"
DATA_SAVER = "http://www.yoursteamcrawlywebsite.com/somesavingscript"

    # Crawler speed
REQUEST_THREADS = 2
SLEEP_TIME = 0.2
ERROR_TIME = 100.0
TIMEOUT = 120.0
QUEUE_SAVE_TIME = 600
STATUS_DUMP_TIME = 300
DATA_DUMP_TIME = 7000

    # Recrawl
RANDOM_CRAWL = 10
MIN_IMPORTANCE = 0.005
RECRAWL_TIME = 250000
RECRAWL_TIME_SPEC = 400000
HILEVEL_TIME = 1200000
NAMELESS_TIME = 100000
ALIAS_TIME = 17000000
COMMON_TIME = 5500000
BG_TIME = 9000000

    # Backup
BACKUP_INTERVAL = 200000
BACKUP_AMOUNT = 8

    # Important list
IMPRT_LST_TIME_SPAN = 1728000
IMPRT_LST_MIN_AMOUNT = 150

    # Common names
MIN_COMMON_NAME = 2
MIN_COMMON_WORD = 2
NAME_IN_NAME_MIN_LEN = 5

    # Misc
ALIAS_DAYS = 10000
HI_ALIAS_MULT = 65.0
BACKGROUND_AMOUNT = 100
COMMON_NAME_AMOUNT = 100
IMPORTANT_AMOUNT = 50
IMPRT_TRESHOLD_INDEX = 1000
MAX_QUEUE_SIZE = 10000
QUICK_CRAWL_LEVEL = 80
EXIST_LIST_SIZE = 1000 #can't make smaller later
