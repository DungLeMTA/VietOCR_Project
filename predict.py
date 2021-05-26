import matplotlib.pyplot as plt
from PIL import Image
import  os
import  time

from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg
from vietocr.train import Trainer
# pretrain: C:\Users\Dung/.cache\torch\hub\checkpoints\vgg19_bn-c79401a0.pth


config = Cfg.load_config_from_file('./config.yml') # sử dụng config của các bạn được export lúc train nếu đã thay đổi tham số
# config = Cfg.load_config_from_name('vgg_transformer') # sử dụng config mặc định của mình
# config['weights'] = './weights/transformerocr.pth' đường dẫn đến trọng số đã huấn luyện hoặc comment để sử dụng pretrained model của mình
# config['device'] = 'cpu' # device chạy 'cuda:0', 'cuda:1', 'cpu'

# khởi tạo predict
detector = Predictor(config)

dir = 'B:\PycharmProjects\VietOCR_Project\\result_linecut\\'
img_dir=os.listdir(dir)

for i, img_file in enumerate(img_dir):
    img = Image.open(dir+img_file)
    start = time.time()
    s = detector.predict(img, return_prob=True) # muốn trả về xác suất của câu dự đoán thì đổi return_prob=True
    end = time.time()
    print('%12s'%img_file,': %.2f giây'%(end-start),' ',s)


# img = './result_linecut/01800.png'
# img = Image.open(img)
# # dự đoán
# s = detector.predict(img, return_prob=True) # muốn trả về xác suất của câu dự đoán thì đổi return_prob=True
# print(s)
# img.show()