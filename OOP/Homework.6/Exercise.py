import re

class Regex():
    def __init__(self, mail_or_ip):
        self.set_ipv6(mail_or_ip)
        self.set_mail(mail_or_ip)
    def set_ipv6(self, ipv6):
        self.__ipv6 = ipv6
    def set_mail(self, mail):
        self.__mail = mail
    def get_ipv6(self):
        return self.__ipv6
    def get_mail(self):
        return self.__mail
    def is_ipv6(self):
        an = "[1-9a-zA-Z]{4}"
        pattern = an+"\:\:"+an+"\:\:"+an+"\:\:"+an+"$"
        res = re.findall(pattern, self.get_ipv6())
        if len(res) > 0:
            print("It's ipv6.")
        else:
            print("It's not ipv6.")
    def is_mail(self):
        print(self.get_mail())
        dom = ["[ru]*$", "[com]*$", "[ai]*$", "[net]*$", "[io]*$"]
        res = []
        for i in dom:
            pattern = "\w{1,}[\_\-\.\*]\w{1,}@\w{1,}\."+i
            res += re.findall(pattern, self.get_mail())
        if len(res) > 0:
            print("It's E-mail.")
        else:
            print("It's not E-mail.")

ip = Regex("b1Sd::b1kd::b1Sd::sajh")
# ip.is_ipv6()
mail = Regex("artyom.vancyan2000@gmail.com")
# mail.is_mail()