# code-compiler

### Introduction
- A python package that can be used to compile or intrepet a piece of code from different languages from your python program
and then do the desired action from the output.

### Prerequisites

* Python3
* gcc
* java

### Supported Languages

* C
* C++
* Java
* Python

### Installation

- Go to the root of your project directory  
```cd /path/to/project/root/```
- Clone this repo  
```git clone https://github.com/anirudh1200/code-compiler.git```
- Import the module in your code
```python
from compile import compile as compiler
```

#### Python Standard Libray packages used:
-  [subprocess](https://docs.python.org/3.6/library/subprocess.html)
-  [uuid](https://docs.python.org/3.6/library/uuid.html)
-  [os](https://docs.python.org/3.6/library/os.html)
-  [sys](https://docs.python.org/3.6/library/sys.html)

# Documentation
The module provides two functions:

* **compiler.init()**
  - This function must be run, before using the ```compile()``` function. It creates a folder named ```tmpcode``` where the code is stored and compiled.

* **compiler.compile(code, source, input, callback(, timeout))**
  - Parameters:
    - code (Integer): Enter the code of the language you want to compile in. 
    
      | Language | Code |
      |----------|------|
      | C        | 1    |
      | C++      | 2    |
      | Java     | 3    |
      | Python3  | 4    |
    
    - source (String): Enter the source code which you want to compile
    
    - input (String): Enter the input which you want to give to the code. Pass a blank string if there is no input
    
    - callback (Function): The callback function to handle the result. The callback function takes these parametes
      - **data** (Object)
        - stdout: Contains the output. Empty if there is a error.
        - stderr: Contains the error message if there are any
    
    - timeout (integer): This is optional paramater. Default is 5 seconds. Takes in integer i.e. seconds before process terminates.
      
# Example
A example program to print Hello World in C:
```python
from compile import compile as compiler

compiler.init()

compiler.compile(1, '#include<stdio.h>\n int main() {printf("Hello Wolrd"); return 0;}', "", print)
```

Output: 
```
{ 
  stdout: 'Hello Wolrd', 
  stderr: null 
 }
```
***
    
Nodejs implementation of this package is available at https://github.com/Rex1911/compile-code

