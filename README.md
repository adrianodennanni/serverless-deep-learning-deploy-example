# Serverless Deep Learning Deploy examples

1. Install the dependencies of this project with:
```
pip install -r requirements.txt
```

**WARNING!** Make sure to match your Python version according to this:

- Azure Functions uses Python 3.6

- AWS Lambda uses Python 3.6 or Python 3.7

- GCP Functions uses Python 3.7


2. Download the dataset from Kaggle, using the Kaggle API:
```
kaggle datasets download -d iarunava/cell-images-for-detecting-malaria
```

3. Unzip the downloaded `.zip` file to the root of this project with:
```
unzip cell-images-for-detecting-malaria.zip
```

4.Rename the directories and copy random files to validation split:
```
sh prepare_dataset.sh

```

4. Train the model:
```
python train.py
```
