with open('usr_and_pass.txt') as file:
    i = 1
    for line in file:

        get_username = line.split('|')[0]
        get_password = line.split('|')[1]
        def run_remote():
            
        print(get_username)
        print(get_password)
