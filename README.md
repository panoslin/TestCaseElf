# TestCaseElf

Tese cases generating helper tool

## 1. Objective

1. Specific the range of each field and output the product of the test case in a key-value fashion
2. Ability to chain each combination (In a pipe)
2. Out put the test cases in different format such as JSON/pandas.DataFrame/CSV

## 2. Expected Behavior

### Using pipeline:

```PYTHON
(
    Field(region='Earthman')
    * Field(lastname=['Jackson', 'Gadot'])
    * Field(firstname=['Michael', 'Gal'])
    + Field(age=10)
) -> 
[
   {
      "age":10,
      "firstname":"Michael",
      "lastname":"Jackson",
      "region":"Earthman"
   },
   {
      "age":10,
      "firstname":"Gal",
      "lastname":"Jackson",
      "region":"Earthman"
   },
   {
      "age":10,
      "firstname":"Michael",
      "lastname":"Gadot",
      "region":"Earthman"
   },
   {
      "age":10,
      "firstname":"Gal",
      "lastname":"Gadot",
      "region":"Earthman"
   }
]
```

### 3. TODO

1. [Unit testing](https://mp.weixin.qq.com/s/zYpEXK6YTkZ5C6uU2kkexQ) for TestCaseElf🤣
2. Documentation
3. CI/CD in GitHub Action

