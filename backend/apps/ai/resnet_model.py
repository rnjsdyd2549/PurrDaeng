from sre_parse import CATEGORIES
import numpy as np
import os
import cv2
import h5py
from keras.models import load_model

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, '48_class_model_3.h5')
CATEGORIES = [
        "개운죽", "관음죽", "괴마옥", "극락조화", "금전수", "녹태고", "다바나 고사리", "더피 고사리", "둥근 잎 아카시아",
        "드라세나 드라코", "드라세나 마지나타", "디지고테카 아랄리아", "떡갈잎 고무나무", "라벤더", "로즈마리", "립살리스 트리고나",
        "마란타 레우코네우라", "마오리 소포라", "마오리 코로키아", "멕시코 소철", "멜라니 고무나무", "목마가렛", "몬스테라 델리시오사",
        "몬스테라 아단소니", "몬스테라 알보 바리에가타", "무늬 푸미라", "무늬벤자민 고무나무", "미모사", "바로크 벤자민", "박쥐란", "백묘국", "베고니아",
        "벵갈 고무나무", "보스턴 고사리", "브레이니아 니보사", "블루스타 고사리", "산세베리아", "산세베리아 문샤인", "세네시오 칸디칸스",
        "소철", "수박 페페로미아", "수채화 고무나무", "스위트 바질", "스킨답서스", "스투키", "스파티필름", "사계귤", "드라세나 맛상게아나"
]

class Resnet:
     
    def __init__(self, path):
        self.resnet_model = load_model(path)
        
    def dataization(self,img_path):
        image_w = 224
        image_h = 224
        ff = np.fromfile(img_path, np.uint8)
        img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
        img = cv2.resize(img, None, fx=image_w/img.shape[1], fy=image_h/img.shape[0])
        return (img/224)
  
    def calc_percent(self, y_prob, y_sort):
        result = []
        result_percent = []
           
        for i in range(-1,-4,-1):
            for j in range(48):
                if y_prob[0][j] == y_sort[0][i]:
                    index_num = j
                    temp=CATEGORIES[index_num]
                    temp_percent=round((y_prob[0][index_num]*100), 2)
                    break
            result.append(temp)
            result_percent.append(temp_percent)
            
        return (result, result_percent)

    def predict(self, img_path):
        test = []
        test.append(self.dataization(img_path))
        y_prob= self.resnet_model.predict(np.array(test), verbose=0)
        y_sort = np.sort(y_prob, axis = 1)
        
        result, result_percent = self.calc_percent(y_prob, y_sort)
             
        for i in range(3):
            print(f'top_{i+1} : {result[i]}, {result_percent[i]}%')
        
        content = {}
        for i in range(3):
            content[f'top{i+1}'] = {
                "name" : result[i],
                "percent" : result_percent[i],
            }
        
        return content 

# model = Resnet('48_class_model_3.h5')
# print(model.predict('test.jpeg'))