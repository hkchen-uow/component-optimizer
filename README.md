# MiCADO - Scaling Optimizer with Machine Learning Support

## Test program
From project root run
```python pure.py```

## Test flask
From project root run
```python helloMTA.py```

## Start program 
From project root run  
```python optimizer.py --cfg path/to_config_file```

```python optimizer.py --cfg config/config.yaml```

```python optimizer.py --cfg config/config.yaml --host=192.168.0.60```

## Test REST API 
__POST /optimizer/init__  
Initialize optimizer with the neccessary constants.  
```curl -X POST http://127.0.0.1:5000/optimizer/init --data-binary @test_files/optimizer_constants.yaml```  

```curl -X POST http://193.224.59.115:5000/optimizer/init --data-binary @test_files/optimizer_constants.yaml```
  
__GET /optimizer/training_data__  
Download zipped training data that contains both neural network and linear regression data.  
```curl -X GET http://127.0.0.1:5000/optimizer/training_data```  
  
__POST /optimizer/sample__   
Send a new training sample.  
```curl -X POST http://127.0.0.1:5000/optimizer/sample --data-binary @test_files/metrics_sample_example.yaml``` 

```curl -X POST http://193.224.59.115:5000/optimizer/sample --data-binary @test_files/metrics_sample_example.yaml```
  
__GET /optimizer/advice__     
Get scaling advice.  
```curl -X GET http://127.0.0.1:5000/optimizer/advice```  
