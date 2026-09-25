import sqlite3 as sq, os, uuid, hashlib
from time import sleep
from prettytable import *

def press_enter() :
    End_Press = input('\nPress enter: ')
    os.system('cls')

base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, 'data')
os.makedirs(data_dir, exist_ok=True)
db_path = os.path.join(data_dir, 'menager.db')

con = sq.connect(db_path)
cur = con.cursor()

Format_Table = PrettyTable()
Info_Table = PrettyTable()
Format_Traning = PrettyTable()
Pass_Error = PrettyTable()
Name_Error = PrettyTable()
error_320 = PrettyTable()
table_menu = PrettyTable()
table_traning = PrettyTable()
error_command = PrettyTable()
error_Name = PrettyTable()
error_Id = PrettyTable()
Name_Error_Found = PrettyTable()

Format_Table.title = 'Format Table'
Format_Traning.title = 'Format Training'
error_command.title = 'ERROR COMMAND'
error_Id.title = 'ERROR ID'
error_Name.title = 'ERROR FOUND NAME'
error_320.title = 'ERROR 320'
Name_Error.title = 'ERROR NAME'
Pass_Error.title = 'ERROR PASSWORD'
Name_Error_Found.title = 'ERROR NAME'
table_traning.title = 'Menu Traning'
table_menu.title = 'Menu'

error_command.header = False
error_Id.header = False
error_Name.header = False
error_320.header = False
Name_Error.header = False
Pass_Error.header = False
Name_Error_Found.header = False
Format_Table.header = False

Format_Table.add_row(['Id, Chapter Body, Height, Again, Count'])
error_command.add_row(['Uncorrect Command'])
Info_Table.add_row('Write chapter body for training\nor write 0 for exit\nor write info for check format Training\n')
error_Id.add_row(['Id Not Found '])
error_Name.add_row(['Name Not Found'])
Pass_Error.add_row(['min - 5 letters'])
Name_Error.add_row(['Write name with\nmin - 2 letters\nmax - 10 letters'])
error_320.add_row(['Write number'])
Name_Error_Found.add_row(['Uncorrect Name'])

table_traning.field_names = ['Numirates', 'command']
table_menu.field_names = ['Numirates', 'command']
Format_Traning.field_names = ['№', 'Explanation']

table_menu.add_rows(
    [
        [1, 'Create new account'],
        [2, 'Sign in'],
        [3, 'Exit'],
    ]
)

Format_Traning.add_rows(
    [
        [1, 'Chapter Body(Breast, Back, Shoulders, Hands, Legs, abs or abdominals'],
        [2, 'Height - format decimal number'],
        [3, 'Again - format integer number'],
        [4, 'Count - format integer number']
    ]
)

table_traning.add_rows(
    [
        [1, 'Create new training'],
        [2, 'Open all trainings'],
        [3, 'Delete Training'],
        [4, 'Exit']
    ]
)

cur.execute("""CREATE TABLE IF NOT EXISTS User_Account(
    Id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Pass TEXT NOT NULL,
    Salt TEXT NOT NULL
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS Traning_Table(
    Id INTEGER PRIMARY KEY,
    Id_User INTEGER NOT NULL,
    Chapter_Body TEXT NOT NULL,
    Height REAL NOT NULL,
    Again INTEGER DEFAULT 1,
    Count INTEGER DEFAULT 1,
    Id_Traning TEXT NOT NULL
)""")

