# Serverless Deep Learning Deploy examples

## Training the Malaria detection model

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

## Running the demo server

Enter the `/example_web_page` directory and install the libs:
```bash
npm i
```

To start the server:
```bash
node server.js
```

The demo page will be served in `localhost:4000`