Python Flask API that talks to the NepClock32.


Can run in a docker container. 

##Endpoints

GET, POST, DELETE `/clock` <br/>
POST `/clock/commitCommands` <br/>
GET `/health` <br/>


```
# 'func': fields.String,
# 'param': fields.Integer,
# 'showTime': fields.Integer,
# 'RGB': fields.Integer
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