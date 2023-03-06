'''
io inbuilt module allows to work with inputs and outputs for modifying the data.
one of methods for working with strings is StringIO:
it has several functions: read, write, getvalue, readable, writable, close (after performing which the error occured - the stream is closed to work with
'''
import io

# initialise the string
immutable_string = "Immutable string"

# open text stream
mutable_string = io.StringIO(immutable_string)

# read the stream
print(mutable_string.read())
# Immutable string

# search for index in stream
mutable_string.seek(0, 2)

# modify the value by adding the new value at the end of stream
mutable_string.write(" changed to Mutable")

# check the new value of stream
print(mutable_string.getvalue())
# Immutable string changed to Mutable

# close the stream and check it is not readable and writable anymore
mutable_string.close()
print(mutable_string.writable())
print(mutable_string.readable())

https://docs.python.org/3/library/io.html#io.StringIO
