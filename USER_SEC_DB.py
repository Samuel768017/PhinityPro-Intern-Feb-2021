# from dns.rdatatype import NULL
import mysql.connector
db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="TIGER",
  database="user_db"
)
print(db_connection)


# creating database_cursor to perform SQL operation
db_cursor = db_connection.cursor()
# db_cursor.execute("create database user_db")
# db_cursor.execute("SHOW DATABASES")

SecUser="CREATE TABLE IF NOT EXISTS Sec_User\
         (ID INT(38) AUTO_INCREMENT NOT NULL PRIMARY KEY,\
          CODE VARCHAR(50) NOT NULL,\
          NAME VARCHAR(100) NOT NULL,\
          PASSWORD VARCHAR(100) NOT NULL,\
          DESCRIPTION VARCHAR(255),\
          GROUP_ID INT(38) NOT NULL,\
          EMPLOYEMENT_TITLE VARCHAR(50),\
          EMPLOYEMENT_TYPE  VARCHAR(50),\
          INDICATOR VARCHAR(50),\
          REPORTING_INDICTOR VARCHAR(50),\
          EMAIL VARCHAR(100),\
          MOBILE VARCHAR(50),\
          OFFICE_PHONE VARCHAR(50),\
          HOME_PHONE VARCHAR(50),\
          FAX VARCHAR(50),\
          PASSWORD_EXPIRY_DATE DATE,\
          REC_STATUS CHAR(1) DEFAULT('A'),\
          IS_LOCKED CHAR(1) DEFAULT('N'),\
          IS_RESET CHAR(1) DEFAULT('Y'),\
          LAST_PSWD_ATTEMPTS INT(5),\
          IS_LOGGED CHAR(1) DEFAULT('N'),\
          IS_MULTY_LOGIN CHAR(1) DEFAULT('N'),\
          PICTURE BLOB,\
          DEFAULT_LANG_ID INT,\
          TIMEZONE_ID VARCHAR(100),\
          DATE_FROMAT VARCHAR(12),\
          TIME_FORMAT VARCHAR(10),\
          CREATED_ON DATE NOT NULL,\
          CREATED_BY INT NOT NULL,\
          UPDATED_ON DATE NOT NULL,\
          UPDATED_BY INT NOT NULL);"
db_cursor.execute(SecUser)

SecUserRole="CREATE TABLE IF NOT EXISTS Sec_User_Role\
            (ID INT(38) NOT NULL PRIMARY KEY AUTO_INCREMENT,\
             USER_ID INT(38) NOT NULL,FOREIGN KEY(USER_ID) REFERENCES Sec_User(ID) ON DELETE CASCADE ON UPDATE CASCADE,\
             ROLE_ID INT(38) NOT NULL,FOREIGN KEY(ROLE_ID) REFERENCES Sec_Role(ID) ON DELETE CASCADE ON UPDATE CASCADE,\
             CREATED_ON DATE NOT NULL,\
             CREATED_BY INT NOT NULL,\
             UPDATED_ON DATE NOT NULL,\
             UPDATED_BY INT NOT NULL);"
db_cursor.execute(SecUserRole)

SecUserGroup="CREATE TABLE IF NOT EXISTS Sec_User_Group\
             (ID INT(38) NOT NULL PRIMARY KEY AUTO_INCREMENT,\
              USER_ID INT(38) NOT NULL,FOREIGN KEY(USER_ID) REFERENCES Sec_User(ID) ON DELETE CASCADE ON UPDATE CASCADE,\
              GROUP_ID INT(38) NOT NULL,FOREIGN KEY(GROUP_ID) REFERENCES Sec_Group(ID) ON DELETE CASCADE ON UPDATE CASCADE,\
              CREATED_ON DATE NOT NULL,\
              CREATED_BY INT(38) NOT NULL,\
              UPDATED_ON DATE NOT NULL,\
              UPDATED_BY INT(38) NOT NULL);"
