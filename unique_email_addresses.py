class Solution:
    
    def get_local_name(self, email):
        for i, letter in enumerate(email):
            if letter == '@':
                local = email[:i]
                domain = email[i:]
        return local, domain
    
    def isValid(self, email):
        for l in email:
            if l == '@':
                return True
        return False
    
    def find_patterns(self, local_name):
        cleaned_local_name = ''
        for i, letter in enumerate(local_name):
            if letter == '+':
                break
            if letter != '.':
                cleaned_local_name += letter
                
        return cleaned_local_name
                
    
    def numUniqueEmails(self, emails: List[str]) -> int:
        valid_emails = []
        for email in emails:
            if self.isValid(email):
                local_name, domain_name = self.get_local_name(email)
                email = self.find_patterns(local_name) + domain_name
                valid_emails.append(email)
                
        return len(set(valid_emails))