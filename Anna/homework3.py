# How Python Runs Programs

# 1. What is the Python interpreter?
"""
    Interpreter-ը այն ծրագիրն է, որը կարդում է Python-ի կոդը (մարդու գրած) և կատարում է այն։
    a = 3
    b = 7
    c = a + b
    print(c)
    1.   source code - python կոդը գրում ենք homework 3.py ֆայլում, սա մարդուն հասկանալի կոդ է։
    2.   byte code - python interpretator-ը source code-ը փոխում է byte code-ի: Byte code-ը մեքենային ավելի հասկանալի կոդ է։
        .pyc ֆայլում է պահվում
    3.  PVM( Python Virtual Machine ) - կատարում է bytecode-ը։
        PVM-ն թարգմանիչՆ է, որը կատարում է հետևյալ քայլերը՝
        Բեռնում է փոփոխականները a և b հիշողության մեջ։
        Կատարում է BINARY_ADD → a + b = 10։
        Ստեղծում է փոփոխական c և պահում արդյունքը։
        Կատարում է PRINT_RESULT → տպում է 10։
    4.  Output
        PVM-ը ավարտում է կատարումը, և տեսնում ենք տպված արդյունքը։
        10

    Python Interpreter-ի դերը՝
        Կարդում է source code-ը
        Compile-ավորում է այն bytecode-ի
        Bytecode-ը փոխանցում է PVM-ին
        PVM-ը կատարում է բոլոր հրահանգները և տպում արդյունքը
        եթե չլիներ Interpreter-ը, մեր պարզ Python կոդը չէր կարողանա աշխատել, որովհետև CPU-ն չի հասկանում անմիջապես Python կոդը։

"""
# 2. What is source code?
""" 
    Source code-ը այն կոդն է, որը գրում ենք Python լեզվով (.py ֆայլում)։
    Interpreter-ը կարդում է source code-ը, թարգմանում է այն bytecode-ի, ապա PVM-ը կատարում է։
"""
# 3. What is byte code?
""" Byte code-ը միջանկյալ կոդ է, որը interpreter-ը ստանում է source code-ից։ Այն ավելի մոտ է մեքենային հասկանալի հրահանգներին։ Byte code-ը պահվում են .pyc ֆայլում։  """
# 4. What is the PVM?
"""  PVM (Python Virtual Machine)-ը Python-ի վիրտուալ մեքենան է, որը թարգմանում է byte code-ը։ Կարելի է ասել մի խումբ մարդիկ տարբեր լեզուներով են խոսում, իսկ PVM-ը միջնորդ է, որը թարգմանում է նրանց խոսքը, որ կարողանան համագործակցել։"""
# 5. Name two or more variations on Python’s standard execution model.
""" 
   Կան մի քանի վարիացիաներ․
    1) Jython – Python-ի իրականացում Java - ով։
    2) PyPy – Python interpreter JIT (Just-In-Time) կոմպիլացիայով։  Ավելի արագ է քան CPython-ը։
    3) IronPython - Python-ի իրականացում, աշխատում է .NET / C# ։
    4) CPython -  C լեզվով է գրված ։
"""
# 6. How are CPython, Jython, and IronPython different? Why prefer one over another
"""     
        CPython – Python-ի ամենատարածված իրականացման տարբերակն է։ Գրված է C լեզվով։ Ամենաապահովն ու լայն օգտագործվողը։
        Jython – աշխատում է Java Virtual Machine-ի վրա, կարելի է Python կոդը ինտեգրել Java ծրագրերի հետ։
        IronPython – աշխատում է .NET միջավայրում, հարմար է, եթե պետք է Python-ը ինտեգրել C# կամ .NET ծրագրերի հետ։

    Եթե սովորական ծրագրավորում ենք անում → CPython։
    Եթե աշխատում ենք Java միջավայրում → Jython։
    Եթե .NET միջավայրում → IronPython։
"""

# 7. What are Stackless and PyPy? Why prefer one over another
"""  
    Stackless Python – փոփոխված տարբերակ է, որն ավելի լավ է աշխատում բազմաթիվ փոքր գործառույթների հետ։ Հարմար է մեծ ծավալի parallel հաշվարկների համար։
    PyPy – Python-ի արագացված տարբերակն է, որն ունի JIT (Just-In-Time) compiler։ Այն արագ է CPython-ից։

    Եթե արագություն  → PyPy։
    Եթե պետք են հաշվարկներ → Stackless։ 
"""
# 8. Draw Interpreter’s working process.
"""  
    source code → byte code → PVM → արդյունք։
"""
# 9. How do you run/start a python program?
"""
     terminal / cmd -ում -   python one.py
    
    PyCharm-ում Run կոճակով։
"""
# 10. What is interactive prompt and how do you use it. (Hint: always use it. Play with it as much as possible)
"""  
    Interactive Prompt-ը (կամ REPL — Read–Eval–Print Loop) այն միջավայրն է, որտեղ դու անմիջապես կարող ես գրել Python կոդ և ստանալ արդյունքը։(Command Prompt)
    Այն  սկսվում է երեք >>> նշանով։

    >>> 2 + 3
    5
    
    >>> print("python")
    python
    
    >>> for i in range(3):
...     print(i)
...
0
1
2

"""
# 11. Investigate and explain the usage of hash bang/shebang/bash bang
""" 
    Shebang (#!) հատուկ տող է Python ֆայլի սկզբում, որը ցույց է տալիս, թե որ interpreter-ով պետք է աշխատի ծրագիրը։

    Օրինակ՝ ֆայլի սկզբում գրել՝
    
    #!/usr/bin/env python3
    
    
    Ասում է համակարգին, որ ծրագիրը պետք է բացել python3-ով։
    Հիմնականում օգտագործվում է Unix/Linux համակարգերում, որպեսզի .py ֆայլը կարելի լինի աշխատեցնել անմիջապես, առանց python հրաման գրելու։"""