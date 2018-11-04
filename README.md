# Example of the dynamic nature of objects in Python.

## Instructions

This repo shows the difference between:

- class variables AKA static variables (`useUppercase`)
- instance variables (`str` and `times`)

If we are using **good coding practices**, we would define all variables in the class definition, as is done in `normal.py`.

But Python also allows for **dynamically adding** variables. This is demonstrated in `dynamic.py`. Note that is usually **not good practice**!

Compare this with *compiled* (vs. *interpreted*) languages like C++, Java or C# where using the variables before they are defined, would result in **compilation errors**.

## Notes

Javascript (another *interpreted* language, just like Python) also supports **adding attributes to objects dynamically**. For an example, clone this repo (https://github.com/enablecomputer/SnakeDirection), open `snake.html`, read the `avatar.js`-source, open the Javascript-console in the browser and experiment with the available commands.

(Note that C# has the `dynamic` keyword since 4.0: https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/types/using-type-dynamic)
