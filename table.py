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
        ('13312','QRS789','Yi-An Lin','Taiwan','F','1994-02-13','2021-04-01'),
        ('14336','TUV123','Amelia Earhart','United States','F','1987-07-24','2010-06-17'),
        ('15360','WXY456','Neil Armstrong','United States','M','1980-08-05','2005-03-15'),
        ('16384','ZAB789','Valentina Tereshkova','Russia','F','1982-03-06','2007-06-16'),
        ('17408','CDE123','Jean-Luc Picard','France','M','1985-07-13','2010-10-12'),
        ('18432','FGH456','Chuck Yeager','United States','M','1975-02-13','1998-09-12'),
        ('19456','IJK789','Jacqueline Cochran','United States','F','1981-05-11','2006-08-02'),
        ('20480','LMN123','Charles Lindbergh','United States','M','1982-02-04','2010-05-20'),
        ('21504','OPQ456','Buzz Aldrin','United States','M','1980-01-20','2007-06-05'),
        ('22528','RST789','Svetlana Savitskaya','Russia','F','1983-08-08','2011-07-25'),
        ('23552','UVW123','John Glenn','United States','M','1977-07-18','2002-02-20'),
        ('24576','XYZ456','Robert H. Lawrence Jr.','United States','NB','1985-10-02','2015-06-30'),
        ('25600','CBA123','Bessie Coleman','United States','F','1989-01-26','2010-06-15'),
        ('26624','FED456','Guion Bluford','United States','M','1979-11-22','2007-08-09'),
        ('27648','IHG789','Sergey Krikalev','Russia','M','1985-08-27','2010-12-01'),
        ('28672','LKJ123','Wang Yaping','China','NB','1990-01-27','2015-08-30')
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
        ('A380840','A380',853,'2012-08-23','2023-06-14'),
        ('A319012','A319',144,'2003-04-30','2023-05-25'),
        ('B757220','B757',200,'2009-01-19','2022-03-30'),
        ('B767300','B767',250,'2007-10-03','2023-09-12'),
        ('A350920','A350',369,'2019-07-12','2023-09-10'),
        ('B787803','B787',242,'2017-05-25','2023-07-20'),
        ('A220200','A220',135,'2021-06-01','2023-07-10'),
        ('B777302','B777',396,'2013-11-07','2023-09-29'),
        ('A380800','A380',853,'2012-08-23','2023-06-14'),
        ('A319002','A319',144,'2003-04-30','2023-05-25'),
        ('B757200','B757',200,'2009-01-19','2022-03-30'),
        ('B767330','B767',250,'2007-10-03','2023-09-12'),
        ('A350900','A350',369,'2019-07-12','2023-09-10'),
        ('B787800','B787',242,'2017-05-25','2023-07-20'),
        ('A340300','A340',280,'2005-03-17','2023-06-01'),
        ('B737900','B737',178,'2015-09-05','2023-09-08'),
        ('A320565','A320',194,'2020-11-01','2022-10-20'),
        ('B787100','B787',318,'2019-06-18','2023-07-30'),
        ('A321123','A321',206,'2020-03-10','2023-09-01'),
        ('A350100','A350',440,'2020-02-14','2023-08-25'),
        ('C919001','C919',158,'2023-01-16','2023-09-15')
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
        ('QF128','HKG','2023-12-04 20:05','SYD','2023-12-05 08:30','B787800','8192'),
        ('AF132', 'CDG', '2023-11-20 14:00', 'MEX', '2023-11-20 18:45', 'A350900', '10240'),
        ('LH456', 'FRA', '2023-12-01 09:30', 'LAX', '2023-12-01 12:45', 'A380800', '12288'),
        ('BA102', 'LHR', '2023-12-10 16:00', 'JNB', '2023-12-11 04:30', 'B777300', '6144'),
        ('DL123', 'ATL', '2023-12-15 22:10', 'CPT', '2023-12-16 12:45', 'A350900', '5120'),
        ('EK205', 'DXB', '2023-12-20 02:30', 'SFO', '2023-12-20 12:45', 'A380800', '4096'),
        ('SQ319', 'SIN', '2023-12-25 09:15', 'FCO', '2023-12-25 18:45', 'A350900', '10240'),
        ('CX890', 'HKG', '2023-11-18 21:45', 'JFK', '2023-11-18 23:45', 'B777300', '8192'),
        ('QR128', 'DOH', '2023-12-05 12:00', 'ORD', '2023-12-05 20:30', 'A350900', '6144'),
        ('AA84', 'MIA', '2023-12-09 07:00', 'GRU', '2023-12-09 14:45', 'B777300', '13312'),
        ('NZ123', 'AKL', '2023-12-03 16:30', 'LAX', '2023-12-03 09:00', 'B787900', '512'),
        ('QF138', 'SYD', '2023-11-22 08:00', 'LHR', '2023-11-22 18:00', 'B787800', '4096'),
        ('NZ456', 'AKL', '2023-12-05 14:00', 'SIN', '2023-12-05 20:00', 'B787900', '8192'),
        ('AF400', 'CDG', '2023-11-28 09:30', 'JNB', '2023-11-28 20:15', 'A350900', '12288'),
        ('BA345', 'LHR', '2023-12-18 07:45', 'AUH', '2023-12-18 18:10', 'A380800', '7168'),
        ('SQ281', 'SIN', '2023-12-10 01:30', 'AMS', '2023-12-10 08:00', 'A350900', '5120'),
        ('EK521', 'DXB', '2023-12-12 15:30', 'IST', '2023-12-12 20:30', 'A380800', '13312'),
        ('LH789', 'FRA', '2023-12-25 13:20', 'BKK', '2023-12-25 23:55', 'A330300', '3072'),
        ('CX856', 'HKG', '2023-12-01 08:10', 'SFO', '2023-12-01 23:45', 'B777300', '6144'),
        ('DL782', 'ATL', '2023-11-15 21:00', 'GRU', '2023-11-16 07:30', 'A330300', '5120'),
        ('AA241', 'ORD', '2023-11-30 11:00', 'FCO', '2023-11-30 21:00', 'B787900', '4096'),
        ('AF135', 'CDG', '2023-11-10 16:20', 'AMS', '2023-11-10 17:35', 'A319002', '6144'),
        ('NZ321', 'AKL', '2023-12-18 12:15', 'LAX', '2023-12-18 21:50', 'B787800', '9216'),
        ('QF721', 'SYD', '2023-12-28 19:40', 'PEK', '2023-12-29 05:10', 'B787900', '13312'),
        ('UA452', 'JFK', '2023-11-22 06:15', 'DXB', '2023-11-22 18:45', 'B777300', '8192'),
        ('EK843', 'DXB', '2023-11-27 20:00', 'JNB', '2023-11-28 04:35', 'A380800', '10240'),
        ('SQ892', 'SIN', '2023-12-22 02:45', 'NRT', '2023-12-22 08:00', 'A350900', '6144'),
        ('CX654', 'HKG', '2023-11-16 09:10', 'JFK', '2023-11-16 22:15', 'B777300', '7168'),
        ('BA203', 'LHR', '2023-12-09 11:45', 'MIA', '2023-12-09 19:45', 'A380800', '4096'),
        ('AA492', 'LAX', '2023-12-07 23:00', 'AKL', '2023-12-08 08:10', 'B787900', '10240'),
        ('EK220', 'DXB', '2023-11-29 23:45', 'SYD', '2023-11-30 09:20', 'A380800', '3072')
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
        ('GRU', 'Sao Paulo', 'Brazil', 'UTC-3'),
        ('MEX', 'Mexico City', 'Mexico', 'UTC-6'),
        ('BOM', 'Mumbai', 'India', 'UTC+5.5'),
        ('DEL', 'Delhi', 'India', 'UTC+5.5'),
        ('ICN', 'Seoul', 'South Korea', 'UTC+9'),
        ('KUL', 'Kuala Lumpur', 'Malaysia', 'UTC+8'),
        ('CPT', 'Cape Town', 'South Africa', 'UTC+2'),
        ('SCL', 'Santiago', 'Chile', 'UTC-3'),
        ('DUB', 'Dublin', 'Ireland', 'UTC+0'),
        ('ZRH', 'Zurich', 'Switzerland', 'UTC+1'),
        ('MUC', 'Munich', 'Germany', 'UTC+1'),
        ('BRU', 'Brussels', 'Belgium', 'UTC+1'),
        ('YVR', 'Vancouver', 'Canada', 'UTC-8'),
        ('YYZ', 'Toronto', 'Canada', 'UTC-5'),
        ('DME', 'Moscow', 'Russia', 'UTC+3'),
        ('LED', 'St. Petersburg', 'Russia', 'UTC+3'),
        ('DOH', 'Doha', 'Qatar', 'UTC+3'),
        ('SVO', 'Moscow', 'Russia', 'UTC+3'),
        ('LIS', 'Lisbon', 'Portugal', 'UTC+0'),
        ('HEL', 'Helsinki', 'Finland', 'UTC+2'),
        ('OSL', 'Oslo', 'Norway', 'UTC+1'),
        ('CPH', 'Copenhagen', 'Denmark', 'UTC+1'),
        ('ARN', 'Stockholm', 'Sweden', 'UTC+1')
    """)
              
    conn.commit()
    conn.close
