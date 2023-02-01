#!/usr/bin/env python
# coding: utf-8

# ## Data Crunching program

# In[22]:


import csv


# In[24]:


def read_tsv(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f, delimiter='\t')
        return [row for row in reader]


# In[25]:


def write_tsv(filename, rows):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'username', 'email', 'hashed_password', 'plain_text_password','ip_address'], delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)


# In[5]:


first_rows = read_tsv("user_email_hash.1m.tsv") # Reading User_email.hash.1m.tsv – 1 million records of users with id, username, email, hashed_password


# In[6]:


third_rows = read_tsv("ip_1m.tsv") # Reading Ip_1m.tsv – 1 million records of users with id, ip


# In[7]:


second_rows = read_tsv("plain_32m.tsv") # Reading Plain_32m.tsv – 32 million records of users with email, plaintext_password


# In[8]:


print(first_rows[0])


# In[32]:


print(second_rows[0])


# In[10]:


print(third_rows[0])


# In[33]:


second_rows_dict = {row['sbh0608@hotmail.com']: row for row in second_rows}
third_rows_dict = {row['id']: row for row in third_rows}

new_rows = []
for first_row in first_rows:
    id = first_row['id']
    email = first_row['email']
    username = first_row['username']
    password = first_row['password']
    second_row = second_rows_dict.get(email, {})
    third_row = third_rows_dict.get(id, {})
    new_row = {
        'id': id,
        'username': username,
        'email': email,
        'hashed_password': password,
        'plain_text_password': second_row.get('Culsen', ''),
        'ip_address': third_row.get('ip_address', ''),
    }
    new_rows.append(new_row)

write_tsv('new_crunched_file.tsv', new_rows)


# In[ ]:




