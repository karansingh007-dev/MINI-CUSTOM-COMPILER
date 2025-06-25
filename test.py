from compiler import run

test_code = """
set x as 5;
set y as 3;
display x + y;
"""

output = run(test_code)
print(output)
