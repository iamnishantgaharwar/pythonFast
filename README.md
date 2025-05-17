Install Python

And to use fast api we can do it with two way that is installing it globally andanother is installing in virtual env 

### To install globally we can do 
```pip3 install fastapi```

### To install in virtual env we need to make one first to do that we can use command ```python3 -m venv nameOfFile-env / path```

```python3 -m venv fastapi-env```

-m Stands for module means run module as a script


After this we installed uvicorn it's basically like node which helps us to listen http request and all 

same command pip install uvicorn to install it 

After that we create a main file which we want to listen on some port same as node's index or server.js file

Now to run the main file or we can say listen 

we need to write following command 
uvicorn main:app 

this will start the server

"main" is the file name which is "main.py"

"app" is the instance of fastapi which we declare in main.py e.g app = FastAPI()

we can also use --reload to reload the server


