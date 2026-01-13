from database import get_connection

def create_booking():
    customer_id = int(input("Customer ID: "))
    room_id = int(input("Room ID: "))
    check_in = input("Check-in date: ")
    check_out = input("Check-out date: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO TBL_BOOKING
        (customer_id, room_id, check_in, check_out, booking_status)
        VALUES (?, ?, ?, ?, 'Booked')
    """, (customer_id, room_id, check_in, check_out))

    cur.execute("""
        UPDATE TBL_ROOM SET status='Occupied'
        WHERE room_id=?
    """, (room_id,))

    conn.commit()
    conn.close()
    print("Booking created")
