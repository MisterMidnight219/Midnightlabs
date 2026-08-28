# 🧠 MidnightLabs EnterpriseSim  
## EXP Entry 001: Domain Dawn — From VM Chaos to Order

> **Historical status:** Completed Foundation Era lab, May 2025  
> **Environment:** Isolated VirtualBox training network  
> **Security note:** Screenshots may show disposable training credentials and private lab addressing. They are not operational credentials and must not be reused.

Welcome to the first entry of the **MidnightLabs Inc.** lab journal, where we brute-force enlightenment one experiment at a time. This log covers the early infrastructure grind: setting up our Active Directory domain, provisioning DHCP, configuring DNS, and onboarding our first digital employee — the one and only Mister Midnight.

---

## ☁️ Environment Overview

We spun up our playground in **VirtualBox**, assembling a ragtag crew of virtual machines to simulate a lightweight enterprise environment. Our main pieces:

- 1x Windows Server 2019 (Domain Controller)
- 1x Windows 10 Pro (Client1)
- 1x Kali Linux (prepared for later security exercises)
  
![VirtualBox Kali VM Settings](../screenshots/VirtualBox_KaliVM_Settings.png)

---

## 🏗️ Phase 1: Active Directory Setup

After installing the AD DS role, we created our internal training domain: `Midnightlab.local`.

![Server Manager Roles](../screenshots/ServerManager_AllRolesEnabled.png)

We created an **Organizational Unit (OU)** for Human Resources and introduced **Mister Midnight** as the first test user.

![Create HR User Mister Midnight](../screenshots/ActiveDirectory_HR_User_MisterMidnight.png)

We then attempted to automate user creation through PowerShell. The script collided with an OU that already existed:

![PowerShell Script Error](../screenshots/Powershell_AutoUserScriptError.png)

The useful lesson was larger than the error: automation must account for existing state. A repeatable provisioning script should check whether an object exists before attempting to create it.

---

## 📡 Phase 2: DHCP + DNS

Next came **DHCP configuration**, because typing addresses manually is a crime against sysadmins.

![DHCP Config Start](../screenshots/DHCP_Initial_Config.png)

We created a scope in the private `172.16.0.0/24` training range.

![DHCP Scope Tree](../screenshots/DHCP_Scope_Setup.png)

---

## 🖥️ Phase 3: Client Onboarding

With the core services running, we joined Client1 to the domain.

![Client1 Join Domain](../screenshots/Client1_DeviceSpecs_ADJoin.png)

A ping to the domain controller confirmed basic network reachability:

![CMD Ping Domain](../screenshots/CMD_PingDomainController.png)

---

## 🔍 Reflection

This first arc was about structure: establishing the domain skeleton that later experiments could extend, defend, or deliberately break. The most important outcome was not merely that the client joined. It was seeing how identity, addressing, name resolution, and automation depend on one another.

The original follow-on ideas included phishing simulation, SIEM monitoring, Group Policy enforcement, and controlled ransomware exercises. Those ideas are preserved as planned templates—not represented as completed drills.

---

## Evidence Inventory

All evidence used by this entry lives under [`/screenshots`](../screenshots/):

1. `VirtualBox_KaliVM_Settings.png`
2. `ServerManager_AllRolesEnabled.png`
3. `ActiveDirectory_HR_User_MisterMidnight.png`
4. `Powershell_AutoUserScriptError.png`
5. `DHCP_Initial_Config.png`
6. `DHCP_Scope_Setup.png`
7. `Client1_DeviceSpecs_ADJoin.png`
8. `CMD_PingDomainController.png`
