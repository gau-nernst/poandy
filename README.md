# Poandy

Simple Python wrapper for Oanda (https://developer.oanda.com/rest-live-v20/introduction/).

## Setup

1. Create neccessary files.

   ```
   # navigate to Poandy directory
   cd poandy
   # create a file called "secrets.json". It should contain your oanda api key. E.g.
   {
       "token": "7851c27f3bb2bc0f39g3c6d6a3c6b42509e-4015643c1a6ca4651b0c6bd836bc8b8"
   }
   ```

2. Setup virtual environment, activate and install neccessary dependencies. For Windows and Linux, the requirements files are at `requirements/win-64.txt` and `requirements/linux-64.txt` respectively.

   ```
   # Open Anaconda Prompt as Administrator, create virtual environment and install dependencies.
   conda create -n poandy python=3.8.5
   conda install -n poandy -y requests pandas black pytest
   # activate virtual environment (activation required everytime before working on repo)
   conda activate poandy
   # when done
   conda deactivate
   ```

## Linter

Use flake8 without line length limit. If using vscode, include the following in settings.json.

    ```
    "python.linting.flake8Args": ["--max-line-length=200"]
    ```

## Formatter

Black is the default code formatter. To format all files in the directory, run the following command on the command prompt.

```
cd poandy
black .
```

If using vscode, include the following settings in your settings.json file.

```
"python.formatting.provider": "black",
"editor.formatOnSave" : true,
"editor.defaultFormatter": null
```

Vscode should now automatically format your code based on Black style guide whenever you hit save.

## Test

    pytest
