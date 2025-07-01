
hash_table = [[] for _ in range(32)]
# Hash functions
def hash_function_1(key):
    return key % 32

def hash_function_2(key):
    return ((1731 * key + 520123) % 524287) % 32

def hash_function_3(key): # Use the default hash method of Python as the third hash function
    return hash(key) % 32

# Function to process commands and update the hash table
def process_commands(hash_function, num_commands, commands):
    global hash_table
    hash_function_mapping = {1: hash_function_1, 2: hash_function_2, 3: hash_function_3}

    for command_str in commands[:num_commands]:
        command = command_str.split()

        if not command:
            continue  # Skip empty commands

        action, *rest = command

        if action == 'del' and len(rest) == 1:
            delete_word(hash_function_mapping[hash_function], rest[0])

        elif len(command) == 1:
            insert_word(hash_function_mapping[hash_function], command[0])

def delete_word(hash_function, word):
    key = sum(map(ord, word))
    index = hash_function(key)

    hash_table[index] = [entry for entry in hash_table[index] if not entry.startswith(word)]
def insert_word(hash_function, word):
    key = sum(map(ord, word))
    index = hash_function(key)

    existing_entry_index = next((i for i, entry in enumerate(hash_table[index]) if entry.startswith(word)), None)

    if existing_entry_index is not None:
        # Update the existing entry
        hash_table[index][existing_entry_index] = word
    else:
        # Insert the new element at the head of the stack
        hash_table[index] = [word] + hash_table[index]

