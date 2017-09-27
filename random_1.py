class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
        
        
rev = Reverse("spam")
print iter(rev)
print rev.__iter__()
print rev.__next__()
print rev.__next__()
print rev.__next__()
print rev.__next__()

                
class FileOwners:

    @staticmethod
    def group_by_owners(files):
        new_files = {}
        for key,value in files.items():
            new_files.setdefault(value, []).append(key)
        return new_files

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))
    
    
class Palindrome:
    
    @staticmethod
    def is_palindrome(word):
        if len(word) == 0 or len(word) == 1:
            return None
        else:
            word = word.lower()
            rev_word = word[::-1]
            if word == rev_word:
                return True
            return False
            
    
            

print(Palindrome.is_palindrome('Deleveled'))