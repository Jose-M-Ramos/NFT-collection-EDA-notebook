#!/usr/bin/env python
# coding: utf-8

# In[47]:


import pandas as pd
import requests 


# In[39]:


def max_calls(x):
    
    numbers = [(int(str((x[i])), 16)) for i in range(999)]
        
    return str(max(numbers))
        


# In[50]:


def get_all_data(first_block_contract, collection_contract, personal_apikey):

    list_df = []
    stop =0
    i = 0

    while stop == 0: 
      i += 1
      if i == 1:
          fromBlock = first_block_contract 
  
      
      module = "logs" 
      action = "getLogs" 
      toBlock = "latest" 
      address = collection_contract 
      topic0 = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef" 
      apikey = personal_apikey 
      url = "https://api.etherscan.io/api?module="+module+"&action="+action+"&fromBlock="+fromBlock+"&toBlock="+toBlock+"&address="+address+"&topic0="+topic0+"&apikey="+apikey
      response = requests.get(url) 
      address_content= response.json() 
      result=address_content.get("result") 
      df=pd.DataFrame.from_dict(result) 
        
      list_df.append(df) 

      try: 
        fromBlock = max_function(df.blockNumber) 
      except:
        pass


   
      if i>2:
        if list_df[i-1].equals(list_df[i-2]):  
              stop=1 
                
    list_df=pd.concat(list_df)
  
    
    return list_df


# In[49]:


get_full_data("12864862", "0x1Eb7382976077f92cf25c27CC3b900a274FD0012", "1HTNWZIW5WAT5KV8P58IUH88SQINB8VADJ")


# In[ ]:




