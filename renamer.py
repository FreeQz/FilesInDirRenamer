import os

print("Example:\n")
print("Path: C:\\Users\\mypc\\Desktop\\lolkek")
print("Extension: .png")
print("This will rename all files into .png")
print("Starting now...\n")

path = input("Path: ")
extension = input("Extension: ")
print("Working...")

for root, dirs, files in os.walk(path):
    for file in files:
        base = os.path.splitext(file)[0]
        os.rename(os.path.join(root,file), os.path.join(root,base+extension))

print("Done")
