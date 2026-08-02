import sqlite3

conn = sqlite3.connect("database/geoshield.db")
cursor = conn.cursor()

resources = [

# ---------------- FIRE ----------------

("Nairobi Fire HQ","Fire Station","Nairobi",-1.2866,36.8172,"Active",12,"999"),
("Mombasa Fire Station","Fire Station","Mombasa",-4.0435,39.6682,"Active",8,"999"),
("Kisumu Fire Station","Fire Station","Kisumu",-0.0917,34.7680,"Active",6,"999"),

# ---------------- HOSPITALS ----------------

("Kenyatta National Hospital","Hospital","Nairobi",-1.3014,36.8080,"Open",2000,"0202726300"),
("Moi Teaching Hospital","Hospital","Uasin Gishu",0.5143,35.2698,"Open",1200,"0532033471"),
("Coast General Hospital","Hospital","Mombasa",-4.0437,39.6684,"Open",900,"0412314204"),

# ---------------- POLICE ----------------

("Central Police Station","Police","Nairobi",-1.2841,36.8219,"Operational",400,"999"),
("Mombasa Central Police","Police","Mombasa",-4.0432,39.6680,"Operational",250,"999"),

# ---------------- RED CROSS ----------------

("Kenya Red Cross HQ","Red Cross","Nairobi",-1.3000,36.8200,"Ready",500,"0700395395"),

# ---------------- ST JOHN ----------------

("St John Ambulance HQ","St John","Nairobi",-1.2890,36.8170,"Ready",200,"0722200000"),

# ---------------- SCOUTS ----------------

("Rowallan National Scout Camp","Scouts","Nairobi",-1.2750,36.8800,"Ready",300,"0700000000"),

# ---------------- MILITARY ----------------

("Kahawa Barracks","Military","Nairobi",-1.1800,36.9300,"Operational",1500,"N/A"),

# ---------------- NEMA ----------------

("NEMA Headquarters","NEMA","Nairobi",-1.2920,36.8220,"Operational",300,"0202183718"),

]

cursor.executemany("""

INSERT INTO infrastructure
(name,category,county,latitude,longitude,status,capacity,contact)

VALUES(?,?,?,?,?,?,?,?)

""", resources)

conn.commit()
conn.close()

print("✅ Infrastructure Imported Successfully")