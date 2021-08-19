import os
class Settings:
    
    secretKey="a12nc)238OmPq#cxOlm*a"

    #Dev
    host='localhost'
    database='furniture'
    user='root'
    password='Singapore1'

    #Production
    # host=os.environ['HOST2']
    # database=os.environ['DATABASE2']
    # user=os.environ['USERNAME2']
    # password=os.environ['PASSWORD2']
    # print("host",host)
    print("database",database)
    print("username",user)
    print("password",password)