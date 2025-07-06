# 🧰 ko — Network Toolkit for Python & CLI

`ko` is a versatile Python library and command-line tool for performing network operations such as `ping`, `telnet`, `netcat`, `ssh`, `scp`, `nmap`, `zmq`, `mqtt`, `minio`, `s3`, and more. It is designed for both **educational purposes** and **practical usage**.

## 🎯 Purpose

Originally, `ko` was created as a **reference tool for learning network programming in Python** — offering simple, clear, and hackable implementations. Over time, it evolved into a **real CLI utility** and a **reusable Python library** for other applications.

---

## 🧩 Key Features

- ✨ **Command-line Interface (CLI)**:
```bash
  ko ping google.com
  ko telnet 127.0.0.1 8000
  ko ssh user@host
```

* 🐍 **Python Library**: Import and use directly in your code:

  ```python
  from ko.ping import ping
  result = ping("8.8.8.8", mode="mycode")
  ```

* ⚙️ **Three execution modes** for each tool:

  * `system`: Uses `subprocess` to call system-level commands.
  * `extlib`: Uses third-party libraries (e.g., `pythonping`, `telnetlib`, etc.).
  * `mycode`: Implements each tool from scratch using low-level Python for educational clarity and full control.

---

## 🧱 Built-in Tools

* `ping`
* `netcat`
* `telnet`
* `ssh`
* `scp`
* `nmap`

---

## 🔌 Plugin System

To keep the core lightweight and modular, advanced tools are separated into plugins:

* `ko-zmq`: ZeroMQ communication
* `ko-mqtt`: MQTT client/publisher
* `ko-minio`: MinIO/S3 support
* `ko-s3`: Simple S3 CLI integration
* `ko-http`: Basic HTTP client
* `ko-mitm`: Integrates `mitmproxy` for network debugging

Install plugins via pip:

```bash
pip install ko-zmq ko-mqtt ko-minio
```

---

## 🚀 Installation

```bash
pip install ko
```

Or install from source:

```bash
git clone https://github.com/konetkit/ko.git
cd ko
pip install -e .
```

---

## 💻 Example Usage

From the command line:

```bash
ko ping 8.8.8.8 --mode=mycode
ko telnet --mode=extlib 127.0.0.1 23
ko ssh user@192.168.1.100
```

In Python:

```python
from ko.ping import ping

ping("1.1.1.1", mode="extlib")
```

---

## 📚 What Can You Learn from `ko`?

* Understand how network protocols work (ICMP, TCP, SSH, etc.)
* Reimplement tools like `ping`, `telnet`, or `netcat` in pure Python
* Compare methods: system call vs. external lib vs. handwritten code
* Easily extend `ko` with custom plugins

---

## 📄 License

MIT License

---

## 🔗 Links

* Homepage: [github.com/konetkit/ko](https://github.com/konetkit/ko)
