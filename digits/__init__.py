from digits.hand_writing import HandWriting
if __name__ == '__main__':
    def print_menu():
        print('0. EXIT')
        print('1. 손글씨 인식')
        print('2. 손글씨 인식 러신머닝')
        print('3. 테스트')
        '''print('4. LENA 이미지 인식')
        print('5. FASHION 이미지 인식')
        print('6. 이미지 편집')
        print('7. 얼굴 인식')
        print('8. 고양이 모자이크')
        print('9. 얼굴 모자이크')'''
        return input('CHOOSE ONE\n')


    while 1:
        menu = print_menu()
        if menu == '0':
            print('EXIT')
            break
        elif menu =='1':
            m=HandWriting()
            m.read_file()
            break
        elif menu =='2':
            m=HandWriting()
            m.learning()
            break
        elif menu =='3':
            m=HandWriting()
            fname='./data/my2.png'
            print('테스트')

            print(m.test(fname))
            break