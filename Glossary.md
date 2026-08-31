# 📘 MidnightLabs Glossary

A quick-reference guide for common terms, commands, and metaphors used throughout the MidnightLabs project.

---

## 📚 Concepts

### **CLI (Command Line Interface)**
A text-based interface to interact directly with the operating system or device. Seen as the "ocean" in our metaphor—vast and flexible compared to GUI.

### **GUI (Graphical User Interface)**
A visual, point-and-click interface. Represented as a system of structured canals—easier to navigate but limited in scope.

### **SSH (Secure Shell)**
A secure protocol to remotely access a device’s CLI, usually over the internet. Acts like opening a wormhole into another machine’s command line.

### **IOS (Internetwork Operating System)**
Cisco’s proprietary OS used in network devices like switches and routers.

### **Packet Tracer**
A Cisco network simulation tool used to practice CLI commands and network topologies without needing physical equipment.

### **Console Access**
Direct physical access to a device’s terminal—like plugging in a hardline to a switch to begin configuration.

### **Context-Sensitive Help (`?`)**
A CLI tool that shows you what commands or options are valid at any point in a command.

### **Tab Completion**
Pressing `Tab` will auto-complete a command if the typed prefix is unique.

### **Command Shortening**
Typing only enough of a command to make it unambiguous (e.g., `conf t` for `configure terminal`).

---

## ⚙️ IOS Modes

| Mode                 | Description                                      |
|----------------------|--------------------------------------------------|
| **User EXEC**        | Basic mode with limited view commands (`S1>`)    |
| **Privileged EXEC**  | Elevated view permissions (`S1#`)                |
| **Global Config**    | System-wide changes (`S1(config)#`)              |
| **Interface Config** | Configuring specific ports/interfaces            |
| **Line Config**      | Configuring access lines (e.g., console, SSH)    |

---

## 🧠 Shortcuts (Hotkeys)

| Shortcut             | Purpose                                      |
|----------------------|----------------------------------------------|
| `Ctrl + A`           | Move to beginning of line                    |
| `Ctrl + E`           | Move to end of line                          |
| `Up / Down Arrows`   | Cycle through command history                |
| `Tab`                | Auto-complete command                        |
| `Ctrl + C`           | Abort command / exit mode                    |
| `Ctrl + Z`           | Exit to Privileged EXEC                      |
| `Ctrl + Shift + 6`   | Interrupt current command (e.g., stop ping)  |
| `Ctrl + R`           | Redraw interrupted line                      |

---

_This file will be updated as more concepts are introduced through MidnightLabs entries._
