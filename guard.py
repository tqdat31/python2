def input_personal_info():
    
    person_infor = {}
    person_infor['name']  = input('Hay nhap ten cua ban: ')
    person_infor['gender'] = input('Hay nhap gioi tinh cua ban (nam/nu): ')
    person_infor['age'] = int(input('Hay nhap tuoi cua ban: '))
    person_infor['experience'] = int(input('Hay nhap so nam kinh nghiem cua ban trong nghanh: '))
    person_infor['height'] = float(input('Hay nhap chieu cao cua ban ( theo met): '))
    person_infor['weight'] = float(input('Hay nhap can nang cua ban(theo kg): '))
    return person_infor

def isQualified(person):

    def printQualifiedMessage():
        print('Xin chuc mung ban da trung tuyen')
    
    def printNotQualifiedMessage():
        print('Xin loi ban kh hop le')
    
    if person['gender'] == 'nam':
        printNotQualifiedMessage()
        return False
    
    if 30 <= person['age'] <= 40:
        if person['experience'] >= 5 and person['height'] >= 1.55 and person['weight'] <= 45:
            printQualifiedMessage()
        elif person['experience'] >= 2 and person ['height'] >= 1.6 and person['weight'] <= 50:
            printQualifiedMessage()
        else:
            printNotQualifiedMessage()
    
    elif 18 <= person['age'] < 30:
        if person['height'] >= 1.6 and person['weight'] <= 50:
            printQualifiedMessage()
        else:
            printNotQualifiedMessage()
    
    else:
        printNotQualifiedMessage()

isQualified(input_personal_info())


