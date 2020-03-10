```
Generate art in 5 mins setup:

# 1. Download data from wikiart using robbiebarrat's script (https://github.com/robbiebarrat/art-DCGAN/blob/master/genre-scraper.py)
mkdir ./images
python genre-scraper.py --output_dir ./images --style cubism

# 2. Preprocess images to make them 1024x1024 (Remember to edit NAME inside preprocess.py file)
mkdir ./processed-images
python preprocess.py

# 3. Create TF dataset
python dataset_tool.py create_from_images datasets/cubism/ ./processed-images/cubism

# 4. Train (Remember to edit the config.py file)
python train.py

# 5. Generate (Remember to edit the import_example file)
python import_example.py
```

![Alt text](samples/1.png?raw=true "sample")
