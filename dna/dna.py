from sys import argv
import csv
import re

def max_repeat_length(s, substring):
    # how many times each substring repeats
    repeat = [0] * len(s)
    for i in range(len(s) - len(substring), -1, -1):
        if s[i: i + len(substring)] == substring:
            if i + len(substring) > len(s) - 1:
                repeat[i] = 1
            else:
                repeat[i] = 1 + repeat[i + len(substring)]
    
    return max(repeat)
                
        



def match(reader, substring_repeat):
     for line in reader:
         person = line[0]
         values = [int(val) for val in line[1:]]
         if values == substring_repeat:
             print(person)
             return
         
     print("No match")
     
     
    
    
def main():
    db_size = str(argv[1])
    with open(db_size) as db:
        reader = csv.reader(db)
        substring = next(reader)[1:]
        
        sequence = str(argv[2])
        with open(sequence) as seq:
            s = seq.read()
            substring_repeat = [max_repeat_length(s, seq) for seq in substring] 
        
        match(reader, substring_repeat)
        

if __name__ == "__main__":
    main()
            
        
    