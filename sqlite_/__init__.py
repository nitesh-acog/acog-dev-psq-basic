

import sqlite3

class SQLITE3:
   

    def __init__(self,path_to_db:str):
        '''
    Takes is path for sqlite3 db, If it isn't present creates one to connect to it
    args: path_to_db='db.sqlite3' 

    '''
        self.path=path_to_db
    
        
        with sqlite3.connect(path_to_db) as conn:
            pass
    
    def check_for_table(self,table_name:str)->bool:
        '''
        check if a table already exists in given db
        args: table_name
        returns bool


        '''
        with sqlite3.connect(self.path) as conn:
            cursor=conn.cursor()
            cursor.execute("""SELECT name FROM sqlite_master  
                WHERE type='table' 
                """)
        return table_name in [table[0] for table in cursor.fetchall()]

    
    def create_table(self,table_name:str , schema:str):
        schema='(in_file TEXT NOT NULL, out_file TEXT NOT NULL, STATUS INT)'
        #print(f'CREATE TABLE IF NOT EXISTS {table_name}'+ schema)
        with sqlite3.connect(self.path) as conn:
            cursor=conn.cursor()
            cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name}(in_file TEXT NOT NULL, out_file TEXT NOT NULL, STATUS INT NOT NULL)')
            conn.commit()
    

    
    def insert_record(self,table_name:str,infile:str,out_file:str,status:int=0):
        with sqlite3.connect(self.path) as conn:
            cursor=conn.cursor()
            cursor.execute(f'INSERT INTO {table_name} values(?,?,?)',(infile,out_file,status))
            conn.commit()
            # cursor.execute(f'select * from {table_name}')
            # print(cursor.fetchall())

    def check_if_both_infile_outfile_in_table(self,table_name,infile_:str,out_file_:str)-> bool:
        with sqlite3.connect(self.path) as conn:
            cursor=conn.cursor()
            cursor.execute(f'select * from {table_name}')

        return (infile_,out_file_) in [(x[0],x[1]) for x in cursor.fetchall()]

    def update_table(table_name:str,values_to_update:dict):
        infile=values_to_update['infile']
        outfile=values_to_update['outfile']
        status=values_to_update['status']
        
        with sqlite3.connect(self.path) as conn:
            cursor=conn.cursor()
            cursor.execute(f'UPDATE {table_name} SET status={status} where in_file={infile} and out_file={outfile}')
            conn.commit()
    
    def delete_record(table_name:str):
        
        with sqlite3.connect(self.path) as conn:
            cursor=conn.cursor()
            cursor.execute(f'DELETE * from {table_name} where status=0')
            conn.commit()
        
        



    
        

                
        

if __name__=="__main__":
    sql=SQLITE3('sqlite3')
    sql.create_table('test', 'jdikk')
    sql.insert_record('test', 'in.csv', 'out.csv')





    

