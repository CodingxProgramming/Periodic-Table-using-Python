import periodictable

# Get element information by atomic number
# try:
    #atomic_number = int(input("Enter the atomic number of the element: "))
#element = periodictable.elements[n]
# for n in range(1,119):
for n in range(1,119):
    element = periodictable.elements[n]
    # try:
    print(f"Number: {n:<4}       Name: {element.name:<15}      \t\tSymbol: {element.symbol:^8}     \t\tAtomic Mass: {element.mass:^8}      \t\tDensity: {element.density or 'N/A':^8}")
        # print("Symbol: {element.symbol}")
        # print("Atomic Mass: {element.mass}")
        # print("Density: {element.density}")
        # print("Molar Heat: {element.molar_heat}")
        # print("Melting Point: {element.melt}")
        # print("Boiling Point: {element.boil}")
        # print("Phase: {element.phase}")
    # except ValueError:    
        # print("Invalid input. Please enter an integer.")
    # except KeyError:
    #     print("Element not found for the given atomic number.")
    # except AttributeError:
    #     print("Attribute not found for this element.")
    # except Exception as e:
    #     print(f"An error occurred: {e}")