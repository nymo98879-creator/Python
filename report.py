from database import get_connection

def daily_income():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT invoice_date, SUM(total)
        FROM TBL_INVOICE
        GROUP BY invoice_date
    """)

    for r in cur.fetchall():
        print(r)

    conn.close()
