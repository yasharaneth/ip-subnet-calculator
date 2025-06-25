# IP Subnet Calculator 

A Python script to calculate IPv4 subnets for both **classful (A/B/C)** and **classless (CIDR)** addressing schemes.


---

#Features
- **Classful Subnetting**: Supports Class A, B, and C IP ranges
- **Classless (CIDR) Subnetting**: Handles custom prefix lengths (e.g., `192.168.1.0/24`)
- **Comprehensive Output**:
  - Network and broadcast addresses for each subnet
  - Subnet masks in dotted-decimal notation
  - Number of hosts per subnet
- **Input Validation**: Ensures proper IPv4 format and range checking
- **User-Friendly Interface**: Clear prompts and formatted output tables

---

🛠️ Usage
Classful Subnetting Example
```
Enter IP address: 192.168.1.0
Enter required number of subnets: 4

Subnet  Network Address    Broadcast IP
[1]     192.168.1.0        192.168.1.63
[2]     192.168.1.64       192.168.1.127
[3]     192.168.1.128      192.168.1.191
[4]     192.168.1.192      192.168.1.255

Subnet Mask: 255.255.255.192

Classless (CIDR) Subnetting Example

Enter IP address: 10.0.0.0/16
Enter required number of subnets: 2
Number of hosts for subnet 1: 100
Number of hosts for subnet 2: 50

-----------------------------------------------------------
| NOH  | Network IP       | Broadcast IP    | Subnet Mask    |
-----------------------------------------------------------
| 128  | 10.0.0.0/25      | 10.0.0.127/25   | 255.255.255.128 |
| 64   | 10.0.0.128/26    | 10.0.0.191/26   | 255.255.255.192 |
-----------------------------------------------------------
```

❓ Support
For help or questions:

contact

Email: nethsarayashara@gmail.com

## 📜 License
This project is released into the **public domain**.  
You may use, modify, and distribute this code for any purpose without restriction.

Created with ❤️ by yashara nethsara