db_cursor.execute(SecUserGroup)   

SecGroup="CREATE TABLE IF NOT EXISTS Sec_Group\
         (ID INT(38) NOT NULL PRIMARY KEY AUTO_INCREMENT,\
          CODE VARCHAR(50) NOT NULL,\
          NAME VARCHAR(100) NOT NULL,\
          DESCRIPTIONS VARCHAR(255),\
          HEAD_NAME VARCHAR(100),\
          OFFICE_PHONE VARCHAR(50),\
          FAX VARCHAR(50),\
          REC_STATUS CHAR(1) DEFAULT('A'),\
          CREATED_ON DATE NOT NULL,\
          CREATED_BY INT(38) NOT NULL,\
          UPDATED_ON DATE NOT NULL,\
          UPDATED_BY INT(38) NOT NULL);"
db_cursor.execute(SecGroup) 

SecGrpRole="CREATE TABLE IF NOT EXISTS Sec_Grp_Role\
           (ID INT(38) NOT NULL PRIMARY KEY AUTO_INCREMENT,\
            GROUP_ID INT(38),FOREIGN KEY(GROUP_ID) REFERENCES Sec_Group(ID) ON DELETE CASCADE ON UPDATE CASCADE,\
            ROLE_ID INT(38) NOT NULL,FOREIGN KEY(ROLE_ID) REFERENCES Sec_Role(ID) ON DELETE CASCADE ON UPDATE CASCADE,\
            CREATED_ON DATE NOT NULL,\
            CREATED_BY INT(38) NOT NULL,\
            UPDATED_ON DATE NOT NULL,\
            UPDATED_BY INT(38) NOT NULL);"
db_cursor.execute(SecGrpRole) 

SecIcon="CREATE TABLE IF NOT EXISTS Sec_Icon\
         (ID INT(38) NOT NULL PRIMARY KEY AUTO_INCREMENT,\
          KEY_ VARCHAR(50) NOT NULL,\
          NAME_ VARCHAR(50) NOT NULL,\
          IS_LOCKED CHAR(1) DEFAULT('N'),\
          CREATED_ON DATE NOT NULL,\
          CREATED_BY INT(38) NOT NULL,\
          UPDATED_ON DATE NOT NULL,\
          UPDATED_BY INT(38) NOT NULL);"
db_cursor.execute(SecIcon)


SecMenuOption="CREATE TABLE IF NOT EXISTS Sec_Menu_Option\
              (ID INT(38) NOT NULL PRIMARY KEY AUTO_INCREMENT,\
               MODULE_ID INT(38) NOT NULL,FOREIGN KEY(MODULE_ID) REFERENCES Sec_Module(ID) ON DELETE CASCADE ON UPDATE CASCADE\
               PARENT_ID INT(38) NOT NULL,\
               NAME VARCHAR(100) NOT NULL,\
               ALTERNATE_NAME VARCHAR(100),\
               SEQUENCE INT(6) NOT NULL,\
               SCREEN_ID INT(38),FOREIGN KEY(SCREEN_ID) REFERENCES Sec_Screen(ID) ON DELETE CASCADE ON UPDATE CASCADE\
               REFRESH_ON_ASSET_CHANGE CHAR(1) DEFAULT('N'),\
               PARAMETER_VALUES VARCHAR(500),\
               ICON_KEY VARCHAR(50),SHOW_ASSET_TREE CHAR(1)DEFAULT('N'),\
               IS_LOCKED CHAR(1) DEFAULT('N'),\
               REC_STATUS CHAR(1) DEFAULT('A'),\
               CREATED_ON DATE NOT NULL,CREATED_BY INT(38) NOT NULL,\
               UPDATED_ON DATE NOT NULL,UPDATED_BY INT(38) NOT NULL);"
db_cursor.execute(SecMenuOption) 

