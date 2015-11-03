#Amdahl's Law, Processors and Assembly language#

Requirements of a processor
===========================
 - Fetch instruction
 - Interpret instruction
 - Fetch data
 - Process data
 - Write data

The registers in the processors perform two roles.
 - User-visible roles
Allows programmer to minimise the number of required references to main memory
by optimizing use of registers. 
 - Control and status registers
Used by the control unit to control operation of the processor and by privileged
OS programs to control execution of programs.

 Instruction Cycle
==================
The indirect phase. Instruction fetched into memory, has to be decoded. 

Machine Code
============

Amdahl's Law
============
Measures the increase in performance of a processor given multiple instructions.
Compares implementation of a particular program using one processor.
