#Computer Architecture and Networks#
Computer Function and Interconnection
=====================================

###Section A###
1) The buses that connect different parts of the processor can be hierarchical
to improve the performance (**True**)  
2) Instead of hard-wiring units, software is used to interpret and execute
instructions in a general purpose system (**True**)  
3) The program counter stores the address of the next instruction to be executed
(**True**)  
4) The fetched instructions are stored in the Accumulator register (**False**)
5) Interrupts are part of the program that can cause the processor to stop
(**True**)  
6) All interrupts are handled by the interrupt handler (**True**)  
7) Multiple interrupts cannot be handled by the processor (**False**)  
8) I/O modules can have direct access to the memory (**True**)  
9) If a module needs to transmit data, the data is sent through the buses
immediately (**False**)
10) Data transfer between modules/units cannot be controlled (**False**)  
11) The PCI bus is used for high speed I/O transfers (**True**)  
12) Interrupt request is a PCI command (**False**)  

###Section B###

1) *How are data and instructions stored in the Von Neumann architecture?*  
Unified read-write memory

2) *Which are the main stages of an instruction cycle?*  
Fetch and execute cycle

3) *Where is the fetched instruction stored?*  
Instruction register

4) *Which of the following is a type of interrupt?*  
All (program interrupt, hardware/power failure, I/O interrupt)

5) *Which of the following approaches is used to handle multiple interrupts?*  
Disable interrupts and priority assignment

6) *Which of these interconnection wires is not in the bus structure?*  
Instruction lines

7) *Which of the following is a bus arbitration scheme?*  
All (Priority, round-robin, first come first serve)
#Computer Architecture and Networks#

Memory
======

###Section A###

1) The memory devices used in a computer form a hierarchy based on a set of
characteristics (**True**)  
2) The lowest level of memory in the hierarchy is the closest to the processor
(**False**)  
3) Semiconductor ROM memory is a non-erasable but volatile type of memory
(**False**)  
4) If the memory has a faster acces time, then the cost per bit is less
(**False**)  
5) A hit occures when the word requested can be accessed from the lowest memory
in the hierarchy (**False**)  
6) Data stored in the secondary auxiliary memory is represented in terms of
files or records (**True**)  
7) Direct mapping implies that the number of lines in the cache must be equal to
the main memory (**False**)  
8) The best among the three cache replacement algorithms is the least recently
used algorithm (**True**)  
9) Like the entire memory, the system can have multi-level caches (**True**)  
10) Static RAM is faster and denser memory than DRAM (**False**)  
11) The capability of being written into a stable state is one important poperty
of semiconductor memories (**True**)  
12) DRAM uses a set of transistors to store change (**False**)  
13) ROMs cannot be used even when only a few bits are corrupted (**True**)  
14) EPROMs and Flash memory use only a single transistor to store information in
each cell (**False**)  
15) Read-mostly memory is a type of RAM (**False**)  

###Section B###

1) *How is data stored in the internal memory?*  
Bytes or words

2) *Which among the following is not a method of accessing data?*  
Asynchronous

3) *The unit of transfer between the levels of memory is defined by?*  
Number of electric lines in and out of memory

4) *Performance of the memory is decided by which of the following parameters?*  
All (transfer rate, latency, cycle time)

5) *Victim caching helps what type of cache arcitecture?*  
Direct mapped

6) *Random cache line replacement policy performs close to which other policy?*  
All (LRU, LFU, FIFO)

7) *Split caches indicate separate:*  
Data and instruction cache

8) *Prefetching can be done only in what type of cache?*  
Split cache

9) *As you go down the hierarcy:*  
All(Latency increases, cost per bit reduces, capacity increases)

10) *An important attribute of RAM memories is:*  
Volatile

11) *Important difference between SRAM and DRAM?*  
Static/dynamic & no refresh for SRAM

12) *In a DRAM, the cell value is decided as 1 or 0, depending on the:*  
Transistor threshold voltage

13) *For how long does static RAM hold data?*  
For as long as power is supplied

14) *How often/how is data written into the ROM?*  
During manufacturing

15) *What happens when a bit of data is incorrect in a ROM?*  
ROM cannot be used

16) *From the following, which type of memory is not a read-mostly memory?*  
PROM
