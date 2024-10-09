import sqlite3

def airline_table(c):
    conn = sqlite3.connect('airline_database.db')
    c = conn.cursor()

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
        ('256','ABC123','Kate Moss','UK','F','1988-01-16','2015-02-28'),
        ('512','DEF456','Michael Jackson','USA', 'M','1976-08-29','2002-07-11'),
        ('1024','GHI789','Usain Bolt', 'JAM','M','1986-08-21','2020-03-03'),
        ('2048','JKL123','Sully Sullenberger','USA','M','1951-01-23','1980-06-15'),
        ('3072','MNO456','Patty Wagstaff','USA','F','1951-09-11','1984-07-10'),
        ('4096','PQR789','Peggy Whitson','USA','F','1960-02-09','1986-06-08'),
        ('5120','STU123','Samantha Cristoforetti','ITA','F','1977-04-26','2001-11-15'),
        ('6144','VWX456','David Mackay','UK','M','1957-05-07','1994-02-15'),
        ('7168','YZA789','Eileen Collins','USA','F','1956-11-19','1990-05-04'),
        ('8192','BCD123','Yuri Malenchenko','RUS','M','1961-12-22','1988-01-01'),
        ('9216','EFG456','Koichi Wakata','JPN','M','1963-08-01','1992-10-12'),
        ('10240','HIJ789','Sunita Williams','USA','F','1965-09-19','1995-06-19'),
        ('11264','KLM123','Chris Hadfield','CAN','M','1959-08-29','1992-05-01'),
        ('12288','NOP456','Sally Wadsworth','AUS','F','1981-02-17','2008-04-09'),
        ('13312','QRS789','Nora Al Matrooshi','UAE','F','1993-05-01','2021-04-01')
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

    c.execute('''
      CREATE TABLE IF NOT EXISTS Flight(
        FlightID TEXT,
        DepartureCountry TEXT,
        DepartureCity TEXT,
        DepartureAirportCode TEXT,
        DepartureDateTime_Local DATETIME,
        DepartureTimeZone TEXT,
        ArrivalCountry TEXT,
        ArrivalCity TEXT,
        ArrivalAirportCode TEXT,
        ArrivalDateTime_Local DATETIME,
        ArrivalTimeZone TEXT,
        TotalFlightTime INTEGER,
        AircraftID TEXT, 
        PilotID TEXT,
        PRIMARY KEY (FlightID, PilotID),
        FOREIGN KEY(AircraftID) REFERENCES Aircraft(AircraftID),
        FOREIGN KEY(PilotID) REFERENCES Pilot(PilotID)
      )
    ''')

    c.execute("""
      INSERT OR IGNORE INTO Flight VALUES
        ('BA1499','UK','Glasgow','GLA','2023-11-03 11:45','UTC+0','UK','London','LHR','2023-11-03 13:10','UTC+0','01:25','A321003','256'),
        ('BA1499','UK','Glasgow','GLA','2023-11-03 11:45','UTC+0','UK','London','LHR','2023-11-03 13:10','UTC+0','01:25','A321003','512'),
        ('TG436','IDN','Jakarta','CGK','2023-11-05 19:05','UTC+7','THA','Bangkok','BKK','2023-11-05 22:35', 'UTC+7','3:30','B777002','512'),
        ('CX840','JPN','Tokyo','HND','2023-11-09 17:20','UTC+9','USA','NewYork','JFK','2023-11-09 19:05','UTC-5','15:45','A350006','256'),
        ('SQ52','SIN','Singapore','SIN','2023-12-01 08:30','UTC+8','USA','San Francisco','SFO','2023-12-01 19:10','UTC-8','16:40','B787900','7168'),
        ('EK203','UAE','Dubai','DXB','2023-12-03 02:30','UTC+4','USA','New York','JFK','2023-12-03 08:30','UTC-5','14:00','A380800','6144'),
        ('QF10','UK','London','LHR','2023-12-05 21:15','UTC+0','AUS','Sydney','SYD','2023-12-07 06:00','UTC+10','21:45','B787800','12288'),
        ('AF459','BRA','Rio de Janeiro','GIG','2023-11-25 16:55','UTC-3','FRA','Paris','CDG','2023-11-26 08:10','UTC+1','11:15','A350900','10240'),
        ('LH401','USA','New York','JFK','2023-11-18 16:00','UTC-5','GER','Frankfurt','FRA','2023-11-19 05:30','UTC+1','07:30','B747400','4096'),
        ('AA101','USA','Los Angeles','LAX','2023-11-15 13:45','UTC-8','UK','London','LHR','2023-11-16 07:00','UTC+0','10:15','B777300','5120'),
        ('JL34','JPN','Tokyo','NRT','2023-11-20 11:20','UTC+9','SIN','Singapore','SIN','2023-11-20 17:05','UTC+8','06:45','B767300','6144'),
        ('UA858','USA','San Francisco','SFO','2023-12-01 10:25','UTC-8','JPN','Tokyo','NRT','2023-12-02 14:45','UTC+9','11:20','B787900','4096'),
        ('EK412','UAE','Dubai','DXB','2023-12-08 10:15','UTC+4','AUS','Sydney','SYD','2023-12-09 07:00','UTC+10','13:45','A380800','7168'),
        ('NZ2','UK','London','LHR','2023-11-30 16:15','UTC+0','NZL','Auckland','AKL','2023-12-01 05:30','UTC+13','24:15','B787800','10240'),
        ('DL108','USA','Atlanta','ATL','2023-12-10 22:30','UTC-5','GER','Frankfurt','FRA','2023-12-11 12:30','UTC+1','08:00','A350006','11264'),
        ('BA75','UK','London','LHR','2023-12-02 12:50','UTC+0','GHA','Accra','ACC','2023-12-02 19:25','UTC+0','06:35','B777300','8192'),
        ('AF22','FRA','Paris','CDG','2023-12-07 13:40','UTC+1','USA','Washington','IAD','2023-12-07 16:10','UTC-5','08:30','A350900','6144'),
        ('CX880','HKG','Hong Kong','HKG','2023-12-03 23:45','UTC+8','USA','Los Angeles','LAX','2023-12-03 19:45','UTC-8','12:00','B777300','4096'),
        ('LH778','GER','Frankfurt','FRA','2023-11-29 22:15','UTC+1','SIN','Singapore','SIN','2023-11-30 17:50','UTC+8','12:35','A350900','12288'),
        ('QF128','HKG','Hong Kong','HKG','2023-12-04 20:05','UTC+8','AUS','Sydney','SYD','2023-12-05 08:30','UTC+10','09:25','B787800','8192')
    """)
