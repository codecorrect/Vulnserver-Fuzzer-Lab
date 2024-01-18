Final Project files for Cybersecurity Bootcamp. Ran against VulnServer running on a Windows server to find a buffer overflow in the VulnServer program. 

1_Fuzzer.py is used to send increasingly longer data til VulnServer crashes, that gives us the ballpark of the characters needed for the overflow. 
2_eip_hunter.py is used to send a nonrepeating string to the server to see what pattern is written into the EIP (in the debugger on the Windows Server). This will give us our buffer size.
3_shellcode.py is the final buffer overflow exploit. After the buffer is the memory address of a command in the VulnServer DLL that will redirect execution back into the current stack frame. Then it includes a NOP sled for variability of the Stack Pointer. Finally it executes a payload that generates a reverse TCP shell. 

For a detailed overview of this project, view the [Google Slides Presentation](https://docs.google.com/presentation/d/1-FVf3o4jOFlyRfadM31PTF1wuuZd_WjA8flF05g9hLs/edit?usp=sharing).

These are for study only, do not use on a system that you don't own or have permission to do this to. 

