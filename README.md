# xn-reverser
Enumerate possible ASCII text being spoofed by a particular IDN domain name

#### How it works
The basic algorithm for how this library works is as follows:

 - Convert raw `xn--` IDN domain to Unicode representation (using `idna` library)
 - For each Unicode char in the domain:
  - Check a pre-built mapping for possible ASCII characters that look similar to the Unicode character
  (i.e. plaintext ASCII characters that the Unicode character could be spoofing)
 - Compute the [Cartesian product](https://en.wikipedia.org/wiki/Cartesian_product) of the character lists (using `itertools.product`) to generate the possible plaintext domain names

#### Usage
```python
import xn_reverser

result = xn_reverser.xn_reverser("xn--80ak6aa92e.com")
print(result["possible_spoofed_ascii"])
```

xn_reverser() returns a dict containing the following elements:
 - `domain_raw` (string): the actual `xn--` raw IDN domain provided as the input
 - `domain_idn_rendered` (string): the rendered Unicode form of the IDN domain
 - `possible_spoofed_ascii` (list): a list of possible ASCII domains converted from the IDN form

#### Caveats
 - Does not parse subdomains. Must provide a base domain
