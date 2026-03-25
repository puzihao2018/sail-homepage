---
title: "Hardware Design"
code: "6CCE3HAD"
semester: "Spring 2026"
level: "Undergraduate"
description: "Introduces digital logic, combinational and sequential circuits, hardware description languages, and simple processor design."

staff:
  - name: "Dr. Haiyu Mao"
    role: "Module Leader"
    # email: "haiyu.mao@kcl.ac.uk"
    url: "https://hybol1993.github.io/"
    # office: "Bush House, S2.07"
    # office_hours: "Tue 14:00–15:00 or by appointment"

  - name: "Ali Alsarraf"
    role: "Teaching Assistant"
    # email: ""
    url: "https://sail.kcl.ac.uk/people/"
    # office: "Bush House, S2.07"
    # office_hours: "Tue 14:00–15:00 or by appointment"

  - name: "Stefan Johannesson"
    role: "Teaching Assistant"
    # email: ""
    # url: "https://sail.kcl.ac.uk/people/"
    # office: "Bush House, S2.07"
    # office_hours: "Tue 14:00–15:00 or by appointment"


  - name: "Zihao Pu"
    role: "Teaching Assistant"
    # email: ""
    url: "https://sail.kcl.ac.uk/people/"
    # office: "Bush House, S2.07"
    # office_hours: "Tue 14:00–15:00 or by appointment"


# schedule:
#   - week: 1
#     date: "2026-02-03"
#     topic: "Introduction & Motivation"
#     slides: ""
#     reading: ""
#   - week: 2
#     date: "2026-02-10"
#     topic: "Combinational Logic I: Gates & Boolean Algebra"
#     slides: ""
#     reading: ""
#   - week: 3
#     date: "2026-02-17"
#     topic: "Combinational Logic II: Karnaugh Maps & Minimisation"
#     slides: ""
#     reading: ""
#   - week: 4
#     date: "2026-02-24"
#     topic: "Sequential Logic I: Latches & Flip-Flops"
#     slides: ""
#     reading: ""
#   - week: 5
#     date: "2026-03-03"
#     topic: "Sequential Logic II: Finite State Machines"
#     slides: ""
#     reading: ""
#   - week: 6
#     date: "2026-03-10"
#     topic: "Hardware Description Languages (VHDL/Verilog)"
#     slides: ""
#     reading: ""
#   - week: 7
#     date: "2026-03-17"
#     topic: "Arithmetic Circuits: Adders & Multipliers"
#     slides: ""
#     reading: ""
#   - week: 8
#     date: "2026-03-24"
#     topic: "Memory: RAM, ROM, Registers"
#     slides: ""
#     reading: ""
#   - week: 9
#     date: "2026-03-31"
#     topic: "Programmable Logic: FPGAs & PLDs"
#     slides: ""
#     reading: ""
#   - week: 10
#     date: "2026-04-28"
#     topic: "Simple Processor Design I: Datapath"
#     slides: ""
#     reading: ""
#   - week: 11
#     date: "2026-05-05"
#     topic: "Simple Processor Design II: Control Unit"
#     slides: ""
#     reading: ""
#   - week: 12
#     date: "2026-05-12"
#     topic: "Revision & Exam Preparation"
#     slides: ""
#     reading: ""
---
## Schedule

| Week   | Topic                                                    | Slides                                                                                                                      |
| ------ | -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Week 1 | von Neumann Model & Instruction Set Architectures        | [Lecture 1](/assets/slides/spring2026-hardware-design/lecture/Lecture 1 - vonneumann-isa.pdf)                               |
| Week 2 | Instruction Set Architectures II                         | [Lecture 2](/assets/slides/spring2026-hardware-design/lecture/Lecture 2 - instruction-set-architecture-ii.pdf)              |
| Week 3 | ISA, Microarchitecture, and Assembly                     | [Lecture 3](/assets/slides/spring2026-hardware-design/lecture/Lecture 3 - ISA-Microarchitecture-Assembly.pdf)               |
| Week 4 | Single-Cycle Microarchitecture: build the whole CPU once | [Lecture 4](/assets/slides/spring2026-hardware-design/lecture/Lecture 4 - Single-Cycle-Microarchitecture.pdf)               |
| Week 5 | Multi-Cycle Microarchitecture and Pipelining             | [Lecture 5](/assets/slides/spring2026-hardware-design/lecture/Lecture 5 - Mutli-Cycle-Microarchitecture-and-Pipelining.pdf) |
| Week 6 | Pipelined Processor Design                               | [Lecture 6](/assets/slides/spring2026-hardware-design/lecture/Lecture 6 - Pipelining.pdf)                                   |
| Week 7 | Memory                                                   | [Lecture 7](/assets/slides/spring2026-hardware-design/lecture/Lecture 7 - memory.pdf)                                       |
| Week 8 | Cache                                                    | [Lecture 8](/assets/slides/spring2026-hardware-design/lecture/Lecture 8 - cache.pdf)                                        |
| Week 9 | Cache II and Storage                                     | [Lecture 9](/assets/slides/spring2026-hardware-design/lecture/Lecture 9 - cache 2 and storage .pdf)                         |

