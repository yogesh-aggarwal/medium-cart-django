from sql_tools import sqlite


# PRODUCT
'''
# Connecting database
sqlite.connect("data/products.sqlite3")


commands = [
    """
    CREATE TABLE IF NOT EXISTS PRODUCT (
        id INT NOT NULL PRIMARY KEY,
        endId VARCHAR(70) NOT NULL UNIQUE,
        name TEXT,
        shortDesc TEXT,
        description TEXT,
        images TEXT,
        rating FLOAT,
        owners TEXT,
        categories TEXT,
        reviews TEXT,
        assets TEXT,
        quantity FLOAT,
        sale TEXT,
        price FLOAT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS OWNER (
        id INT NOT NULL PRIMARY KEY,
        username TEXT,
        name TEXT,
        email EMAIL,
        phone INT,
        otherNumber INT,
        storeId TEXT,
        storeName VARCHAR(18),
        storeStatus TEXT,
        passwordHash TEXT,
        joinDate DATE,
        leaveDate DATE
    );
    """
]

for command in commands:
    sqlite.execute(command)

commands = [
    """
    INSERT INTO PRODUCT VALUES (125785, "someHash125785", "Apple iPhone8", "Other than that, it’s an iPhone 8. You’ll get the exact same features and components as in other iPhone 8 models. The iPhone 8 is also available in gold, silver and (“space”) gray. Alas, there’s still no rose gold option", "Description: Other than that, it’s an iPhone 8. You’ll get the exact same features and components as in other iPhone 8 models. The iPhone 8 is also available in gold, silver and (“space”) gray. Alas, there’s still no rose gold option", "/static/products/product1.png", 5, "Apple Inc.", "Mobiles", 'This is a great device =+=+=@#$%^&*()=+=+= I love this device =+=+=@#$%^&*()=+=+= Looks are awesome', "", 568431, "false", 67,940),
                               (146842, "someHash146842", "Headphones", "Silver Kartz on being questioned “Are wired headphones safer than wireless”, our answer is yes. Even though, wireless headphones are harmful but with the intelligent use of smart wireless technology, its ill effects can be minimised, but not cued.", "When buying a headphone these days people typically debate the style of headphone they want (in-ear, on-ear, around-ear) whether to go wired or wireless (or even totally wireless) and whether to opt for such extra features as active noise-cancellation to help muffle ambient noise. Oh, and then there's price. Everybody has a budget. Silver Kartz presents you, the in budget wired headphones, with ear friendly cushioned earhead knobes, which will delight you while listening music and your important messages.", "/static/products/product1.png", 4.5, "Dragon Headphones", "Accessories", 'Awesome headphones =+=+=@#$%^&*()=+=+= Looks is very nice =+=+=@#$%^&*()=+=+= Audio quality is very nice', '', 4463258, "true", 3000)
    """
]

for command in commands:
    sqlite.execute(command)


# Disconnecting database
sqlite.constants.__databPath__ = []

'''

# USER DATA

# ================================================================================================================ #

# Connecting database
sqlite.connect("data/users.sqlite3")

commands = [
    """
    CREATE TABLE IF NOT EXISTS USER (
        id INT PRIMARY KEY NOT NULL,
        publicId TEXT UNIQUE NOT NULL,
        username VARCHAR(20) NOT NULL UNIQUE,
        firstName VARCHAR(30) NOT NULL,
        lastName VARCHAR(30) NOT NULL,
        password TEXT NUT NULL,
        accountStatus TEXT,
        staff VARCHAR(20),
        merchant VARCHAR(20),
        emailAddress EMAIL NOT NULL,
        phoneNumber INT,
        recieveNewsletter VARCHAR(20),
        recieveProductInfo VARCHAR(20),
        profileImage TEXT,
        region VARCHAR(40),
        joinedDate DATE,
        leaveDate DATE
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS USERDATA (
        id INT PRIMARY KEY,
        username VARCHAR(20) NOT NULL UNIQUE,
        password TEXT NOT NULL,
        emailAddress EMAIL NOT NULL,
        contactNumber INT,
        language VARCHAR(20),
        region VARCHAR(40),
        cartItems TEXT,
        history TEXT,
        orderStatus VARCHAR(40),
        helpRequests TEXT,
        lastActive TEXT,
        lastLogin TEXT
    );
    """
]

for command in commands:
    sqlite.execute(command)

sqlite.constants.__databPath__ = []
