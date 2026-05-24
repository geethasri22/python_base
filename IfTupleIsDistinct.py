arr = tuple(map(int, input().split()))
# Print "True" if all elements of tuple are different, otherwise print "False"
if len(arr)==len(set(arr)):
    print("True")
else:
    print("False")
