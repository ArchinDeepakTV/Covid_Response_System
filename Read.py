import psycopg2

from config import config


def id_extraction(rs):
    l = []
    for i in rs:
        # converting set to list
        k = list(i)
        # taking the first element from the list and append it to the list
        l.append(k[0])
    # Converting integer list to string list
    s = [str(i) for i in l]

    # Join list items using join()
    res = int("".join(s))
    return res


def final_report():
    """ query data from the hospitals table """
    sql = "SELECT hospital_id, hospital_name FROM hospitals ORDER BY " \
          "distance asc, beds, oxy_tanks"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        print("The Order of Approach: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def read_hospital_one(ID):
    # read number of beds available in a hospital
    sql = """SELECT hospital_name, beds FROM hospitals "
                    "WHERE hospital_id = '%s'"""
    conn = None
    updated_rows = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, [ID])
        result = cur.fetchall()
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
        return result

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


def read_hospital_two(ID):
    # read number of oxygen tanks available in a hospital
    sql = """SELECT hospital_name, oxy_tanks FROM hospitals "
                    "WHERE hospital_id = %s"""
    conn = None
    updated_rows = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, [ID])
        result = cur.fetchall()
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows
