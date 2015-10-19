#Function Units from Logic Gates#
Decoders
========
Manager call 7 assistants. 2 options:  
 a: Seven individual lines  

 b: Three lines used to indicate the number of the assistant. Suitable **decoding** logic is then required
 at the end of the 3 lines to pick out the correct assistant.

| A | B | C | Result |
|---|---|---|---|
| 0 | 0 | 0 | No call |
| 0 | 0 | 1 | First assistant |
| 0 | 1 | 0 | Second assistant |
| 1 | 0 | 0 | Third assistant |
| 0 | 1 | 1 | Fourth assistant | 
| 1 | 1 | 0 | Fifth assistant |
| 1 | 0 | 1 | Sixth assistant |
| 1 | 1 | 1 | Seventh assistant |

A functional unit commonly used either on its own or integrated into a much larger circuit would have all of the
decoders in the same block. For the above example, this would be a 3-to-8 line decoder. For larger numbers of selections
4-to-16 or 5-to-32 decoders could be used.

Encoders
========

Multiplexers
============

llows a number of signals to share a single line. Allows only one output at any given time.
