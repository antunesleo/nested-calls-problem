# nested-calls-problem
Collection of APIs to explore how slow blocking operation impact APIs performance

## Getting Started

Each API has two endpoints /delay and /other. The delay endpoint is very slow, simulating a slow IO call, blocking the process of the request.
The other endpoint has no IO and should respond instantly.

### How the test works

We you use vegeta to put load in the /delay endpoint. When the /other endpoint is affected by such load, it means that we are generating cascading failures

### Running for Go

Run server with
```
go main.go
```

Stress /delay endpoint with
```
vegeta attack -targets=config.txt -rate=300/s -duration=200s | vegeta report
```

Ensure that /other endpoint is still working
```
http localhost:8000/other
```

### Running for FAST API async

Run server with
```
uvicorn main:app
```

Stress /delay endpoint with
```
vegeta attack -targets=config.txt -rate=300/s -duration=200s | vegeta report
```

Ensure that /other endpoint is still working
```
http localhost:8000/other
```

### Running for FAST API Sync

Run server with
```
uvicorn main:app
```

Stress /delay endpoint with
```
vegeta attack -targets=config.txt -rate=300/s -duration=200s | vegeta report
```

Ensure that /other endpoint is still working
```
http localhost:8000/other
```
