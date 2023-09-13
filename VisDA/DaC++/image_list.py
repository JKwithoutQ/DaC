import os
from typing import Optional
import os

def image_list(path: str, pre_path: Optional[str] = None, save_path: Optional[str] = None) -> None:
    """ lab from 0 to length-1
    """
    with open(save_path, 'w') as f:
        cate_lst = [cate for cate in os.listdir(path) if os.path.isdir(os.path.join(path, cate))]
        for lab, cate in enumerate(cate_lst):
            for img in os.listdir(os.path.join(path, cate)):
                if pre_path is None:
                    img_path = os.path.join(path, cate, img)
                else:
                    img_path = os.path.join(pre_path, path, cate, img)
                f.write(f'{img_path} {lab}\n')
    print(f'finish save path: {save_path}')


if __name__ == '__main__':
    image_list(path='./data/VISDA-C/train', save_path='./data/VISDA-C/train_list.txt')
    image_list(path='./data/VISDA-C/test', save_path='./data/VISDA-C/test_list.txt')
    image_list(path='./data/VISDA-C/validation', save_path='./data/VISDA-C/validation_list.txt')
