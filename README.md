# share

## setup
```
pip install -r requirements.txt
```

### run for development
```
python view.py
```

### run for server
```
docker build -t eric_share .

docker run -d --restart always --network elk --network-alias eric_share --name=eric_share -p 8001:8001 -v /data_solid/configs:/data_solid/configs -v /data_solid/apps:/data_solid/apps eric_share:latest
```

