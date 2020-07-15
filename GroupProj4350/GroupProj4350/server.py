import pypyodbc

class server():
    serverObject=None
    hostName=''
    databaseName=''

    def __init__(self,serverName, databaseName):
        #, hostName, databaseName, userName, serverPassword
        self.hostName=serverName
        self.databaseName=databaseName
       # self.userName=userName
        #self.serverPassword=serverPassword
        self.connect()


    def connect(self):
        self.serverObject=None
        self.serverObject = pypyodbc.connect('Driver={SQL Server};'
                                            'Server='+self.hostName+';'
                                            'Database='+self.databaseName+';'
                                            'Trusted_Connection=yes;')

        print("Connected to server!")
    #Runs a sql command (Geared for select right now)
    def command(self,order):
        cursor = self.serverObject.cursor()
        cursor.execute(order)
        for row in cursor:
            print(row)
    
    def loginCheck(self,order):
        cursor = self.serverObject.cursor()

        cursor.execute(order)
        #query = pd.read_sql_query(order, self.serverObject)
        return cursor


    #Ends Connection
    def endConnection(self):
        self.serverObject.close()


#This is a test function
def test():
    firstServer=server('Rxlbcoxlt\mssqlserver01','master')
    #firstServer.command('SElECT * FROM master.dbo.customers')
   # firstServer.endConnection()

