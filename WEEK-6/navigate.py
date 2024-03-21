import os 

docs = os.walk('./')
for doc in docs:
    for file in doc[2]:
        if file.endswith('.txt'):
            print(file)

 