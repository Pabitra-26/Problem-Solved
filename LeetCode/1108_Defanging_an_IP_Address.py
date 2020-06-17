"""Problem name: Defanging an IP Address
Description: Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]"
Strategy= use the replace function: string.replace(old,new,count)"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")

