#Iterators and generators
#Generator DONT holds entire result in memory, it yield one result at a time . Hint uses next() method to see the real working
def generator(number):
    for item in number:
        yield item * item 

lst = [2,3,4,5,6,7]

my_generator = generator(lst)
print 'Print all the elements where generators are applied.'
for my_iterator in my_generator:
    print my_iterator 
    
#Generator Comprehension 
my_gen = (n*n for n in lst)
print 'Generate only First  Element From List =: ' , next(my_gen)
print 'Generate only Second Element From List =: ' , next(my_gen)

print 'Topic Covers Iterator'
str = 'abcdefgh'
my_iterator = iter(str) 

#for item in my_iterator:
#    print 'All String elements =:' , item

print next(my_iterator)
print next(my_iterator)
    
    