# [program name]
# Pavel Stoimenov
# [date]
# AS Computer Science

# Creates a max size of the stack
def one(max_size=10):
    try:
        stack = []
        top = -1
        return stack, top, max_size  
    except Exception as e:
        print("Error occurred:", e )

# Returns if the stack is empty
def two(top):
    try:
        return top==-1   
    except Exception as e:
        print("Error occurred:", e )

# Returns if the stack is full
def three(top,max_size):
    try:
        return top == (max_size - 1)   
    except Exception as e:
        print("Error occurred:", e )


# gets total element count
def four(top):
    try:
        return top+1   
    except Exception as e:
        print("Error occurred:", e )


# Pushes a item
def five(stack,top,max_size,item):
    try:
        if three(top, max_size):
            print("OVERFLOW ERROR: Stack is full!")
            print(f"Cannot add '{item}' - capacity reached.")
            return top
        top = top + 1
        stack.append(item)
        print(f"Pushed '{item}' onto the stack.")
        return top
    
    except Exception as e:
        print("Error occurred:", e )


# Pops a stack
def six(stack,top):
    try:
        if two(top):
            print("UNDERFLOW ERROR: Stack is empty!")
            print("Cannot pop from an empty stack.")
            return None, top
        item = stack[top]
        top = top - 1
        print(f"Popped '{item}' from the stack.")
        return item, top

    except Exception as e:
        print("Error occurred:", e )

# Peeks at the stack
def seven(stack,top):
    try:
        if two(top):
            print("Stack is empty - nothing to peek.")
            return None

        item = stack[top]
        print(f"Top item is: '{item}'")
        return item
    
    except Exception as e:
        print("Error occurred:", e )


# Displays the stack
def eight(stack,top):
    try:
        if two(top):
            print("\nStack is empty.")
            return

        print("\n--- Current Stack ---")
        print("TOP")
        for i in range(top, -1, -1):
            print(f" [{i}] {stack[i]}")
        print("BOTTOM")
        print(f"Size: {four(top)}/{len(stack)}")
        print("-------------------\n")
        pass   
    except Exception as e:
        print("Error occurred:", e )


# Menu of the stack
def nine():
    try:
        print("\n=== STACK OPERATIONS ===")
        print("1. Push (add item)")
        print("2. Pop (remove item)")
        print("3. Peek (view top item)")
        print("4. Display stack")
        print("5. Check if empty")
        print("6. Check if full")
        print("7. Get stack size")
        print("8. Exit")
        print("========================")
        pass   
    except Exception as e:
        print("Error occurred:", e )



# Main program for the stack
def main():
    try:
        stack, top, max_size = one(20)
        print(f"Stack initialised with capacity: {max_size}")
        while True:
            nine()
            choice = input("\nEnter your choice (1-8): ")
            if choice == '1':
                item = input("Enter item to push: ")
                top = five(stack, top, max_size, item)
            elif choice == '2':
                item, top = six(stack, top)
            elif choice == '3':
                seven(stack, top)
            elif choice == '4':
                eight(stack, top)
            elif choice == '5':
                print("Empty:", two(top))
            elif choice == '6':
                print("Full:", three(top, max_size))
            elif choice == '7':
                print("Size:", four(top))
            elif choice == '8':
                print("Exiting programme. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1-8.")
        pass   
    except Exception as e:
        print("Error occurred:", e )    

if (__name__ == "__main__"):
    main()

''' _ _                  _@_
^\_(*_*)_/} - - - -  {\_[^_^] __,,
I will get u          HaHa u sad cuz i got hair
'''





