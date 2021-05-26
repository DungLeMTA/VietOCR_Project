import matplotlib.pyplot as plt
from PIL import Image

from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg
from vietocr.model.trainer import Trainer

# pretrain: C:\Users\Dung/.cache\torch\hub\checkpoints\vgg19_bn-c79401a0.pth
config = Cfg.load_config_from_name('vgg_seq2seq')

print(config)

trainer = Trainer(config, pretrained=True)
trainer.config.save('/content/drive/MyDrive/VietOCR/config.yml')
trainer.visualize_dataset()
trainer.train()