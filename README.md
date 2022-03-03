# What?

NFT images and matedata simple quick generator

metadata for Opensea [standard](https://docs.opensea.io/docs/metadata-standards).


# How?

 - Copy your images layer file directory to images
 - Config your trait layer in source code
 - Config the number of unique NFTs you want to generate
```
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

thanks your cool doggos :)
