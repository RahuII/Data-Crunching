# Data-Crunching
- In this program we have to take 3 file as a input and make a new file which contains all three files specific data(id, name, email, hashed_password, plain_pass, ip_address)
- In this program i use csv built in library for operation perform on tsv(tab-separated values).
- I have make 'read_tsv' funtion to read .tsv file and returns a list of dictionaries, where each dictionary represents a row in the file.
- 'write_tsv' which is take two parameter 1. file_name in which we have to write data. 2. is a list of dictionaries, where each dictionary represents a row in the file.
- In main code creates two dictionaries, second_rows_dict and third_rows_dict. The dictionaries are created by using a dictionary comprehension, which is a concise way to create a new dictionary.
- For second_rows_dict, the dictionary comprehension takes each row in the second_rows list and creates a key-value pair in the dictionary,
- Initializes an empty list new_rows to store the new dictionaries that will be created.
- Run a loops over each row in the first_rows list.
- appends the new_row dictionary to the new_rows list.
