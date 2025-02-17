# Remove the pass and call the function to perform write.
    # Read the file that was created while writing.
    # Make the changes in the file by appending some material.
    # Again read the same file.

'''
Print all the output of the function.
For better representation, please use jupyter.
Will also aid in easy maintanence of files for submissions.
'''

from contextlib import contextmanager

@contextmanager
def genericFileFunction (filename, method):
    file = open (filename, method)
    yield file
    file.close ()

if __name__ == '__main__':
    try:
        with genericFileFunction("trial.txt","w") as f:
            f.write("Namaste, I am UmarShaikh.")
            print("\nWriting complete!")

        with genericFileFunction("trial.txt","r") as f:
            print(f.read())

        with genericFileFunction("trial.txt","a") as f:
            f.write(" I am a student.")
            print("\nAppending complete!")

        with genericFileFunction("trial.txt","r") as f:
            print(f.read())

    except Exception as e:
        print(e)

     
Writing complete!
Namaste, I am UmarShaikh.

Appending complete!
Namaste, I am UmarShaikh. I am a student.
