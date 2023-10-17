try:
    file_name = input("Enter a file name : ")
    
    with open(file_name, 'r') as file:
        for line in file:
        
            print(line.upper(), end='')  
    
except FileNotFoundError:
    print("Error: The specified file does not exist.")
except Exception as e:
    print(f"An error occurred: {str(e)}")