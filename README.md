# TestCaseElf

Tese cases generating helper tool

## 1. Objective

1. Specific the range of each field and output the product of the test case in a dictionary fashion
2. Ability to chain each combination (Maybe in a pipeline)

## 2. Expected Behavior

### Case 1 - Direct initialization:

INPUT:

```python
firstname = ['Michael', 'Gal']
lastname = ['Jackon', 'Gadot']
```
OUTPUT:

```python
[
    {
        'firstname': 'Michael', 
        'lastname': 'Jackon'
    },
    {
        'firstname': 'Michael', 
        'lastname': 'Gadot'
    },
    {
        'firstname': 'Gal', 
        'lastname': 'Jackon'
    },
    {
        'firstname': 'Gal', 
        'lastname': 'Gadot'
    },
]

```

### Case 2 - using pipeline:

```PYTHON
(
    VarField(firstname=['Michael', 'Gal']) 
    | VarField(lastname=['Jackon', 'Gadot']) 
    | FixField(region='Earthman')
) -> 
[
    {
        'firstname': 'Michael', 
        'lastname': 'Jackon',
        'region': 'Earthman'
    },
    {
        'firstname': 'Michael', 
        'lastname': 'Gadot',
        'region': 'Earthman'
    },
    {
        'firstname': 'Gal', 
        'lastname': 'Jackon',
        'region': 'Earthman'
    },
    {
        'firstname': 'Gal', 
        'lastname': 'Gadot',
        'region': 'Earthman'
    },
]
```

## TODO

1. Chain behavior between objects VarField and FixField
2. Pipeline similar to Celary one
3. Able to trasform to a pandas DataFrame or CSV file
