import os
class Settings:
    
    secretKey="a12nc)238OmPq#cxOlm*a"

    #Dev
    # host='localhost'
    # database='furniture'
    # user='root'
    # password='Singapore1'

    #Production
    host=os.environ['HOST']
    database=os.environ['DATABASE']
    user=os.environ['USERNAME']
    password=os.environ['PASSWORD']
    print("host",host)
    print("database",database)
    print("username",user)
    print("password",password)