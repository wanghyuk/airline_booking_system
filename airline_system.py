#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 09:06:06 2025

@author: haoooyu
"""

class SeatBookingSystem():
    def __init__(self):
        self.rows = 80
        self.cols = ["A","B","C","X","D","E","F"]
        self.seats = self.seats_table()
        
    #Generate a dictionary representing the seating arrangement.
    def seats_table(self):
        seats = {}
        for row in range(1, self.rows+1):
            for cols in self.cols:
                seatsid = f"{row}{cols}"
                if cols == "X":
                    seats[seatsid] = "X"
                elif row <= self.rows-2 and row >= self.rows-4 and cols in ["D","E","F"]:
                    seats[seatsid] = "S"
                else:
                    seats[seatsid] = "F"
                    
        return seats
    #Check if a seat is available. Returns True if available, False otherwise.
    def check_availability(self,seat):
        return self.seats.get(seat, "N/A") == "F"
    
    #Print the current seat reservation status in a structured format
    def display_seats(self):
        print("\nCurrent seat reservation status:\n")
        print("   " + "  ".join(self.cols))
        for row in range(1, self.rows + 1):
            row_display = f"{row:2} "
            for col in self.cols:
                seat_id = f"{row}{col}"
                row_display += self.seats[seat_id] + "  "
            print(row_display)
        print("'F' is available, 'X' is isles, 'S' is storage area, 'R' is already booked")
        
    #book a seat if available.
    def book_seat(self, seat):
        if self.seats[seat] == "F":
            print("Your seat is booked successfully")
            self.seats[seat] = "R"
        else:
            print("This seat is unavailable, please choose another one")
        
    #free a seat if it has been booked
    def free_seat(self, seat):
        if self.seats[seat] == "R":
            self.seats[seat] = "F"
            print(f"Status update, free this seat {seat} successfully")
        else:
            print("This seat has not been booked, can not free it")
            
    #Main menu loop for the seat booking system.
    def run(self):
        while True:
            print("Please choose roles")
            print("1. Check availability of seat")
            print("2. Book a seat")
            print("3. Free a seat")
            print("4. Show booking status")
            print("5. Exit program")
            choice = input("please enter your choice: ").strip()
            
            if choice == "1":
                seat = input("Please enter the seat which you want to check ").strip().upper()
                if self.check_availability(seat):
                    print(f"seat{seat} is available")
                else:
                    print(f"seat{seat} is unavailable")
            elif choice == "2":
                seat = input("Please choose your seat: ").strip().upper()
                self.book_seat(seat)
            elif choice == "3":
                seat = input("Please enter the seat which need to be free: ").strip().upper()
                self.free_seat(seat)
            elif choice == "4":
                self.display_seats()
            elif choice == "5":
                print("Bye!")
                break
            else:
                print("Please enter again")
            
if __name__ == "__main__":
    system = SeatBookingSystem()
    system.run()
            
            
            
            
            
            
            
            
            
            
            
            
            