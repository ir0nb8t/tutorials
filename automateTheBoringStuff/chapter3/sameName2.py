# sameName.py taken from automatetheboringstuff.com/chapter3/

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
