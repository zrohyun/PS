#https://leetcode.com/explore/featured/card/wix-engineering/651/arrays-and-strings/4154/
from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniq_emails = {}
        for email in emails:
            local,domain = email.split("@")
            local = local.replace(".","").split("+")[0]
            if local in uniq_emails:
                uniq_emails[local].add(domain)
            else:
                uniq_emails[local] = set({domain})
        
        ans = 0
        for k,v in uniq_emails.items():
            ans += len(v)
        return ans


"""
Other Solution
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = "".join(local.split("."))
            
            unique_email = local + "@" + domain
            unique.add(unique_email)
        
        return len(unique)
"""