from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

message = b'gAAAAABdFkosUAUoun2oUOgtm4PQbEDlBciqZVSBYeIFr3C3PQkmY5XMt7-e_LwqiB0Q9MWpZuD9DX2X0DV5rLVZ9bsJLfuhWV' \
          b'1Kok8SfHVYlzwgwyMyvCAXi7K4-SWZnXifCQ85d44HCnNi-u7yHT4dwptU7Xz_DOMu7RE7clYIbRdRx0JKJTE='


def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
