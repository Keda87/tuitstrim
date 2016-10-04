# tuitstrim
Simple script to mining twitter stream.

# Usage:
- Create `config.ini` file and put your twitter key.

    ```
    [twitter]
    access_token = ...
    access_token_secret = ...
    consumer_key = ...
    consumer_secret = ...
    ```
- Install required dependencies. `pip install -r requirements.txt`
- Change database name on [this](https://github.com/Keda87/tuitstrim/blob/master/app.py#L18)
- Change stream tags with your own on [this](https://github.com/Keda87/tuitstrim/blob/master/app.py#L46)
- Run the script. `$ python app.py`
