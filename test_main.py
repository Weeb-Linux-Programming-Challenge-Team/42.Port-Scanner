#!/usr/bin/env python3
import main


class Test_main:
    def test_scan_port_range(self):
        assert type(main.scan_port_range("localhost", 20, 1025)) is list
