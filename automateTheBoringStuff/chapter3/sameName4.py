# sameName4.py taken from automatetheboringstuff.com/chapter3/

def spam():
    print(eggs) # ERROR!!!
    eggs = 'spam local'

eggs = 'global'
spam()
