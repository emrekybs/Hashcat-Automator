import os
banner="""
╦ ╦╔═╗╔═╗╦ ╦╔═╗╔═╗╔╦╗  
╠═╣╠═╣╚═╗╠═╣║  ╠═╣ ║  
╩ ╩╩ ╩╚═╝╩ ╩╚═╝╩ ╩ ╩ 
𝑇ℎ𝑖𝑠 𝑝𝑦𝑡ℎ𝑜𝑛 𝑠𝑐𝑟𝑖𝑝𝑡 𝑤𝑎𝑠 𝑐𝑟𝑒𝑎𝑡𝑒𝑑 𝑡𝑜 𝑠𝑝𝑒𝑒𝑑 𝑢𝑝 𝑡ℎ𝑒 𝑚𝑜𝑠𝑡 𝑢𝑠𝑒𝑑 ℎ𝑎𝑠ℎ 𝑎𝑡𝑡𝑎𝑐𝑘𝑠 𝑤𝑖𝑡ℎ 𝐻𝑎𝑠ℎ𝑐𝑎𝑡.

							𝑩𝒚 𝑬𝒎𝒓𝒆 𝑲𝒚𝒃𝒔
"""
print(banner)
print("""							
							         							
- [ Hash modes ] -

 #   | Name                                           | Category
=====+================================================+======================================						    
5600 | NetNTLMv2 				      | Network Protocols						
1000 | NTLM 					      | Operating System							
2100 | Domain Cached Credentials 2 (DCC2), MS Cache 2 | Operating System		
1800 | sha512crypt $6$, SHA512 (Unix)  		      | Operating System				
7400 | sha256crypt $5$, SHA256 (Unix) 		      | Operating System				
500  | md5crypt, MD5 (Unix), Cisco-IOS $1$ (MD5)      | Operating System		
0    | MD5                                            | Raw Hash
1400 | SHA2-256                                       | Raw Hash
1700 | SHA2-512                                       | Raw Hash

8- 𝐇𝐚𝐬𝐡𝐈𝐃 
9- 𝐇𝐚𝐬𝐡-𝐈𝐝𝐞𝐧𝐭𝐢𝐟𝐢𝐞𝐫
""")
hash = input("Select the id number of the process you want to use: ")

if (hash=="5600"):
	os.system("clear")
	hashfile5600 = input("Input Path of Hash File :")
	dict5600 = input("Input Path of Wordlist File :")
	os.system("clear && hashcat -m 5600 -a 0 "+hashfile5600+" "+dict5600+" --status --force --potfile-disable")

if (hash=="1000"):
        os.system("clear")
        hashfile1000 = input("Input Path of Hash File :")
        dict1000 = input("Input Path of Wordlist File :")
        os.system("clear && hashcat -m 1000 -a 0 "+hashfile1000+" "+dict1000+" --status --force --potfile-disable")

if (hash=="2100"):
        os.system("clear")
        hashfile2100 = input("Input Path of Hash File  :")
        dict2100 = input("Input Path of Wordlist File  :")
        os.system("clear && hashcat -m 2100 -a 0 "+hashfile2100+" "+dict2100+" --status --force --potfile-disable")


if (hash=="1800"):
        os.system("clear")
        hashfile1800 = input("Input Path of Hash File  :")
        dict1800 = input("Input Path of Wordlist File  :")
        os.system("clear && hashcat -m 1800 -a 0 "+hashfile1800+" "+dict1800+" --status --force --potfile-disable")
        

if (hash=="7400"):
        os.system("clear")
        hashfile7400 = input("Input Path of Hash File :")
        dict7400 = input("Input Path of Wordlist File :")
        os.system("clear && hashcat -m 7400 -a 0 "+hashfile7400+" "+dict7400+" --status --force --portfile-disable")

if (hash=="500"):
        os.system("clear")
        hashfile500 = input("Input Path of Hash File  :")
        dict500 = input("Input Path of Wordlist File  :")
        os.system("clear && hashcat -m 500 -a 0 "+hashfile500+" "+dict500+" --status --force --potfile-disable")

if (hash=="0"):
        os.system("clear")
        hashfile0 = input("Input Path of Hash File :")
        dict0 = input("Input Path of Hash File :")
        os.system("clear && hashcat -m 0 -a 0 "+hashfile0+" "+dict0+" --status --force --potfile-disable")

if (hash=="1400"):
        os.system("clear")
        hashfile1400 = input("Input Path of Hash File  :")
        dict1400 = input("Input Path of Wordlist File  :")
        os.system("clear && hashcat -m 1400 -a 0 "+hashfile1400+" "+dict1400+" --status --force --potfile-disable")

if (hash=="1700"):
        os.system("clear")
        hashfile1700 = input("Input Path of Hash File  :")
        dict1700 = input("Input Path of Wordlist File  :")
        os.system("clear && hashcat -m 1700 -a 0  "+hashfile1700+" "+dict1700+" --status --force --potfile-disable")
        
if (hash=="8"):
        try:
                os.system("apt-get install hashid && clear")
                hashtype = input("Input Hash :")
                os.system("clear && hashid "+hashtype)
        except:
                os.system("sudo pacman -S hashid && clear")
                hashtype = input("Input Hash :")
                os.system("clear && hashid "+hashtype)

if (hash=="9"):
        try:
                os.system("apt-get install hash-identifier && clear")
                hashtype2 = input("Input Hash :")
                os.system("clear && hash-identifier "+hashtype2)
        except:
                os.system("sudo pacman -S hash-identifier && clear")
                hashtype2 = input("Input Hash :")
                os.system("clear && hash-identifier "+hashtype2)
