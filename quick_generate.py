from PIL import Image 
import os
import random
import json

trait_dict = {}

def init_files():
    for (root, dirs, files) in os.walk('./images'):
        # print(root, dirs, files)
        if len(files):
            trait_dict[root[9:]] = files


def generate(count):
    unique = {}
    tokenId = 1
    times = 0
    while times < count:
        new_nft_kind = []
        new_nft_dir = []
        metadata = []
        for _layer in trait_layer:
            kinds = trait_dict[_layer]
            kind = random.choice(kinds)
            new_nft_kind.append(kind)
            trait_file = os.path.join('./images', _layer, kind)
            new_nft_dir.append(trait_file)
            _meta_dict = {'trait_type': _layer, 'value': kind[:-4]}
            metadata.append(_meta_dict)

        # print(new_nft_kind, new_nft_dir)
        unique_key = ''.join(new_nft_kind)
        if unique.get(unique_key, None) is None:
            img = None
            for _dir in new_nft_dir:
                _img = Image.open(_dir).convert('RGBA')
                if img:
                    img = Image.alpha_composite(img, _img)
                else:
                    img = _img

            convert_rgb = img.convert('RGB')
            file_name = str(tokenId) + '.png'
            convert_rgb.save('./nfts/' + file_name)

            with open('./metadata/{}.json'.format(str(tokenId)), 'w') as f:
                json.dump(metadata, f)
            tokenId += 1
            times += 1

def main(count=10):
    init_files()
    generate(count)


if __name__ == '__main__':
    # config trait layer.
    # the layer order is the bottom layer must set first in the list
    # e.x. Usually the background image is at the top of the list
    trait_layer = ['backgrounds', 'furs', 'hats', 'ears', 'mouths', 'eyes', 'clothes']
    # the number of unique NFTs you want to generate
    count = 1
    main(count)