## Coursework Project

### RISKing 16: A 16-bit RISC CPU

The RISKing16 is a custom 16-bit Reduced Instruction Set Computer (RISC) processor designed specifically for the HAD26 (Hardware Architecture and Design) course at King's College London. It serves as a pedagogical "playground," allowing students to transition from theoretical concepts to practical engineering by building a fully functional CPU from the ground up.

**Core Design Philosophy**

- Unlike complex industry standards like x86 or ARM, RISKing16 focuses on architectural clarity:
- 16-bit Architecture: Features a compact 16-bit datapath and instruction format, optimized for FPGA implementation (like the Basys3 board).
- Load-Store Architecture: Memory is accessed only via explicit LDR and STR instructions, simplifying the internal datapath.
- Full-Stack Development: Students don't just write Verilog; they develop the entire ecosystem, including the Instruction Set Architecture (ISA) and a custom Assembler.

**Modular Learning**: The project is structured to master individual components—such as the ALU, Register File, and Control Unit—before integrating them into a multi-cycle or pipelined processor.

| Component | Weight | Details                         | Supporting Materials                                                                                        |
| --------- | ------ | ------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Task 1    | 20%    | Building 16-bit ALU and Shifter | [Task 1 Slides](/assets/slides/spring2026-hardware-design/lab/CW%20Task%201.pdf)                               |
| Task 2    | 20%    | Building CPU Datapath           | [Task 2 Slides](/assets/slides/spring2026-hardware-design/lab/CW%20Task%202.pdf)                               |
| Task 3    | 20%    | Building CPU FSM                | [Task 3 Slides](/assets/slides/spring2026-hardware-design/lab/CW%20Task%203.pdf)                               |
| Task 4    | 20%    | Supporting Memory               | [Task 4 Slides](/assets/slides/spring2026-hardware-design/lab/CW%20Task%204.pdf)                               |
| Task 5    | 20%    | Supporting Branching and IO     | [Task 4 Slides](/assets/slides/spring2026-hardware-design/lab/CW%20Task%204.pdf) Task 5 contents are also here |
| Bonus     | 20%    | Pipelining                      | NA                                                                                                          |

## Practical Skills

To complement the coursework project and facilitate practical FPGA experience, we have developed three introductory lab demonstrations.

| Component | Topic                                        | Slides                                                              | Supporting Materials                                                     | Instructor         |
| --------- | -------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------ | ------------------ |
| Lab 1     | Getting started with FPGA and VIVADO         | [Lab 1](/assets/slides/spring2026-hardware-design/lab/Lab1%20Demo.pdf) | [Lab 1 Code](/assets/slides/spring2026-hardware-design/lab/Lab1%20Demo.zip) | Zihao Pu           |
| Lab 2     | FPGA Debugging: USING VIO AND ILA IN VIVADO | [Lab 2](/assets/slides/spring2026-hardware-design/lab/Lab2%20Demo.pdf) | NA                                                                       | Stefan Johannesson |
| Lab 3     | Writing FSM using SystemVerilog              | [Lab 3](/assets/slides/spring2026-hardware-design/lab/Lab3%20Demo.pdf) | [Lab 3 Code](/assets/slides/spring2026-hardware-design/lab/Lab3_Demo.zip)   | Ali Alsarraf       |

## Useful Tools

| Tool               | Description                                                    | Source                                                                                       |
| ------------------ | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Verilog Autograder | The online simulation platform for the project                 | https://had26lab.zihaopu.cn                                                                  |
| openFPGAloader     | Download bitstream to FPGA using any platform, including macOS | [openFPGAloader-Document](https://trabucayre.github.io/openFPGALoader/compatibility/board.html) |

## Prerequisites

- Basic programming experience (Python, Verilog)
- Boolean algebra (covered in LOD Logic Design)

## Resources

- Recommended text: *Digital Design and Computer Architecture* — Harris & Harris (available in library)
- Lab recordings:

<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?si=0y5L76wey1tG5l5z&list=PLSxjD_JEbzkwLRZu8DoWHlJN2zbyclPGS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