SecModule="CREATE TABLE IF NOT EXISTS Sec_Module\
          (ID INT(38) NOT NULL PRIMARY KEY AUTO_INCREMENT,\
           CODE VARCHAR(10) NOT NULL,\
           NAME VARCHAR(50) NOT NULL,\
           DESCRIPTIONS VARCHAR(255),\
           SETUP_SHEET_ID INT(6),\
           REC_STATUS CHAR(1) NOT NULL,\
           DEFAULT_MENU_ID INT(8),\
           CREATED_ON DATE NOT NULL,\
           CREATED_BY INT(38) NOT NULL,\
           UPDATED_ON DATE NOT NULL,\
           UPDATED_BY INT(38) NOT NULL);"
db_cursor.execute(SecModule) 

SecPasswordPolicy="CREATE TABLE IF NOT EXISTS Sec_Password_Policy\
                  (ID INT(38) NOT NULL PRIMARY KEY AUTO_INCREMENT,\
                   USE_AD CHAR(1),\
                   PASSWORD_RESET_DAYS INT(6),\
                   IS_NUMBER_MUST CHAR(1) NOT NULL,\
                   IS_ALPHABET_MUST CHAR(1) NOT NULL,\
                   MIN_PASSWORD_LENGTH INT(6) NOT NULL,\
                   MAX_PASSWORD_LENGTH INT(6) NOT NULL,\
                   WARN_PASSWORD_EXPIRY_DAYS INT(6) NOT NULL,\
                   GENERATE_RANDOM_PASSWORD CHAR(1) NOT NULL,\
                   DEF_PASSWORD_ON_RESET CHAR(50) NOT NULL,\
                   SAME_AS_USERID CHAR(1) NOT NULL,\
                   MIX_CASE CHAR(1) NOT NULL,\
                   SPECIAL_CHAR CHAR(1) NOT NULL,\
                   MAX_ATTEMPTS_ALLOWED INT(38) NOT NULL,\
                   CREATED_ON DATE NOT NULL,\
                   CREATED_BY INT(38) NOT NULL,\
                   UPDATED_ON DATE NOT NULL,\
                   UPDATED_BY INT(38) NOT NULL);"
db_cursor.execute(SecPasswordPolicy) 

SecRole="CREATE TABLE IF NOT EXISTS Sec_Role\
        (ID INT(38) NOT NULL PRIMARY KEY AUTO_INCREMENT,\
         CODE VARCHAR(50) NOT NULL,\
         NAME VARCHAR(100) NOT NULL,\
         DESCRIPTION VARCHAR(255),\
         REC_STATUS CHAR(1) DEFAULT('A'),\
         IS_LOCKED CHAR(1) DEFAULT('N'),\
         CREATED_ON DATE NOT NULL,\
         CREATED_BY INT(38) NOT NULL,\
         UPDATED_ON DATE NOT NULL,\
         UPDATED_BY INT(38) NOT NULL);"
db_cursor.execute(SecRole) 

SecRoleScrFuncLink="CREATE TABLE IF NOT EXISTS Sec_Role_Screen_Func_Link\
      (ID INT(38) NOT NULL PRIMARY KEY AUTO_INCREMENT,\
      ROLE_ID INT(38) NOT NULL,FOREIGN KEY(ROLE_ID) REFERENCES Sec_Role(ID) ON DELETE CASCADE ON UPDATE CASCADE,\
      SCREEN_FUNCTIONALITY_ID INT(9) NOT NULL,FOREIGN KEY(SCREEN_FUNCTIONALITY_ID) REFERENCES Sec_Screen_Functionality(ID) ON DELETE CASCADE ON UPDATE CASCADE,\
      ASSET_TYPE VARCHAR(128),\
      CREATED_ON DATE NOT NULL,\
      CREATED_BY INT(38) NOT NULL,\
      UPDATED_ON DATE NOT NULL,\
      UPDATED_BY INT(38) NOT NULL);"
db_cursor.execute(SecRoleScrFuncLink) 

