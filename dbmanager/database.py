import sys
import os
import contextlib
import sqlite3
import time
from datetime import datetime
import bcrypt


#===========================================================================================
class PasswordManager:
    DIR=os.getcwd()
    NOW=time.asctime(time.localtime())
    #---------------------------------------------------------------------------------------

    def get_database_url(self,mode):
        DATABASE_URL="file:"+os.path.join(self.DIR,"passwordmanager.sqlite")+"?mode="+mode
        return DATABASE_URL
    def create(self):
        file_exist= os.path.exists("passwordmanager.sqlite")
        if file_exist:
            os.remove("passwordmanager.sqlite")
        with open(os.path.join(self.DIR,"passwordmanager.sqlite"),"x") as dbFile:
            dbFile.close()
        DATABASE_URL= self.get_database_url("rwc")
        with open(os.path.join(self.DIR,"dbmanager\\database.sql"),"r") as schema:
            stmt= schema.readlines()
        
        try:
            with sqlite3.connect(DATABASE_URL,isolation_level=None, uri=True ) as connection:
                with contextlib.closing(connection.cursor()) as cursor:
                    for line in stmt:
                        cursor.execute(line) 
                    
        except Exception as ex:
            print(ex, file=sys.stderr)
            sys.exit(1)
    #-------------------------------------------------------------------------------------------

    def create_superuser(self, username, password, secret_phrase): 
        hashed_password= bcrypt.hashpw(password, bcrypt.gensalt())
        hashed_secrete_phrase= bcrypt.hashpw(secret_phrase, bcrypt.gensalt())
        DATABASE_URL= self.get_database_url("rw")
        with sqlite3.connect(DATABASE_URL, isolation_level=None, uri=True) as connection:
            with contextlib.closing(connection.cursor()) as cursor:
                stmt="INSERT INTO user "
                stmt+="(username, password, secret_phrase ) "
                stmt+="VALUES(?,?,?)"
                cursor.execute(stmt,[username, hashed_password.decode(), hashed_secrete_phrase.decode()])
                stmt="UPDATE controller SET registered=1"
                cursor.execute(stmt)
        


    def create_new_password(self, password, site, username):
        DATABASE_URL= self.get_database_url("rw")
        try:
            with sqlite3.connect(DATABASE_URL, isolation_level=None, uri=True) as connection:
                with contextlib.closing(connection.cursor()) as cursor:
                    pid=f"{datetime.now().second}{site[4:6]}{ time.asctime(time.localtime())[0:2]}".upper()
                    cursor.execute("BEGIN")
                    stmt="INSERT INTO passwords "
                    stmt+="(pid,password, site, created, username) "
                    stmt+="VALUES(?, ?, ?, ?,?)"
                    cursor.execute(stmt, [pid,password, site, self.NOW, username])
                    cursor.execute("COMMIT")
        except Exception as ex:
            print(ex, file=sys.stderr)
            sys.exit(1)
    #------------------------------------------------------------------------------------------------------        
    def change_password(self, pid,new_password):
        DATABASE_URL= self.get_database_url("rw")
        try:
            with sqlite3.connect(DATABASE_URL, isolation_level=None, uri=True) as connection:
                with contextlib.closing(connection.cursor()) as cursor:
                    cursor.execute("BEGIN")
                    stmt= "UPDATE passwords SET password=?, created=? WHERE pid = ?"
                    cursor.execute(stmt, [new_password, self.NOW, pid])
                    cursor.execute("COMMIT")
        except Exception as ex:
            print(ex, file=sys.stderr)
            sys.exit(1)
    #--------------------------------------------------------------------------------------------
    def delete_password(self, pk):
        DATABASE_URL=self.get_database_url("rw")
        try:
            with sqlite3.connect(DATABASE_URL, isolation_level=None, uri=True) as connection:
                with contextlib.closing(connection.cursor()) as cursor:
                    cursor.execute("BEGIN")
                    stmt="DELETE FROM passwords WHERE pid=?"
                    cursor.execute(stmt, [pk])
                    cursor.execute("COMMIT")
        except Exception as ex:
            print(ex, file=sys.stderr)
            sys.exit(1)
    #---------------------------------------------------------------------------------------------------    
    def display_password(self):
        DATABASE_URL=self.get_database_url("ro")
        try:
            with sqlite3.connect(DATABASE_URL, isolation_level=None, uri=True) as connection:
                with contextlib.closing(connection.cursor()) as cursor:
                    stmt="SELECT pid, username, site, created, password FROM passwords "
                    cursor.execute(stmt) 
                    records= cursor.fetchall()
                    return records
        except Exception as ex:
            print(ex, file=sys.stderr)
            sys.exit(1)
    #------------------------------------------------------------------
    def display_user(self,username, password):
        DATABASE_URL=self.get_database_url("ro")
        user_password=password.encode()
        
        with sqlite3.connect(DATABASE_URL, isolation_level=None, uri=True) as connection:
            with contextlib.closing(connection.cursor()) as cursor:
                stmt="SELECT username, password FROM user "
                stmt+="WHERE username=?"
                cursor.execute(stmt, [username])
                record= cursor.fetchall()
                saved_password=record[0][1].encode()
                is_valid= bcrypt.checkpw(user_password, saved_password)
                if is_valid:
                    return True
                return False
         

    #--------------------------------------------------------------------
    def change_user_password(self,username, old_password, new_password, secrete_phrase):
        DATABASE_URL= self.get_database_url("rw")
        with sqlite3.connect(DATABASE_URL, isolation_level=None, uri=True) as connection:
            with contextlib.closing(connection.cursor()) as cursor:
                
                stmt="select password, secret_phrase from user where username=?"
                cursor.execute(stmt,[username])
                user_credintials = cursor.fetchone()
                old_password_exist=False
                secrete_phrase_exist=False

                if user_credintials:
                    old_password_exist= bcrypt.checkpw(old_password.encode(), user_credintials[0].encode())
                    secrete_phrase_exist=bcrypt.checkpw(secrete_phrase.encode(),user_credintials[1].encode())

                else:
                    raise ValueError("Superuser not found")
                
                if old_password_exist and secrete_phrase_exist:
                    hashed_new_password= bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
                    cursor.execute("BEGIN")
                    stmt="UPDATE user SET password = ? WHERE username=?"
                    cursor.execute(stmt, [hashed_new_password.decode(),username ])
                    cursor.execute("COMMIT")
                else:
                    raise ValueError("Invalid old password or secret phrase.")
                

                    
                
    def user_registered(self ):
            DATABASE_URL= self.get_database_url("rw")
            with sqlite3.connect(DATABASE_URL, isolation_level=None, uri=True) as connection:
                with contextlib.closing(connection.cursor()) as cursor:
                    stmt="SELECT registered FROM controller"
                    cursor.execute(stmt)
                    record=cursor.fetchall()
                    answer=answer=record[0][0]
                    if int(answer) ==1:
                        return True
                    else:
                        return False

         
#===========================================================================================    
    

# Impano Manzi Enock

                

        
