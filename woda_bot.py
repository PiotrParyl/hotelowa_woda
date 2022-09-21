from pymodbus.client.sync import ModbusTcpClient
from time import sleep, time
import datetime
import mysql.connector

#========================= db.connection #=========================

db = mysql.connector.connect(
    host="127.0.0.1",
    user="maczo420all",
    passwd="Pomidor13",
    database="metryka",
)

mycursor = db.cursor()

from time import sleep, time

while True:
    client = ModbusTcpClient(host= '192.168.1.243', port=502)
    client.connect()

    rr  = client.read_holding_registers(30,4)

    client.close()

    a = rr.registers[-1]
    b = rr.registers[-2]

   

    def water_calculation (a,b):

    
        bin_a = bin(a)
        bin_b = bin(b)

        bin_a_list = list(bin_a)
        bin_b_list = list(bin_b)

        del bin_a_list[:2]
        del bin_b_list[:2]

        joined_a = "".join(bin_a_list)
        joined_b = "".join(bin_b_list)

        x = joined_b + joined_a

        x_str =  joined_b + "0000" + joined_a

        x_int = int(x_str,2)
        e = datetime.datetime.now()
        if x_int <= 1_000_000:

            mycursor.execute(f"INSERT INTO woda (value) VALUES({x_int})")
            db.commit()
        else:
            bin_a = bin(a)
            bin_b = bin(b)

            bin_a_list = list(bin_a)
            bin_b_list = list(bin_b)

            del bin_a_list[:2]
            del bin_b_list[:2]

            joined_a = "".join(bin_a_list)
            joined_b = "".join(bin_b_list)

            x = joined_b + joined_a

            x_str =  joined_b + "000" + joined_a

            x_int = int(x_str,2)
            e = datetime.datetime.now()

            if x_int <= 1_000_000:
                mycursor.execute(f"INSERT INTO woda (value) VALUES({x_int})")
                db.commit()
            else:
                bin_a = bin(a)
                bin_b = bin(b)

                bin_a_list = list(bin_a)
                bin_b_list = list(bin_b)

                del bin_a_list[:2]
                del bin_b_list[:2]

                joined_a = "".join(bin_a_list)
                joined_b = "".join(bin_b_list)

                x = joined_b + joined_a

                x_str =  joined_b + "00000" + joined_a

                x_int = int(x_str,2)
                e = datetime.datetime.now()

                if x_int <= 1_000_000:
                    mycursor.execute(f"INSERT INTO woda (value) VALUES({x_int})")
                    db.commit()
                else:
                    bin_a = bin(a)
                    bin_b = bin(b)

                    bin_a_list = list(bin_a)
                    bin_b_list = list(bin_b)

                    del bin_a_list[:2]
                    del bin_b_list[:2]

                    joined_a = "".join(bin_a_list)
                    joined_b = "".join(bin_b_list)

                    x = joined_b + joined_a

                    x_str =  joined_b + "00" + joined_a

                    x_int = int(x_str,2)
                    
                    if x_int <= 1_000_000:
                        mycursor.execute(f"INSERT INTO woda (value) VALUES({x_int})")
                        db.commit()
                    else:
                        bin_a = bin(a)
                        bin_b = bin(b)

                        bin_a_list = list(bin_a)
                        bin_b_list = list(bin_b)

                        del bin_a_list[:2]
                        del bin_b_list[:2]

                        joined_a = "".join(bin_a_list)
                        joined_b = "".join(bin_b_list)

                        x = joined_b + joined_a

                        x_str =  joined_b + "0" + joined_a

                        x_int = int(x_str,2)

                        if x_int <= 1_000_000:
                            mycursor.execute(f"INSERT INTO woda (value) VALUES({x_int})")
                            db.commit()
                        else:
                            print ('frajer')






    water_calculation(a,b)

    sleep(300)
