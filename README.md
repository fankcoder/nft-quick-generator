# About

Simple and quick generator NFT images and matedata with python

support Opensea metadata [standard](https://docs.opensea.io/docs/metadata-standards) .


# How to use

 - Copy your images layer file directory to images
 - Config probability with your images name. Use # symbol and probability number, the sum of the numbers in the same directory is 100.
 - Config your trait layer in source code trait_layer
 - Config the number of unique NFTs you want to generate
```
....
if __name__ == '__main__':
    ....
    # config below trait_layer and count
    trait_layer = ['backgrounds', 'furs', 'hats', 'ears', 'mouths', 'eyes', 'clothes']
    count = 1
```

# Run

**Python >= 3.6
```
pip install -r requirements.txt
python quick_generate.py
```

# Thanks

Example image using [cyberdoggos](https://github.com/cyberdoggos/generator)