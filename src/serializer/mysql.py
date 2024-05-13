import env
import MySQLdb # type: ignore

def run(config: dict, data: list):
    try:
        dbh= MySQLdb.connect(host = config['host'], user=config['user'], password=config['pass'], database=config['database'], port=config['port'])
        print("Connection to MySQL database successful!")
        try:
            rd = dfmt(env.now())
            for item in data:
                runonce(dbh, rd, item)
        except:
            print("Something went wrong in the SQL statement")
            return 0
    except:
        print("Can't connect to database")
        return 0
    
def runonce(dbh, rd: str, item: dict):
    sql = "INSERT INTO results (date, itemid, metricid, status, description)"
    sql += " VALUES ('%s', '%s', '%s', '%s', '%s')"
    data = (rd, item['item'], item['metric'], item['result'], item.get('title', ''))
        
    try:
        cursor = dbh.cursor()
        cursor.execute(sql % data)
        dbh.commit()
        cursor.close()
        print("Adding data to MySQL was successful")
    except Exception as e:
        print(e)

def dfmt(datetime):
    return datetime.strftime('%Y-%m-%d %H:%M:%S')