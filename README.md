# Home Telemety with Discord
==Project level 60%== Using Discrod we can esily check water consumption on each day, and check how much the heat pump has used the energy. Discord bot can also print chart show how much HP used energy in relation to the outdoor temperature  


-----------------------------------------------------------
## Table of contents
* [About Project](#about-project)
* [Measured Values](#measured-values)
* [Technologies](#technologies)
* [Scheme](#scheme)
* [Docker](#docker)
* [For code reviewer](#for-code-reviewer)

-----------------------------------------------------------
# About Project

The MyHome_Telemetry project is about how much my house use: 
* water (dm3) per 24h/7d/e.t.c
* energu (kWh) to heat water use heat pump

Tu trzeba coś dopisać i opisać dokończyć bla bla bla 

-----------------------------------------------------------
## Measured Values
* [Water](#water)
* [Heat Pump](#heat-pump)
* [Solaredge](#solaredge)

### Water
-----------------------------------------------------------

For wather measuring i use this water meter. Signal from register go to Anybus M-Bus/Modbus-TCP-Gateway by M-Bus where is convert to Modbus-TCP. From Anybus signal goes by to RasberyPi by TCP/IP protocol in LAN where bot (code in 'bots' file) written by me convert binary value to decimal value and send it to remote database every 5 min. 

-----------------------------------------------------------
![299819866_476893500568790_1032156745109520596_n](https://user-images.githubusercontent.com/44020188/185767357-36bae3b8-2d75-4846-8627-dfc2f47971b2.jpg)
![299748267_441129544697349_3292354809080360242_n](https://user-images.githubusercontent.com/44020188/185767350-104266fb-3bf5-45e2-9f71-47b57928bfff.jpg)
![300295083_596211648753536_1953649162381851983_n](https://user-images.githubusercontent.com/44020188/185767363-328519c8-a0f9-45a0-90e4-92e2b18389b7.jpg)


### Heat Pump 
-----------------------------------------------------------
In Heat Pump situation looks like this. The meter LE-03m is connecter to heat pump and measure how much HP consume energy. Then send singla use MODBUS by RS486  to converter which is connectet to RasberyPi where bot (code in 'bots' file) written by me conver input using this formula ( value = (r0 *(256*256) + r1 * 256 + r2)/10 ) to decimal number and send ist to remote database every 5 min .

Heat Pump also have more features. From HP signal by RS485 goes to 'black-box' and then goes to hub. Using RasberyPi we can read from HP values like: Temperature in boiler, temperature outside, temperature in/out and many many more (but right now i dont have idea/plan how to use this features :/)

LE-03M manual - https://www.fif.com.pl/pl/liczniki-zuzycia-energii-elektrycznej/339-licznik-zuzycia-energii-le-03m.html?fbclid=IwAR1bsHkWOV45t7rHKxRCWijoEu41s5mZq2mSojO2wou5koqmfIexHmO2TS0



-----------------------------------------------------------
![300527622_1450506268708443_1793216454363325692_n](https://user-images.githubusercontent.com/44020188/185767364-fde33aef-6c20-453e-b6d4-c1153b6e438e.jpg)
![299983697_3288583861412217_546950818204531387_n](https://user-images.githubusercontent.com/44020188/185767367-f9452846-3e50-463e-92bd-2198fca3bb31.jpg)
![299748267_441129544697349_3292354809080360242_n](https://user-images.githubusercontent.com/44020188/185767370-450c477b-0ed8-4d59-8b84-563cef1dd288.jpg)

## Technologies
-----------------------------------------------------------
Project is created with:
* Python version 3.12
* Flask\Django\FastAPI
* Modbus\M-Bus\Modbus-TCP

## Scheme
![image](https://user-images.githubusercontent.com/44020188/187191983-09bdd6a8-7a62-4bd9-ab2f-6382e4290327.png)


## Docker
-- Not Ready Yet --
