from xlrd import open_workbook
import sys
import threading , Queue
from random import randint
from time import sleep
from pprint import pprint

class ExcelData():
    
    def __init__(self, lab , mac_id):        
        self.lab    = lab
        self.mac_id = mac_id
    
    def __str__(self):        
        return("LAB Name= {0} MAC_ID= {1}".format(self.lab, self.mac_id))

def readExcel():
    items = []
    wb = open_workbook('bulk-decom.xlsx')
    for sheet in wb.sheets():
        number_of_rows = sheet.nrows
        number_of_columns = sheet.ncols        
        for row in range(1, number_of_rows):        
            values = []
            for col in range(number_of_columns):
                value = (sheet.cell(row,col).value)                                  
                try:
                    value =  str(int(value))             
                except ValueError:
                    pass
                finally:
                    values.append(value)     
            item = ExcelData(*values)
            items.append(item)
    return items

def split_list(the_list, chunk_size):
    result_list = []
    while the_list:
        result_list.append(the_list[:chunk_size])
        the_list = the_list[chunk_size:]
    return result_list



def print_number(myList , number):
    # Sleeps a random 1 to 10 seconds
    rand_int_var = randint(1, 20)
    sleep(rand_int_var)
    
    print "Thread " + str(number) + " slept for " + str(rand_int_var) + " seconds"
    for item in myList:
        print item
    

def worker(a_list):
    # Create Workers and give each list to perform the list opertions
    thread_list = []
    cnt = 0 
    for element in a_list:
        # Instantiates the thread
        # (i) does not make a sequence, so (i,)
        t = threading.Thread(target=print_number, args=(element,cnt))
        # Sticks the thread in a list so that it remains accessible
        thread_list.append(t)
        cnt = cnt + 1
    
    # Starts threads
    for thread in thread_list:
        thread.start()
        
    for thread in thread_list:
        thread.join()
    
    print "Done"

if __name__ == '__main__':
    items = readExcel()    
    a_list = split_list(items, 50)
    worker(a_list)
