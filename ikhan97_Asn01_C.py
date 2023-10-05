'''
CS1026a 2023
Assingment 1 Project 1 - Part C
Isa Khan
251337547
ikhan97
10/03/2023
'''

# Function that converts flops to appropriate units
# Based on the amount of flops this method divides by the appropriate figure and appends both the 
# adjusted number and units to a list that is returned then printed with the rest of the data
def convert_units (raw_flops):
    converted = []

    # Keeping units as FLOPS
    if raw_flops < 1000:
        converted.append(round(raw_flops , 2))
        converted.append("FLOPS")

    # Converting units to kiloFLOPS
    elif raw_flops >= 1000 and raw_flops < 1000000:
        adjusted_flops = raw_flops / 1000
        converted.append(adjusted_flops)
        converted.append("kiloFLOPS")
    
    # Converting units to megaFLOPS
    elif raw_flops >= 1000000 and raw_flops < 1000000000:
        adjusted_flops = raw_flops / 1000000
        converted.append(adjusted_flops)
        converted.append("megaFLOPS")

    # Converting units to gigaFLOPS
    elif raw_flops >= 1000000000 and raw_flops < 1000000000000:
        adjusted_flops = raw_flops / 1000000000
        converted.append(adjusted_flops)
        converted.append("gigaFLOPS")

    # Converting units to teraFLOPS
    elif raw_flops >= 1000000000000 and raw_flops < 1000000000000000:
        adjusted_flops = raw_flops / 1000000000000
        converted.append(adjusted_flops)
        converted.append("teraFLOPS")

    # Converting units to petaFLOPS
    elif raw_flops >= 1000000000000000 and raw_flops < 1000000000000000000:
        adjusted_flops = raw_flops / 1000000000000000
        converted.append(adjusted_flops)
        converted.append("petaFLOPS")
    
    # Converting units to exaFLOPS
    elif raw_flops >= 1000000000000000000 and raw_flops < 1000000000000000000000:
        adjusted_flops = raw_flops / 1000000000000000000
        converted.append(adjusted_flops)
        converted.append("exaFLOPS")
    
    # Converting units to zetaFLOPS
    elif raw_flops >= 1000000000000000000000 and raw_flops < 1000000000000000000000000:
        adjusted_flops = raw_flops / 1000000000000000000000
        converted.append(adjusted_flops)
        converted.append("zettaFLOPS")
    
    # Converting units to yottaFLOPS
    elif raw_flops >= 1000000000000000000000000:
        adjusted_flops = raw_flops / 1000000000000000000000000
        converted.append(adjusted_flops)
        converted.append("yottaFLOPS")

    # Returing list that contains the converted figure and units
    return converted


print("Project One (1) - Part C : The Moore the Merrier")

# Prompting for user input
current_transistors = int(input("Starting Number of transistors: ")) # Current number of transistors
current_year = int(input("Starting Year: ")) # Current year
total_years = int(input("Total Number of Years: ")) # Total amount of years

# Setting the ending year for the program
end_year = current_year + total_years


print("\nYEAR : TRANSISTORS : FLOPS:")

# Loop that iterates through from the start to end year
while current_year <= end_year:
    
    # Converting current amount of transistors to flops
    raw_flops = current_transistors * 50
    
    # Sending flops to be converted to appropriate unit
    adjusted_units = convert_units(raw_flops)
    
    # Printing the values per set year
    print(f"{current_year} {current_transistors:,} {adjusted_units[0]:.2f} {adjusted_units[1]} {raw_flops:,}")
    
    # Incrementing year and transistor values for the following 2 year cycle
    current_transistors = current_transistors * 2
    current_year += 2

print("\nEnd Part One (01) - Project C\nIsa Khan ikhan97 251337547")