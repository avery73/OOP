import CoinClass as c #import file name, not class name
    #c is an alias, easier and faster to type


# The main function.
def main():
       # Create an object from the Coin class.
       my_coin = c.Coin()   # this creates an instance called 'my_coin' of the class 'Coin()'

       # Display the side of the coin that is facing up.
       print('This side is up:', my_coin.get_sideup())    # notice you do not have to supply the argument/parameter

       # Toss the coin.
       print('I am going to toss the coin ten times:')
       for count in range(10):
           my_coin.toss()
           # my_coin.sideup = "Heads", toss method doesn't matter
           # beacuase you already set it to heads
           # if you put __ on every sideup on the other file, it ignores your heads
           # it over-rides the whole thing and makes it random
           # always hide your attributes
           
           # Display the side of the coin that is facing up.
           print('This side is up:', my_coin.get_sideup())

           


       

# Call the main function.

main()