while True:
    os.system('cls')
    print(table_menu)
    try:
        User_Menu = int(input('Choice: '))
    except ValueError:
        os.system('cls')
        print(error_320)
        press_enter()
        continue
    sleep(0.2)
    if User_Menu == 1:
        while True:
            os.system('cls')
            print('== Create new account ==')
            salt = str(uuid.uuid4())
            Name_Account = input('\nName: ').strip()
            cur.execute("SELECT Name FROM User_Account WHERE Name = ?", (Name_Account,))
            Check = cur.fetchall()
            if Check:
                os.system('cls')
                print('<< Name in database, write again >>')
                sleep(2.4)
                os.system('cls')
                continue
            if len(Name_Account) < 2 or len(Name_Account) > 10:
                os.system('cls')
                print(Name_Error)
                sleep(5)
                os.system('cls')
                continue
            Pass_Account = input('Pass: ')
            if len(Pass_Account) <= 4:
                os.system('cls')
                print(Pass_Error)
                sleep(2.8)
                os.system('cls')
                continue
            Hash_Pass = hashlib.sha512((Pass_Account + salt).encode()).hexdigest()
            cur.execute("INSERT INTO User_Account(Name, Pass, Salt) VALUES(?, ?, ?)", 
                       (Name_Account, Hash_Pass, salt))
            con.commit()
            os.system('cls')
            print('== Account created! ==')
            sleep(2.3)
            os.system('cls')
            break
    elif User_Menu == 2:
        Attempts = 0
        while Attempts <= 5:
            os.system('cls')
            print('= Sign in account =')
            Name_Sing_User = input('Name: ').strip()
            sleep(0.3)
            cur.execute("SELECT Name, Salt FROM User_Account WHERE Name = ?", (Name_Sing_User,))
            Check = cur.fetchone()
            if Check:
                Pass_Sing_User = input('Pass: ').strip()
                Hash_Pass = hashlib.sha512((Pass_Sing_User + Check[1]).encode()).hexdigest()
                cur.execute("SELECT Pass, Name FROM User_Account WHERE Name = ? AND Pass = ?", 
                           (Name_Sing_User, Hash_Pass))
                Check_Pass = cur.fetchone()
                if Check_Pass:
                    os.system('cls')
                    print('= Welcome! =')
                    sleep(1)
                    os.system('cls')
                    while True:
                        print(table_traning)
                        try:
                            Menu_Traning_Choise = int(input('Choice: '))
                        except ValueError:
                            os.system('cls')
                            print(error_320)
                            sleep(1)
                            press_enter()
                            continue
                        sleep(0.2)
                        os.system('cls')
                        if Menu_Traning_Choise == 1:
                            print(Format_Traning)
                            Chapter_Body = input('Write chapter body : ').strip()
                            sleep(0.3)
                            if Chapter_Body == '0':
                                os.system('cls')
                                continue
                            if Chapter_Body.capitalize() == 'Info':
                                os.system('cls')
                                Format_Traning
                                sleep(1)
                                press_enter()
                                continue
                            valid_chapters = ['Breast', 'Back', 'Shoulders', 'Hands', 'Legs', 'Abs', 'Abdominals']
                            if Chapter_Body.capitalize() not in valid_chapters:
                                os.system('cls')
                                print(error_command)
                                sleep(1)
                                press_enter()
                                continue
                            while True:
                                try:
                                    Height = float(input('Height: '))
                                    break
                                except ValueError:
                                    os.system('cls')
                                    print(error_320)
                                    sleep(1)
                                    press_enter()
                            while True:
                                try:
                                    Again = int(input('Again: '))
                                    break
                                except ValueError:
                                    os.system('cls')
                                    print(error_320)
                                    sleep(1)
                                    press_enter()
                            while True:
                                try:
                                    Count = int(input('Count: '))
                                    break
                                except ValueError:
                                    os.system('cls')
                                    print(error_320)
                                    press_enter()
                            cur.execute("SELECT Id FROM User_Account WHERE Name = ?", (Name_Sing_User,))
                            Check = cur.fetchone()
                            Check_end = Check[0]
                            Id_Traning = str(uuid.uuid4())
                            cur.execute("""
                                INSERT INTO Traning_Table (Id, Id_User, Chapter_Body, Height, Again, Count, Id_Traning)
                                VALUES (?, ?, ?, ?, ?, ?, ?)
                            """, (None, Check_end, Chapter_Body.capitalize(), Height, Again, Count, Id_Traning))
                            con.commit()
                            os.system('cls')
                            print('= Work created =')
                            sleep(1)
                            os.system('cls')
                        elif Menu_Traning_Choise == 2:
                            os.system('cls')
                            cur.execute("SELECT Id FROM User_Account WHERE Name = ?", (Name_Sing_User,))
                            Check = cur.fetchone()
                            Check_end = Check[0]
                            cur.execute("""
                                SELECT Id, Chapter_Body, Height, Again, Count 
                                FROM Traning_Table 
                                WHERE Id_User = ?
                            """, (Check_end,))
                            Check = cur.fetchall()
                            print(Format_Table)
                            for row in Check:
                                print(row)
                                sleep(0.2)
                            sleep(1)
                            press_enter()
                        elif Menu_Traning_Choise == 3:
                            os.system('cls')
                            print('== Delete Menu ==')
                            try:
                                Id_Delete_Traning = int(input('Write Id Training: '))
                            except ValueError:
                                os.system('cls')
                                print(error_320)
                                sleep(1)
                                press_enter()
                                continue
                            sleep(0.3)
                            cur.execute("SELECT Id Id_User FROM Traning_Table WHERE Id = ? AND Id_User = (SELECT Id FROM User_Account WHERE Name = ?)", (Id_Delete_Traning, Name_Sing_User))
                            Check = cur.fetchone()
                            if Check:
                                os.system('cls')
                                cur.execute("""
                                    DELETE FROM Traning_Table 
                                    WHERE Id = ? AND Id_User = (SELECT Id FROM User_Account WHERE Name = ?)
                                """, (Id_Delete_Traning, Name_Sing_User))
                                con.commit()
                                print('\n= Training Deleted =')
                                sleep(1)
                                press_enter()
                            else:
                                os.system('cls')
                                print(error_Id)
                                sleep(1)
                                press_enter()
                        elif Menu_Traning_Choise == 4:
                            Attempts = 6
                            sleep(0.5)
                            os.system('cls')
                            break
                        else:
                            os.system('cls')
                            print(error_command)
                            sleep(1)
                            press_enter()
                else:
                    os.system('cls')
                    Pass_Error.clear()
                    Pass_Error.add_row(['Uncorrect Pass'])
                    print(Pass_Error)
                    Attempts += 1
                    sleep(1)
                    press_enter()
            else:
                os.system('cls')
                print(Name_Error_Found)
                sleep(1)
                press_enter()
                Attempts += 1
    elif User_Menu == 3:
        os.system('cls')
        con.close()
        break
    else:
        os.system('cls')
        print(error_command)
        sleep(1)
        press_enter()