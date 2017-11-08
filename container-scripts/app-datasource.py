import os

# Deployment Information 
domainhome = os.environ.get('DOMAIN_HOME', '/u01/oracle/user_projects/domains/base_domain')

# Definition DataSource Properties
# dsName            = "ds_atm_movil"
# dsDatabaseName    = "test"
# datasourceTarget  = "AdminServer"
# dsJNDIName        = "jdbc/atm_movil"
# dsDriverName      = "com.mysql.jdbc.Driver"
# dsURL             = "jdbc:mysql://192.168.42.1:3306/test"
# dsUserName        = "openshiftUser"
# dsPassword        = "R3dh4t1!"
# dsTestQuery       = "SQL SELECT 1"

dsName            = os.environ.get('dsName')
dsDatabaseName    = os.environ.get('dsDatabaseName')
datasourceTarget  = os.environ.get('datasourceTarget')
dsJNDIName        = os.environ.get('dsJNDIName')
dsDriverName      = os.environ.get('dsDriverName')
dsURL             = os.environ.get('dsURL')
dsUserName        = os.environ.get('dsUserName')
dsPassword        = os.environ.get('dsPassword')
dsTestQuery       = os.environ.get('dsTestQuery')

# Read Domain in Offline Mode
# ===========================
readDomain(domainhome)

# Create DataSource
# ==================

create(dsName, 'JDBCSystemResource')
cd('/JDBCSystemResource/' + dsName)
set('Target','AdminServer')
 
cd('/JDBCSystemResource/' + dsName +'/JdbcResource/' + dsName)

# Create JDBCDataSourceParams
cmo.setName(dsName)
cd('/JDBCSystemResource/' + dsName +'/JdbcResource/' + dsName)
create('myJdbcDataSourceParams','JDBCDataSourceParams')
cd('JDBCDataSourceParams/NO_NAME_0')
set('JNDIName', java.lang.String(dsJNDIName))
set('GlobalTransactionsProtocol', java.lang.String('None'))
 
# Create JDBCDriverParams
cd('/JDBCSystemResource/' + dsName +'/JdbcResource/' + dsName)
create('myJdbcDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName',dsDriverName)
set('URL',dsURL)
set('PasswordEncrypted', dsPassword)
set('UseXADataSourceInterface', 'false')
 
# Create JDBCDriverParams Properties'
create('myProperties','Properties')
cd('Properties/NO_NAME_0')
create('user','Property')
cd('Property')
cd('user')
set('Value', dsUserName)

 
# Create JDBCConnectionPoolParams
cd('/JDBCSystemResource/' + dsName +'/JdbcResource/' + dsName)
create('myJdbcConnectionPoolParams','JDBCConnectionPoolParams')
cd('JDBCConnectionPoolParams/NO_NAME_0')
set('TestTableName',dsTestQuery)

updateDomain()
closeDomain()
exit()
