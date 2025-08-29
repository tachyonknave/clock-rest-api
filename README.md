# Python Flask API that talks to the NeoClock32.


### Endpoints

GET, POST, DELETE `/clock` <br/>
POST `/clock/commitCommands` <br/>
GET `/health` <br/>


- 'func': fields.String,
- 'param': fields.Integer,
- 'showTime': fields.Integer,
- 'RGB': fields.Integer
```
clock_data = {
         "func": "TWENTY_FOUR_CLOCK",
         "param": None,
         "showTime": "200",
         "RGB": "0x030303"}
```

Buffer commands by POSTing clock_data json. A commit will send those commands
to the clock. A GET will return the current buffer. A DELETE will clear the 
buffer. 

A GET health will return an OK if the service is running. 

### Docker

`docker build -t clock_api .`
`docker run --rm -d -p 5001:5001 --name clock-api -e CLOCK_URL=http://192.168.1.168 clock_api`
`curl http://127.0.0.1:5001/health`