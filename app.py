from flask import Flask,jsonify
from mysql.connector import pooling
# from config.Settings import Settings
from config.Settings2 import Settings2
from config.Settings import Settings1


import os
app = Flask(__name__)


# http://localhost:5000?data=test@test.com
@app.route('/')
def validate():
   
    return "hello world"


@app.route('/users')
def validate2():
   
 
    print("settings",Settings2.secretKey)
    print("settings2",Settings1.secretKey)
    print("settings host",Settings1.host)
    print("settings user",Settings1.user)
    print("settings database",Settings1.database)
    print("settings password",Settings1.password)
  
    connection_pool = pooling.MySQLConnectionPool(pool_name="ws_pool",
                                                  pool_size=5,
                                                  host=Settings1.host,
                                                  database=Settings1.database,
                                                  user=Settings1.user,
                                                  password=Settings1.password)
    dbConn = connection_pool.get_connection()
    cursor = dbConn.cursor(dictionary=True)
    sql="select * from user"
    cursor.execute(sql)
    users = cursor.fetchall()
    try:
        jsonUsers=users
        jsonUsers={"Users":jsonUsers}
        return jsonify(jsonUsers)
    except Exception as err:
        print(err)
        return {},500

    # dbConn.close()
    # host='localhost'
    # database='furniture'
    # user='root'
    # password='Singapore1'

    #Production
    # host=os.environ['HOST2']
    # database=os.environ['DATABASE2']
    # user=os.environ['USERNAME2']
    # password=os.environ['PASSWORD2']
   
    return "users"    



@app.route('/settings')
def Settings():
    # host='localhost'
    # database='furniture'
    # user='root'
    # password='Singapore1'
    host=os.environ['HOST']
    database=os.environ['DATABASE']
    user=os.environ['USERNAME']
    password=os.environ['PASSWORD']
    settings={"host":host,"username":user,"database":database}
    return jsonify(settings)
    

if __name__ == '__main__':
    app.run(debug=True)
