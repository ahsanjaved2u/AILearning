import numpy as np
import random
import pandas as pd

transaction_id = [i for i in range(1,501)]
transaction_id

vendor_number = np.random.randint(low=1, high=2500, size=(500))
vendor_number

transaction_amount = np.random.randint(low=20, high=125000, size =( 500))
transaction_amount

transaction_types = ['cash_withdrawl', 'cash_deposit', 'transfer_domestic', 'transfer_international']
random_int = [random.randint(0,3) for i in range(0,500)]
transaction_list = [transaction_types[i] for i in random_int]
transaction_list

transaction_data = {
    "transaction_id":transaction_id,
    "transaction_number": list(vendor_number),
    "transaction_amount":list(transaction_amount),
    "transaction_type":transaction_list
}
transaction_data
transaction_Data_Frame = pd.DataFrame(transaction_data)
transaction_Data_Frame.head(5)

Final_list = transaction_Data_Frame.values.tolist()
Final_list

from neo4j import GraphDatabase

transaction_execution_commands = []

for i in Final_list:
    neo4j_create_statemenet ="create (t:Transaction {transaction_id:" + str(i[0]) +" ,vendor_number: "+ str(i[1])+", transaction_amount: "+str(i[2])+",transaction_type:'" + str(i[3]) + "'})"
    transaction_execution_commands.append(neo4j_create_statemenet) 

