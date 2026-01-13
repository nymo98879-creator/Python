from database import get_connection

def show_available_rooms():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT room_id, room_number, room_type, price
        FROM TBL_ROOM
        WHERE status='Available'
    """)

    for r in cur.fetchall():
        print(r)

    conn.close()

# from database import get_connection

# def add_room():
#     room_number = input("Room Number: ")
#     room_type = input("Room Type: ")
#     price = float(input("Price: "))
#     status = "Available"

#     conn = get_connection()
#     cur = conn.cursor()

#     cur.execute("""
#         INSERT INTO TBL_ROOM (room_number, room_type, price, status)
#         VALUES (?, ?, ?, ?)
#     """, (room_number, room_type, price, status))

#     conn.commit()
#     conn.close()

#     print("Room added successfully")

