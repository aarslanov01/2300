'''
Question 2: Reverse a string word by word

Write a Python class to reverse a string word by word.

'''

class String: 
    
    def __init__(self, word):
        self.word = word
        
    #function to reverse    
    def reverse(self):
        self.reverse = self.word[::-1].split()
        print(self.reverse)
        
def main():
    #take the input 
    word = String(str(input('whats the word: ')))
    word.reverse()
        
        
if __name__ == "__main__":
    main()
