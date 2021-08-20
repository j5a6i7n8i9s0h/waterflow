# waterflow
<h2>Prerequisites</h2>

- Python3 with pip
- Make 3.8 + 

<h2>Setup</h2>

1. Build virtual python environment: 

```
make vp
```

2. Running application locally: <br
  ```
  make run_py CMD_LIST=i,j,k
  where i,j is the coord of the cup and k is the litres poured
  ```
4. Running tests: `make test`
   - This will generate a coverage report in `./output/coverage`. Opening `./output/coverage/index.html` will give a breakdown of the report
6. clean up: deleting virtual python and coverage reports -> `make clean` 
