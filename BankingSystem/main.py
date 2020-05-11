"""
Banking feature will go like this

1. Customer creation
2. Store record
3. track each record
4. update customer detail
5. transaction
6. deposit money

"""
import numpy as np
import pandas as pd
import sqlite3
from sqlite3 import Error
from database import Conection
# will try to save the data into hdf5 extenstion and also compress it

class Banking:
    def __init__(self, conn):
        self.conn = conn
    
    

    

if __name__ == "__main__":
    conn = Conection()
    banking = Banking(conn.main())
    print(banking.main())