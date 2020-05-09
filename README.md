# What is this?

ula.py is an IPv6 ULA (Unique Local Address) Generator, which
generates a ULA according to the pseudo-random global ID algorithm
described in RFC 4193.

# Requires

netaddr https://pypi.org/project/netaddr/#files

# Usage

Generate a ULA with a specific MAC address.

```
$ python3 ula.py -m 22:33:44:55:66:77
fd2a:0c10:2b6d::/48
```

If the program is invoked without the option, the program obtains a
MAC address by using uuid.getnode().

```
$ python3 ula.py
fd2a:0c10:2b6d::/48
```

# License

Permission to use, copy, modify, and/or distribute this software for
any purpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL
WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE
AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL
DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR
PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
