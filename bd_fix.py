import sqlite3

con = sqlite3.connect("roads.sqlite")

cur = con.cursor()

cur.execute('PRAGMA foreign_keys=off;')
cur.execute('BEGIN TRANSACTION;')
cur.execute('ALTER TABLE tbl_roads RENAME TO old_table_roads;')
cur.execute('CREATE TABLE tbl_roads (road_code INTEGER PRIMARY KEY, name TEXT NOT NULL,length_km NUMERIC NOT NULL, '
            'geomtype TEXT NOT NULL, coordinates TEXT NOT NULL);')
cur.execute('INSERT INTO tbl_roads (road_code, name, length_km, geomtype, coordinates) SELECT road_code, name, '
            'length_km, geomtype, coordinates FROM old_table_roads;')
cur.execute('DROP TABLE old_table_roads;')
cur.execute('COMMIT;')
cur.execute('PRAGMA foreign_keys=on;')

'''cur.execute('ALTER TABLE tbl_azs ADD COLUMN id INTEGER PRIMARY KEY AUTOINCREMENT')

cur.execute('COMMIT')'''

print(cur.execute("SELECT * FROM tbl_roads").fetchall())
