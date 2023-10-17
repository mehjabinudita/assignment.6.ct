total_confidence = 0
count = 0


file_name = input("Enter a file name: ")

try:
    
    with open(file_name, 'r') as file:
        
        for line in file:
            if line.startswith("X-DSPAM-Confidence:"):
               
                confidence = float(line.split(":")[1])
                total_confidence += confidence
                count += 1

    if count > 0:
        average_confidence = total_confidence / count
        print(f"Average spam confidence: {average_confidence}")
    else:
        print("No lines found in the specified format in the file.")

except FileNotFoundError:
    print(f"File cannot be opened: {file_name}")
except Exception as e:
    print(f"An error occurred: {e}")
