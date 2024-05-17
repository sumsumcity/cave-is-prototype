import env
import MySQLdb # type: ignore

def run(config: dict, data: list):
    dbh= MySQLdb.connect(host = config['host'], user=config['user'], password=config['pass'], database=config['database'], port=config['port'])

    rd = dfmt(env.now())
    for item in data:
        cursor = dbh.cursor()
        runonce(cursor, dbh, rd, item)

def runonce(cursor, dbh, rd: str, item: dict):
    cursor.execute("""INSERT INTO results (date, itemid, metricid, status, description) VALUES (%s, %s, %s, %s, %s, %s)""", rd, rd, item['item'], item['metric'], item['result'], item.get('title', ''))
    dbh.commit()
    cursor.close()

def dfmt(datetime):
    return datetime.strftime('%Y-%m-%d %H:%M:%S')