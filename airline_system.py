#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 09:06:06 2025

@author: haoooyu
"""
import random
import string

class SeatBookingSystem():
    def __init__(self):
        self.rows = 80
        self.cols = ["A","B","C","X","D","E","F"]
        self.seats = self.seats_table()
        self.bookings = {}  # Store passenger details
        self.existing_refs = set()
        
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
    def check_availability(self, seat):
        if not self.is_valid_seat(seat):
            return False
        return self.seats[seat] == "F"

    
    #Print the current seat reservation status in a structured format
    def display_seats(self):
        print("\nCurrent seat reservation status:\n")

        col_width = 8
        header = "    " + "".join(col.ljust(col_width) for col in self.cols)
        print(header)
        print("-" * len(header))

        for row in range(1, self.rows + 1):
            row_display = f"{str(row).rjust(3)} "
            for col in self.cols:
                seat_id = f"{row}{col}"
                seat_value = self.seats[seat_id]
                row_display += seat_value.ljust(col_width)
            print(row_display)

        print("\nLegend:")
        print("'F' = Free | 'X' = Aisle | 'S' = Storage | Booking Reference = Reserved")


    #book a seat if available.
    #allow the user to book a seat by entering their details
    def book_seat(self, seat):
        if not self.is_valid_seat(seat):
            return

        if self.seats[seat] == "F":
            passport = input("Enter your passport number: ").strip()
            first_name = input("Enter your first name: ").strip()
            last_name = input("Enter your last name: ").strip()
            
            booking_ref = self.generate_booking_reference()
            self.seats[seat] = booking_ref
            self.bookings[booking_ref] = {
                "passport": passport,
                "first_name": first_name,
                "last_name": last_name,
                "seat": seat
            }
            print(f"Seat {seat} booked successfully! Booking Reference: {booking_ref}")
        else:
            print("This seat is unavailable, please choose another one.")

    #free a seat if it has been booked
    def free_seat(self,seat):
        while True:
            if not self.is_valid_seat(seat):
                continue 

            booking_ref = self.seats.get(seat)
            if booking_ref in self.bookings:
                del self.bookings[booking_ref]  # Remove passenger details
                self.seats[seat] = "F"
                print(f"Seat {seat} is now free.")
                break
            else:
                print(" This seat is already free or has no valid booking.")
            
    #Generate a unique 8-character booking reference
    def generate_booking_reference(self):
        while True:
            reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            if reference not in self.existing_refs:
                self.existing_refs.add(reference)
                return reference
            
    #Check if the seat exists in the seating chart
    def is_valid_seat(self, seat):
        if seat in self.seats:
            return True
        print("Invalid seat number! Please enter a correct one.")
        return False
    
    # Lookup booking by booking reference
    def lookup_booking_by_reference(self):
        ref = input("Enter your 8-character booking reference: ").strip().upper()
        if ref in self.bookings:
            passenger = self.bookings[ref]
            print("\n Booking Details Found:")
            print(f"Reference: {ref}")
            print(f"Name     : {passenger['first_name']} {passenger['last_name']}")
            print(f"Passport : {passenger['passport']}")
            print(f"Seat     : {passenger['seat']}")
        else:
            print("No booking found with this reference.")
    
    #Main menu loop for the seat booking system.
    def run(self):
        while True:
            print("Please select an option:")
            print("1. Check availability of seat")
            print("2. Book a seat")
            print("3. Free a seat")
            print("4. Show booking status")
            print("5. Exit program")
            print("6. Lookup booking by reference")
            choice = input("please enter your choice: ").strip()
            
            if choice == "1":
                seat = input("Please enter the seat which you want to check ").strip().upper()
                if self.check_availability(seat) :
                    print(f"seat{seat} is available")
                else:
                    print(f"seat{seat} is unavailable")
            elif choice == "2":
                seat = input("Please choose your seat: ").strip().upper()
                self.book_seat(seat)
            elif choice == "3":
                seat = input("Please enter the seat which need to be free: ").strip().upper()
                if self.is_valid_seat(seat):
                    self.free_seat(seat)
            elif choice == "4":
                self.display_seats()
            elif choice == "5":
                print("Bye!")
                break
            elif choice == "6":
                self.lookup_booking_by_reference()
            else:
                print("Please enter again")
            
if __name__ == "__main__":
    system = SeatBookingSystem()
    system.run()
            
            
            
            
            
            
            
            
            
            
            
            
            