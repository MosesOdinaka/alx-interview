# 0x07. Rotate 2D Matrix

AlgorithmPython

For the “0. Rotate 2D Matrix” project, you are tasked with implementing an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. This challenge requires a good understanding of matrix manipulation and in-place operations in Python. Below are the key concepts and resources that you need to grasp in order to successfully complete this project.

### Concepts Needed:

1.  **Matrix Representation in Python**:
    
    -   Understanding how 2D matrices are represented using lists of lists in Python.
    -   Accessing and modifying elements in a 2D matrix.
2.  **In-place Operations**:
    
    -   Performing operations on data without creating a copy of the data structure.
    -   The importance of minimizing space complexity by modifying the matrix in place.
3.  **Matrix Transposition**:
    
    -   Understanding the concept of transposing a matrix (swapping rows and columns).
    -   Implementing matrix transposition as a step in the rotation process.
4.  **Reversing Rows in a Matrix**:
    
    -   Manipulating rows of a matrix by reversing their order as part of the rotation process.
5.  **Nested Loops**:
    
    -   Using nested loops to iterate through 2D data structures like matrices.
    -   Modifying elements within nested loops to achieve the desired rotation.

### Resources:

-   **Python Official Documentation**:
    
    -   [Data Structures (list comprehensions, nested list comprehension)](https://intranet.alxswe.com/rltoken/eZc_ELGxUgkuc4kkE_fd7Q "Data Structures (list comprehensions, nested list comprehension)")
    -   [More on Lists](https://intranet.alxswe.com/rltoken/0ORj179giGhGe8jpcxBkXg "More on Lists")
-   **GeeksforGeeks Articles**:
    
    -   [Inplace rotate square matrix by 90 degrees](https://intranet.alxswe.com/rltoken/9T8w4mtiIIRDtfLSmEmrLA "Inplace rotate square matrix by 90 degrees")
    -   [Transpose a matrix in Single line in Python](https://intranet.alxswe.com/rltoken/JdIFvtej2hMW-Wd9ABHMOA "Transpose a matrix in Single line in Python")
-   **TutorialsPoint**:
    
    -   [Python Lists](https://intranet.alxswe.com/rltoken/rFmzUTpaLGqDXjGA6D9eYw "Python Lists") for basics of list manipulation in Python.

By understanding these concepts and utilizing the provided resources, you will be able to approach the problem methodically, first transposing the matrix and then reversing each row to achieve a 90-degree clockwise rotation. This project not only tests your ability to manipulate 2D matrices but also challenges you to think about optimizing your solution to operate in-place, thus improving their problem-solving and algorithmic thinking skills in Python.

## Additional Resources

-   [Mock Technical Interview](https://intranet.alxswe.com/rltoken/4GPWA9C2AJHtpdGxuIHEPA "Mock Technical Interview")

## Requirements

### General

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.10)
-   All your files should end with a new line
-   The first line of all your files should be exactly `#!/usr/bin/python3`
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   Your code should use the `pycodestyle` style (version 2.8.0)
-   You are not allowed to import any module
-   All modules and functions must be documented
-   All your files must be executable

## Tasks

### 0\. Rotate 2D Matrix

mandatory

Given an `n` x `n` 2D matrix, rotate it 90 degrees clockwise.

-   Prototype: `def rotate_2d_matrix(matrix):`
-   Do not return anything. The matrix must be edited **in-place**.
-   You can assume the matrix will have 2 dimensions and will not be empty.

```
jessevhedden$ cat main_0.py
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

jessevhedden$
jessevhedden$ ./main_0.py
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]
jessevhedden$
```

**Repo:**

-   GitHub repository: `alx-interview`
-   Directory: `0x07-rotate_2d_matrix`
-   File: `0-rotate_2d_matrix.py`

Done?! Check your code

×

#### Correction of "0. Rotate 2D Matrix"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox

×

#### Recommended Sandbox

Running only

### 1 image<small class="ml-2">(1/2 Sandboxes spawned)</small>

### Ubuntu 20.04Asleep

Basic Ubuntu 20.04, with vim, emacs, curl, wget and all needed for Foundations

WakeDestroy

Copyright © 2024 ALX, All rights reserved.

×

#### Markdown Guide

#### Emphasis

```
**<strong>bold</strong>**
*<em>italics</em>*
~~<strike>strikethrough</strike>~~
```

#### Headers

```
# Big header
## Medium header
### Small header
#### Tiny header
```

#### Lists

```
* Generic list item
* Generic list item
* Generic list item

1. Numbered list item
2. Numbered list item
3. Numbered list item
```

#### Links

```
[Text to display](http://www.example.com)
```

#### Quotes

```
&gt; This is a quote.
&gt; It can span multiple lines!
```

#### Images

CSS style available: `width, height, opacity`

```
![](http://www.example.com/image.jpg)
![](http://www.example.com/image.jpg | width: 200px)
![](http://www.example.com/image.jpg | height: 124px | width: 80px | opacity: 0.6)
```

#### Tables

```
| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John     | Doe      | Male     |
| Mary     | Smith    | Female   |

<em>Or without aligning the columns...</em>

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John | Doe | Male |
| Mary | Smith | Female |
```

#### Displaying code

````
`var example = "hello!";`

<em>Or spanning multiple lines...</em>

```
var example = "hello!";
alert(example);
```
````

window.codySettings = { widget\_id: "9993bc72-2258-452b-a4bf-b2fe1ad5e0d7" }; !function(){var t=window,e=document,a=function(){var t=e.createElement("script");t.type="text/javascript",t.async=!0,t.src="https://trinketsofcody.com/cody-widget.js";var a=e.getElementsByTagName("script")\[0\];a.parentNode.insertBefore(t,a)};"complete"===document.readyState?a():t.attachEvent?t.attachEvent("onload",a):t.addEventListener("load",a,!1)}(); window.userpilotSettings={token:"NX-b636a33d"}; <iframe id="nr-ext-rsicon" style="position: absolute; display: none; width: 50px; height: 50px; z-index: 2147483647; border-style: none; background: transparent; top: 447px; left: 225px;"></iframe>

#cody-wrapper .cody-launcher { position: var(--position) !important; left: var(--left) !important; right: var(--right) !important; bottom: var(--launcher-bottom) !important; border-radius: 9999px !important; border: 0 !important; padding: 0 !important; box-sizing: border-box !important; z-index: 999999 !important; overflow: hidden !important; display: flex !important; align-items: center !important; justify-content: center !important; transition: box-shadow, scale 300ms linear !important; animation: cody-launcher-pulse 4s infinite !important; background-color: var(--background-color) !important; color: var(--text-color) !important; cursor: pointer !important; --icon-margin: 12px; --close-icon-margin: 16px; } #cody-wrapper { --position: fixed; --left: unset; --right: 20px; --launcher-bottom: 20px; --frame-bottom: 90px; --background-color: #FBD647; --text-color: #020617; --shadow-color: 251, 214, 71; } @media screen and (max-width: 512px) { #cody-wrapper { --left: unset; --right: 10px; } } #cody-wrapper .cody-launcher:hover { scale: 1.1 !important; } #cody-wrapper .cody-launcher .cody-close-icon { display: none !important; } #cody-wrapper\[data-launcher-open\] .cody-launcher .cody-icon { display: none !important;; } #cody-wrapper\[data-launcher-open\] .cody-launcher .cody-close-icon { display: block !important;; } #cody-wrapper .cody-iframe { z-index: 99999 !important; transition: visibility .5s, opacity .5s linear !important; background-color: #fff !important; position: fixed !important; left: var(--left) !important; right: var(--right) !important; bottom: var(--frame-bottom) !important; height: 75vh !important; width: 448px !important; border-radius: 10px !important; overflow: hidden !important; box-shadow: 0 2px 4px rgba(0, 18, 26, .08), 0 3px 12px rgba(0, 18, 26, .16), 0 2px 14px 0 rgba(0, 18, 26, .2) !important; border: 0 !important; display: none !important; } @media screen and (max-height: 667px) { #cody-wrapper .cody-iframe { height: calc(100vh - 110px) !important; } } @media screen and (max-width: 448px) { #cody-wrapper .cody-iframe { width: calc(100vw - 20px) !important; } } #cody-wrapper\[data-launcher-open\] .cody-iframe { display: block !important; } @keyframes cody-launcher-pulse { 0%, 100% { box-shadow: 0 0 18px 4px rgba(var(--shadow-color), 0.8); } 50% { box-shadow: 0 0 12px 3px rgba(var(--shadow-color), 0.4); } }

<iframe id="_hjSafeContext_17233527" title="_hjSafeContext" tabindex="-1" aria-hidden="true" src="about:blank" style="display: none !important; width: 1px !important; height: 1px !important; opacity: 0 !important; pointer-events: none !important;"></iframe>userpilot.identify("\\x3cUNIQUE USER ID\\x3e",{name:"John Doe",email:"customer@example.com",created\_at:"1519205055"});userpilot.reload();
