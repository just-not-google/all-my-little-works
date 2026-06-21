MIN_LENGTH_PASS = 5
MAX_LENGTH_PASS = 1000
DEFAULT_OPTION = 0
MIN_LENGTH_PINCODE = 3
MAX_LENGTH_PINCODE = 12

NAMES_FILES = ["files/000webhost.txt", "files/10_million_password_list_top_1000000.txt",
               "files/Ashley_Madison.txt", "files/rockyou-75.txt", "files/myspace-withcount.txt",
               "files/darkc0de.txt", "files/honeynet-nocount.txt"]

fuck_pass_art = """
███████╗██╗   ██╗ ██████╗██╗  ██╗    ██████╗  █████╗ ███████╗███████╗
██╔════╝██║   ██║██╔════╝██║ ██╔╝    ██╔══██╗██╔══██╗██╔════╝██╔════╝
█████╗  ██║   ██║██║     █████╔╝     ██████╔╝███████║███████╗███████╗
██╔══╝  ██║   ██║██║     ██╔═██╗     ██╔═══╝ ██╔══██║╚════██║╚════██║
██║     ╚██████╔╝╚██████╗██║  ██╗    ██║     ██║  ██║███████║███████║
╚═╝      ╚═════╝  ╚═════╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
"""

common_password_bases = [
    "password", "123456", "12345678", "qwerty", "abc123", "111111", "123123", "admin", "letmein", "welcome",
    "monkey", "jesus", "sunshine", "princess", "flower", "superman", "iloveyou", "love", "baby", "angel",
    "sweet", "honey", "fuck", "shit", "bitch", "asshole", "sex", "god", "fuckyou", "ninja",
    "master", "dragon", "baseball", "football", "soccer", "basketball", "hockey", "michael", "jennifer", "jordan",
    "hunter", "buster", "thomas", "robert", "matthew", "daniel", "andrew", "joshua", "ashley", "michelle",
    "tigger", "summer", "winter", "spring", "autumn", "maggie", "ginger", "shadow", "mustang", "bailey",
    "harley", "ranger", "batman", "trustno1", "whatever", "freedom", "solo", "starwars", "hello", "abc123",
    "qazwsx", "zaq1zaq1", "qweasd", "admin123", "pass123", "password1", "123qwe", "1q2w3e", "1qaz2wsx", "qwerty123",
    "123456789", "987654321", "000000", "11111111", "222222", "333333", "444444", "555555", "666666", "777777",
    "888888", "999999", "aaaaaa", "zzzzzz", "xxxxxx", "yyyyyy", "p@ssw0rd", "passw0rd", "password123", "adminadmin",
    "changeme", "secret", "test", "test123", "demo", "guest", "user", "root", "toor", "12345",
    "1234567", "1234567890", "0987654321", "112233", "445566", "778899", "121212", "696969", "420420", "liverpool",
    "chelsea", "arsenal", "manutd", "barcelona", "realmadrid", "messi", "ronaldo", "neymar", "halamadrid", "qwertyuiop",
    "asdfghjkl", "zxcvbnm", "poiuytrewq", "mnbvcxz", "qazwsxedc", "1qazxsw2", "3edc4rfv", "a1b2c3d4", "iloveyou1", "fuckyou1",
    "monkey1", "dragon1", "master1", "ninja1", "sunshine1", "princess1", "flower1", "superman1", "batman1", "shadow1",
    "mustang1", "harley1", "ranger1", "thunder1", "tigger1", "summer1", "winter1", "maggie1", "ginger1", "bailey1",
    "charlie", "samantha", "jessica", "nicole", "amanda", "brandon", "steven", "jonathan", "justin", "ryan",
    "1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999",
    "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009",
    "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019",
    "2020", "2021", "2022", "2023", "2024", "2025", "1985", "1986", "1987", "1988",
    "alex", "maria", "david", "sara", "kevin", "laura", "chris", "anna", "peter", "lisa",
    "john", "mary", "james", "emma", "olivia", "sophia", "isabella", "mia", "ava", "charlotte",
    "london", "paris", "newyork", "berlin", "moscow", "tokyo", "sydney", "dubai", "rome", "madrid",
    "cat", "dog", "bird", "fish", "lion", "tiger", "bear", "wolf", "fox", "horse",
    "red", "blue", "green", "black", "white", "purple", "yellow", "orange", "pink", "brown",
    "money", "work", "home", "life", "happy", "friend", "family", "forever", "best", "cool",
    "apple", "banana", "orange", "grape", "lemon", "coffee", "tea", "pizza", "burger", "sushi",
    "spider", "butterfly", "unicorn", "dragonball", "naruto", "pokemon", "minecraft", "fortnite", "gta", "callofduty",
    "matrix", "internet", "wifi", "bluetooth", "google", "facebook", "instagram", "twitter", "youtube", "tiktok",
    "iphone", "samsung", "android", "windows", "linux", "macbook", "playstation", "xbox", "nintendo", "sony",
    "qwer1234", "asdf1234", "zxcv1234", "qwertyuiop123", "asdfghjkl123", "zxcvbnm123", "password!", "Password1", "Admin123", "Welcome1",
    "summer2023", "winter2024", "spring2025", "autumn2024", "january", "february", "march", "april", "may", "june",
    "july", "august", "september", "october", "november", "december", "birthday", "anniversary", "wedding", "vacation",
    "travel", "beach", "mountain", "forest", "river", "ocean", "sky", "star", "moon", "sun",
    "heart", "kiss", "hug", "smile", "laugh", "dream", "hope", "faith", "peace", "power",
    "king", "queen", "prince", "princess", "knight", "warrior", "hero", "legend", "champion", "winner",
    "loser", "game", "play", "win", "score", "goal", "team", "sport", "music", "dance",
    "party", "fun", "crazy", "wild", "free", "live", "die", "death", "hell", "heaven",
    "devil", "angel1", "demon", "ghost", "zombie", "vampire", "werewolf", "magic", "wizard", "witch",
    "fire", "ice", "water", "earth", "wind", "storm", "thunder", "lightning", "rain", "snow",
    "hot", "cold", "warm", "cool", "dark", "light", "day", "night", "morning", "evening",
    "good", "bad", "nice", "beautiful", "pretty", "handsome", "strong", "weak", "smart", "stupid",
    "rich", "poor", "famous", "unknown", "love123", "hate123", "sex123", "fuck123", "shit123", "bitch123",
    "admin2023", "admin2024", "admin2025", "user123", "guest123", "testtest", "qwert", "poiuyt", "lkjhgfdsa", "mnbvcxz1",
    "1q2w3e4r", "q1w2e3r4", "a1s2d3f4", "z1x2c3v4", "098765", "543210", "13579", "24680", "102030", "405060",
    "iloveyou2", "fuckoff", "getout", "goaway", "byebye", "hello123", "hi123", "hey123", "sup123", "yo123",
    "babe", "darling", "dear", "sweetheart", "cutie", "sexy", "hot123", "cute123", "beautiful1", "handsome1",
    "soccer1", "football1", "baseball1", "basketball1", "tennis1", "golf1", "hockey1", "volleyball1", "cricket1", "rugby1",
    "jordan23", "lebron", "curry", "kobe", "shaq", "messi10", "ronaldo7", "mbappe", "haaland", "benzema",
    "chelsea1", "liverpool1", "manchester", "arsenal1", "barca", "madrid1", "bayern", "juventus", "milan", "inter",
    "paris", "london1", "berlin1", "tokyo1", "dubai1", "miami", "vegas", "rio", "sao", "moscow1"
]