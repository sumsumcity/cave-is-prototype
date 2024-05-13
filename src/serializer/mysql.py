import env
import MySQLdb

def run(config: dict, data: list):
    print(config)
    try:
        dbh= MySQLdb.connect(host = config['host'], user=config['user'], password=config['pass'], database=config['database'])
    # If connection is not successful
    except:
        print("Can't connect to database")
        return 0