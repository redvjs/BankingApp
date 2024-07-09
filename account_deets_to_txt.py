# Dictionary to store each users account details is saved in text file "account_details.txt".
# Details are stored in consistent format in text file for easy extraction.
# Opens file in read mode, then strips leading and trailing whitespaces and splits each persons details by double newlines
# This is stored in a list like this ['dun1\nDuncan\nduncmaster\nDuncanLikesCoding123\n300\n300', 'vic1\nVico\nredvjs\nNetherlandsW1llW1n\n5\n5', 'wil1\nWilson\nwilsonistheman\n1WilsonAndADream\n250\n250']
# for loop to iterate over each list item in the file_content list. the users unique id is stored in variable unique_id which is the
def get_account_details_dict(unique_id):
    with open('account_details.txt', 'r') as file:
        file_content = file.read().strip().split('\n\n')
    account_details_dict = {}

    for line in file_content:
        lines = line.strip().split('\n')
        if lines[0] == unique_id:
            user_data = {
                'Name': lines[1],
                'Username': lines[2],
                'Password': lines[3],
                'Initial deposit': float(lines[4]),
                'Account balance': float(lines[5])
            }
            account_details_dict[unique_id] = user_data
    file.close
    return account_details_dict

# Nested dict containing account details is stored in variable account_details for access within the program
account_details = get_account_details_dict('dun1')
print(account_details)
def save_account_details_dict_to_file(account_details_dict, current_unique_id):
    with open('test.txt', 'w') as file:
        for unique_id, user_details in account_details_dict.items():
            if unique_id == current_unique_id:
                updated_user_details = [
                    unique_id,
                    f'{user_details['Name']}',
                    f'{user_details['Username']}',
                    f'{user_details['Password']}',
                    f'{user_details['Initial deposit']}',
                    f'{user_details['Account balance']}'
                ]
                file.write('\n'.join(updated_user_details) + '\n\n')
save_account_details_dict_to_file(account_details, 'dun1')