SecScreen="CREATE TABLE IF NOT EXISTS Sec_Screen\
          (ID INT(38) NOT NULL PRIMARY KEY AUTO_INCREMENT,\
           NAME VARCHAR(50) NOT NULL,\
           DESCRIPTION VARCHAR(250),\
           SCREEN_URL VARCHAR(1000) NOT NULL,\
           PARAMETER VARCHAR(500),\
           REC_STATUS CHAR(1) DEFAULT('A'),\
           IS_LOCKED CHAR(1) DEFAULT('N'),\
           REFRESH_ON_ASSET_CHANGE CHAR(1) DEFAULT('N'),\
           CREATED_ON DATE NOT NULL,\
           CREATED_BY INT(38) NOT NULL,\
           UPDATED_ON DATE NOT NULL,\
           UPDATED_BY INT(38) NOT NULL );"
db_cursor.execute(SecScreen)           

SecScrFunctionality="CREATE TABLE IF NOT EXISTS Sec_Screen_Functionality\
        (ID INT(38) NOT NULL PRIMARY KEY AUTO_INCREMENT,\
          SCREEN_ID INT(38) NOT NULL,FOREIGN KEY(SCREEN_ID) REFERENCES Sec_Screen(ID) ON DELETE CASCADE ON UPDATE CASCADE,\
          FUNCTIONALITY_ID INT(38) NOT NULL,FOREIGN KEY(FUNCTIONALITY_ID) REFERENCES Sec_Functionality(ID) ON DELETE CASCADE ON UPDATE CASCADE,\
          CREATED_ON DATE NOT NULL,\
          CREATED_BY INT(38) NOT NULL,\
          UPDATED_ON DATE NOT NULL,\
          UPDATED_BY INT(38) NOT NULL);"
db_cursor.execute(SecScrFunctionality) 

#This Sec_User_Menu table is executed and create in db but MENU_ID and PARENT_MENU_ID foreign key are not showing-------------------------NOT----------------------------
SecUserMenu="CREATE TABLE IF NOT EXISTS Sec_User_Menu\
          (ID INT(38) NOT NULL PRIMARY KEY AUTO_INCREMENT,\
            USER_ID INT(38) NOT NULL,FOREIGN KEY(USER_ID) REFERENCES Sec_User(ID) ON DELETE CASCADE ON UPDATE CASCADE,\
            MENU_ID INT(38) NOT NULL,FOREIGN KEY(MENU_ID) REFERENCES Sec_Menu_Option(ID) ON DELETE CASCADE ON UPDATE CASCADE,\
            PARENT_MENU_ID INT(38) NOT NULL,FOREIGN KEY(PARENT_MENU_ID) REFERENCES Sec_Menu_Option(PARENT_ID) ON DELETE CASCADE ON UPDATE CASCADE,\
            VIEW_ONLY CHAR(1) DEFAULT('N'),\
            REC_STATUS CHAR(1) DEFAULT('A'),\
            CREATED_ON DATE NOT NULL,\
            CREATED_BY INT(38) NOT NULL,\
            UPDATED_ON DATE NOT NULL,\
            UPDATED_BY INT(38) NOT NULL);"
db_cursor.execute(SecUserMenu) 
#________________________________________________________________


SecFunctionality="CREATE TABLE IF NOT EXISTS Sec_Functionality\
                 (ID INT(38) NOT NULL PRIMARY KEY AUTO_INCREMENT,\
                  NAME VARCHAR(50) NOT NULL,\
                  DESCRIPTION VARCHAR(250),\
                  IS_LOCKED CHAR(1) DEFAULT('N'),\
                  CREATED_ON DATE NOT NULL,\
                  CREATED_BY INT(38) NOT NULL,\
                  UPDATED_ON DATE NOT NULL,\
                  UPDATED_BY INT(38) NOT NULL);"
db_cursor.execute(SecFunctionality) 

db_cursor.execute("SHOW TABLES")
print(db_cursor.fetchall())    
