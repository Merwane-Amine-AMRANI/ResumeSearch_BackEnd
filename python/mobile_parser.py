import re

def extract_mobile_number(text):
    phone = re.findall(re.compile(r'[0][0-9]+[ .-][0-9]+[ .-][0-9]+[ .-][0-9]+[ .-][0-9]+'), text)

    if phone:
        number = ''.join(phone[0])
        if len(number) > 10:
            return  number
        else:
            return number

