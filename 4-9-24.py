
def avg(alist):
    try:
        return sum(alist) / len(alist)
    except ZeroDivisionError:
        print("The List is empty!")
        return
    except TypeError:
        print("The list is not purely numerical!")
        return float('nan')

l = []
avg(1)
