import time
import numpy as np

with open('subset_elemets.txt') as f:
    subset_elements = f.read().split('\n')
    
with open('all_elements.txt') as f:
    all_elements = f.read().split('\n')
    
def withloop():
    """Name: function1
Description: This is a function which finds the the common elements in two lists using a for loop"""
    start = time.time()
    verified_elements = []

    for element in subset_elements:
        if element in all_elements:
            verified_elements.append(element)

    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start))
    
def withnumpy():
    """Name: function2
Description: This is a function which finds the the common elements in 
                 two lists using an inbuilt function called intersect1d in numpy"""
    start = time.time()
    verified_elements=np.intersect1d(all_elements,subset_elements)

    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start))
    
def withDS():
    """Name: function3
Description: This is a function which finds the the common elements in  two lists using set.
    """
    start=time.time()

    #using datastructure set.
    verified_elements=list(set(all_elements)&set(subset_elements))

    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start))
    
def main():
    print(withloop.__doc__)
    withloop()
    print(withnumpy.__doc__)
    withnumpy()
    print(withDS.__doc__)
    withDS()
    
if __name__ == "__main__":
    main()