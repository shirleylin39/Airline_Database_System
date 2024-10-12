import sqlite3

def airline_table(c):
    conn = sqlite3.connect('airline_database.db')
    c = conn.cursor()

    #c.execute("DROP TABLE IF EXISTS Pilot")

    c.execute("""
      CREATE TABLE IF NOT EXISTS Pilot(
        PilotID TEXT PRIMARY KEY,
        LicenseID TEXT,
        Name TEXT,
        Nationality TEXT,
        Gender CHAR(1),
        DateofBirth DATE,
        OnboardDate DATE
      )
    """)

    c.execute("""
      INSERT OR IGNORE INTO Pilot VALUES
        ('256','ABC123','Kate Moss','United Kingdom','F','1988-01-16','2015-02-28'),
        ('512','DEF456','Michael Jackson','United States', 'M','1976-08-29','2002-07-11'),
        ('1024','GHI789','Usain Bolt', 'Jamaica','M','1986-08-21','2020-03-03'),
        ('2048','JKL123','Sully Sullenberger','United States','M','1951-01-23','1980-06-15'),
        ('3072','MNO456','Patty Wagstaff','United States','F','1951-09-11','1984-07-10'),
        ('4096','PQR789','Peggy Whitson','United States','F','1960-02-09','1986-06-08'),
        ('5120','STU123','Samantha Cristoforetti','Italy','F','1977-04-26','2001-11-15'),
        ('6144','VWX456','David Mackay','United Kingdom','M','1957-05-07','1994-02-15'),
        ('7168','YZA789','Eileen Collins','United States','F','1956-11-19','1990-05-04'),
        ('8192','BCD123','Yuri Malenchenko','Russia','M','1961-12-22','1988-01-01'),
        ('9216','EFG456','Koichi Wakata','Japan','M','1963-08-01','1992-10-12'),
        ('10240','HIJ789','Sunita Williams','United States','F','1965-09-19','1995-06-19'),
        ('11264','KLM123','Chris Hadfield','Canada','M','1959-08-29','1992-05-01'),
        ('12288','NOP456','Sally Wadsworth','Australia','F','1981-02-17','2008-04-09'),
        ('13312','QRS789','Yi-An Lin','Taiwan','F','1994-02-13','2021-04-01')
    """)

    c.execute("""
      CREATE TABLE IF NOT EXISTS Aircraft(
        AircraftID TEXT PRIMARY KEY,
        AircraftModel TEXT,
        Capacity INTEGER,
        ManufactureDate DATE,
        LastMaintainenceDate DATE
      )
    """)

    c.execute("""
      INSERT OR IGNORE INTO Aircraft VALUES
        ('A321003','A321',200,'2007-10-22','2023-09-16'),
        ('B777002','B777',388,'2014-02-13','2023-11-10'),
        ('A350006','A350',410,'2016-01-07','2023-06-09'),
        ('A320004','A320',180,'2005-06-15','2023-08-10'),
        ('B737800','B737',189,'2012-03-22','2023-10-05'),
        ('B747400','B747',416,'2001-09-30','2023-09-25'),
        ('A330300','A330',277,'2010-05-11','2023-07-20'),
        ('B787900','B787',296,'2018-02-14','2023-05-17'),
        ('A220100','A220',135,'2021-06-01','2023-07-10'),
        ('B777300','B777',396,'2013-11-07','2023-09-29'),
        ('A380800','A380',853,'2012-08-23','2023-06-14'),
        ('A319002','A319',144,'2003-04-30','2023-05-25'),
        ('B757200','B757',200,'2009-01-19','2023-03-30'),
        ('B767300','B767',250,'2007-10-03','2023-09-12'),
        ('A350900','A350',369,'2019-07-12','2023-09-10'),
        ('B787800','B787',242,'2017-05-25','2023-07-20')
    """)

    #c.execute("DROP TABLE IF EXISTS Flight")

    c.execute("""
      CREATE TABLE IF NOT EXISTS Flight(
        FlightID TEXT PRIMARY KEY,
        DepartureAirportCode TEXT,
        DepartureDateTime_Local DATETIME,
        ArrivalAirportCode TEXT,
        ArrivalDateTime_Local DATETIME,
        AircraftID TEXT, 
        PilotID TEXT,
        FOREIGN KEY(AircraftID) REFERENCES Aircraft(AircraftID),
        FOREIGN KEY(PilotID) REFERENCES Pilot(PilotID),
        FOREIGN KEY(DepartureAirportCode) REFERENCES Airport(AirportCode),
        FOREIGN KEY(ArrivalAirportCode) REFERENCES Airport(AirportCode)
      )
    """)

    c.execute("""
      INSERT OR IGNORE INTO Flight VALUES
        ('BA1499','GLA','2023-11-03 11:45','LHR','2023-11-03 13:10','A321003','256'),
        ('TG436','CGK','2023-11-05 19:05','BKK','2023-11-05 22:35','B777002','512'),
        ('CX840','HND','2023-11-09 17:20','JFK','2023-11-09 19:05','A350006','256'),
        ('SQ52','SIN','2023-12-01 08:30','SFO','2023-12-01 19:10','B787900','7168'),
        ('EK203','DXB','2023-12-03 02:30','JFK','2023-12-03 08:30','A380800','6144'),
        ('QF10','LHR','2023-12-05 21:15','SYD','2023-12-07 06:00','B787800','12288'),
        ('AF459','GIG','2023-11-25 16:55','CDG','2023-11-26 08:10','A350900','10240'),
        ('LH401','JFK','2023-11-18 16:00','FRA','2023-11-19 05:30','B747400','4096'),
        ('AA101','LAX','2023-11-15 13:45','LHR','2023-11-16 07:00','B777300','5120'),
        ('JL34','NRT','2023-11-20 11:20','SIN','2023-11-20 17:05','B767300','6144'),
        ('UA858','SFO','2023-12-01 10:25','NRT','2023-12-02 14:45','B787900','4096'),
        ('EK412','DXB','2023-12-08 10:15','SYD','2023-12-09 07:00','A380800','7168'),
        ('NZ2','LHR','2023-11-30 16:15','AKL','2023-12-01 05:30','B787800','10240'),
        ('DL108','ATL','2023-12-10 22:30','FRA','2023-12-11 12:30','A350006','11264'),
        ('BA75','LHR','2023-12-02 12:50','ACC','2023-12-02 19:25','B777300','8192'),
        ('AF22','CDG','2023-12-07 13:40','IAD','2023-12-07 16:10','A350900','6144'),
        ('CX880','HKG','2023-12-03 23:45','LAX','2023-12-03 19:45','B777300','4096'),
        ('LH778','FRA','2023-11-29 22:15','SIN','2023-11-30 17:50','A350900','12288'),
        ('QF128','HKG','2023-12-04 20:05','SYD','2023-12-05 08:30','B787800','8192')
    """)



    #c.execute("DROP TABLE IF EXISTS Airport")

    c.execute("""
      CREATE TABLE IF NOT EXISTS Airport(
          AirportCode TEXT PRIMARY KEY,
          City TEXT,
          Country TEXT,
          TimeZone TEXT
        )
    """)

    
    c.execute("""
      INSERT OR IGNORE INTO Airport VALUES
        ('GLA', 'Glasgow', 'United Kingdom', 'UTC+0'),
        ('LHR', 'London', 'United Kingdom', 'UTC+0'),
        ('CGK', 'Jakarta', 'Indonesia', 'UTC+7'),
        ('BKK', 'Bangkok', 'Thailand', 'UTC+7'),
        ('HND', 'Tokyo', 'Japan', 'UTC+9'),
        ('JFK', 'New York', 'United States', 'UTC-5'),
        ('SFO', 'San Francisco', 'United States', 'UTC-8'),
        ('DXB', 'Dubai', 'United Arab Emirates', 'UTC+4'),
        ('SYD', 'Sydney', 'Australia', 'UTC+10'),
        ('GIG', 'Rio de Janeiro', 'Brazil', 'UTC-3'),
        ('CDG', 'Paris', 'France', 'UTC+1'),
        ('FRA', 'Frankfurt', 'Germany', 'UTC+1'),
        ('LAX', 'Los Angeles', 'United States', 'UTC-8'),
        ('NRT', 'Tokyo', 'Japan', 'UTC+9'),
        ('AKL', 'Auckland', 'New Zealand', 'UTC+13'),
        ('ATL', 'Atlanta', 'United States', 'UTC-5'),
        ('ACC', 'Accra', 'Ghana', 'UTC+0'),
        ('IAD', 'Washington', 'United States', 'UTC-5'),
        ('HKG', 'Hong Kong', 'Hong Kong', 'UTC+8'),
        ('SIN', 'Singapore', 'Singapore', 'UTC+8'),
        ('AUH', 'Abu Dhabi', 'United Arab Emirates', 'UTC+4'),
        ('PEK', 'Beijing', 'China', 'UTC+8'),
        ('ORD', 'Chicago', 'United States', 'UTC-6'),
        ('MIA', 'Miami', 'United States', 'UTC-5'),
        ('AMS', 'Amsterdam', 'Netherlands', 'UTC+1'),
        ('MAD', 'Madrid', 'Spain', 'UTC+1'),
        ('FCO', 'Rome', 'Italy', 'UTC+1'),
        ('IST', 'Istanbul', 'Turkey', 'UTC+3'),
        ('JNB', 'Johannesburg', 'South Africa', 'UTC+2'),
        ('GRU', 'Sao Paulo', 'Brazil', 'UTC-3')
    """)
              
    conn.commit()
    conn.close
