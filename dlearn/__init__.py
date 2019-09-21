from dlearn.iris import IrisModel
from dlearn.lena import LenaModel
from dlearn.fashion import Fashion
from dlearn.img_editor import ImgEditor
from dlearn.face import Face
from dlearn.cat_mosaic import CatMosaic
from dlearn.face_mosaic import FaceMosaic

import matplotlib.pyplot as plt
if __name__ == '__main__':
    def print_menu():
        print('0. EXIT')
        print('1. IRIS DATA')
        print('2. IRIS SCATTER')
        print('3. 경계선')
        print('4. LENA 이미지 인식')
        print('5. FASHION 이미지 인식')
        print('6. 이미지 편집')
        print('7. 얼굴 인식')
        print('8. 고양이 모자이크')
        print('9. 얼굴 모자이크')
        return input('CHOOSE ONE\n')

    while 1:
        menu = print_menu()
        if menu=='0':
            print('EXIT')
            break
        elif menu =='1':
            m= IrisModel()
            print('RESULT : %s '% m.get_iris())
            break

        elif menu =='2':
            m=IrisModel()
            m.draw_scatter()
            break

        elif menu =='3':
            m=IrisModel()
            m.plot_decision_regions()
            break
        elif menu =='4':
            m=LenaModel()
            m.execute()
            break
        elif menu =='5':
            m=Fashion()
            #m.fashion_show()
            arr=m.create_model()
            predictions=arr[0]
            test_labels=arr[1]
            img=arr[2]
            i =20
            plt.figure(figsize=(6,3))
            plt.subplot(1,2,1)
            m.plot_image(i,predictions,test_labels,img)
            plt.subplot(1,2,2)
            m.plot_value_array(i,predictions,test_labels)
            plt.show()
            break
        elif menu=='6':
            m=ImgEditor()
            m.ImgCut()
            break
        elif menu=='7':
            m=Face()
            m.read_file()
            break
        elif menu=='8':
            m=CatMosaic()
            m.img_mosaic()
            break
        elif menu=='9':
            m=FaceMosaic()
            m.face_mosaic()


