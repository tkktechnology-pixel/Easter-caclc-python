#------------------------------------------------------------------------------
#
# Module:     Easter:
# Purpose:    Caculates Easter Sunday for any year
#  ver 1.0.0.0
#   This software is protected by national and international copyright. 
#   Any unauthorized use, reproduction or modification is unlawful and 
#   will be prosecuted. Commercial and non-private application of the 
#   software in any form is strictly prohibited unless otherwise granted
#   by the authors.
#   
# (c) 2026 TKK Technology 
#
#------------------------------------------------------------------------------






# Easter Calculator using the Meeus/Jones/Butcher algorithm
# Computes the date of Western (Gregorian) Easter for any given year
def easter_date(year: int) -> tuple[int, int]:
    """
    Calculate the date of Easter Sunday (Western/Gregorian)
    for the given year.
        Returns: (month, day) where month = 3 (March) or 4 (April)
    """
    # Step 1: Basic decompositions of the year
    a = year % 19          # Position in 19-year lunar cycle
    b = year // 100        # Century number
    c = year % 100         # Year within the century
    
    # Step 2: Century-based corrections
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    
    # Step 3: Approximate Paschal full moon
    h = (19 * a + b - d - g + 15) % 30
    
    # Step 4: More corrections within the century
    i = c // 4
    k = c % 4
    
    # Step 5: Find weekday offset for the full moon
    l = (32 + 2 * e + 2 * i - h - k) % 7
    
    # Step 6: Final adjustment factor
    m = (a + 11 * h + 22 * l) // 451
    
    # Step 7: Compute month and day
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    
    return month, day
def month_name(month: int) -> str:
    """Convert numeric month (3 or 4) to name."""
    if month == 3:
        return "March"
    elif month == 4:
        return "April"
    else:
        return f"Month {month}"  # Fallback

if __name__ == "__main__":
    # Ask user for a year
    try:
        year_input = input("Enter a year (e.g., 2028): ")
        year = int(year_input)
        
        # Compute Easter date
        month, day = easter_date(year)
        
        # Print the result
        print(f"In {year}, Easter Sunday falls on {month_name(month)} {day}.")
        
    except ValueError:
        print("Please enter a valid whole number for the year.")
