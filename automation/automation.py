import re

number_val = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
email_val  = re.compile(r'[\w\.-]+@[\w\.-]+')


def read_file(file_path):
    with open(file_path,'r') as f: return f.read()

def find_phone_number(text):
    output = re.findall(number_val, text)
    full_list = []
    for i in output:
        if len(i) == 7 or len(i) == 8: i = '206' +i
        number_only = filter(str.isdigit, i)
        number_string = ''.join(number_only)
        proper_format = number_string[0:3] + '-' + number_string[3:6] + '-'+ number_string[6:]
        if proper_format not in full_list: full_list.append(proper_format)
    return sorted(full_list)

def find_emails(text):
    output = re.findall(email_val, text)
    full_list = []
    [full_list.append(i) for i in output if i not in full_list]
    return sorted(full_list)

def write_content_to_file(arr, file_path):
    with open(file_path, 'w')as f:[f.write(i + '\n') for i in arr ]

contents = read_file('./potential-contacts.txt')
emails = find_emails(contents)
numbers = find_phone_number(contents)
write_content_to_file(numbers, './phone_numbers.txt')
write_content_to_file(emails, './emails.txt')