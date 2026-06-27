---
title: "Hardware Design"
code: "6CCE3HAD"
semester: "Spring 2026"
level: "Undergraduate"
description: "The module provides a foundational, ISA‑to‑hardware understanding that enables students to design and reason about basic processors, pipelines, and memory systems, and to clearly communicate hardware design decisions."

staff:
  - name: "Dr. Haiyu Mao"
    role: "Module Leader"
    # email: "haiyu.mao@kcl.ac.uk"
    url: "https://hybol1993.github.io/"
    # office: "Bush House, S2.07"
    # office_hours: "Tue 14:00–15:00 or by appointment"

  - name: "Zihao Pu"
    role: "Teaching Assistant"
    # email: ""
    url: "https://sail.kcl.ac.uk/people/"
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
# Aims

This module introduces hardware design from the Instruction Set Architecture (ISA) upward, connecting the programmer-visible machine model (instructions, registers, and memory abstraction) to the underlying hardware structures (datapath, control, pipelines, caches, and the memory hierarchy). Building on prior knowledge of combinational and sequential logic, you will learn how these components compose into a complete processor–memory system, and how to reason about correctness and performance using simple engineering models.

By the end of the module, you should be able to explain and trace basic processor microarchitectures, analyze pipelined execution, and evaluate memory-system trade-offs in caches and virtual memory.

## Learning Outcomes

On successful completion of this module, students will be able to:

### ISA and machine-level interface (conceptual)

1.Explain the role of an Instruction Set Architecture (ISA) as a contract between software and hardware.
2.Describe key ISA concepts at a high level (e.g., instruction classes, registers, load/store interface, control flow, memory addressing).

### Processor design and control

3.Construct and explain a single-cycle CPU datapath for a small instruction subset (ALU, load/store, branch).
4.Derive the control signals required to execute instructions (e.g., register write, ALU operation select, memory read/write, PC update).
5.Compare single-cycle vs multi-cycle processor organizations and reason about CPI and clock period trade-offs.

### Pipelining and performance

6.Explain a classic 5-stage pipeline and identify structural, data, and control hazards.
7.Apply basic hazard mitigation techniques (e.g., forwarding, stalling, basic branch handling) to predict pipeline behavior.
8.Use simple performance models (e.g., CPI, pipeline penalties) to assess design decisions.

### Memory hierarchy, virtual memory, and storage

9.Explain locality and analyze cache behavior using tag/index/offset, mapping, and policies.
10.Compute performance metrics such as AMAT and explain the impact of cache design parameters and miss behavior.
11.Describe the purpose and mechanics of virtual memory (paging, TLB, page faults) at a conceptual and practical level.
12.Explain (at a high level) how main memory (DRAM) and storage/I/O fit into the system, including the motivation for concepts like DMA and memory-mapped I/O.

### Professional/engineering skills

13.Communicate design reasoning clearly using block diagrams, timing sketches, and quantitative calculations.

---

# Lecture Schedule

| Week   | Topic                                                    | Slides                                                                                                                      | Tutorials                                                                                  |
| ------ | -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Week 1 | von Neumann Model & Instruction Set Architectures        | [Lecture 1](/assets/slides/spring2026-hardware-design/lecture/Lecture 1 - vonneumann-isa.pdf)                               | [Tutorial 1](/assets/slides/spring2026-hardware-design/tutorial/Tutorial%201%20Annotated.pdf) |
| Week 2 | Instruction Set Architectures II                         | [Lecture 2](/assets/slides/spring2026-hardware-design/lecture/Lecture 2 - instruction-set-architecture-ii.pdf)              | [Tutorial 2](/assets/slides/spring2026-hardware-design/tutorial/Tutorial%202.pdf)             |
| Week 3 | ISA, Microarchitecture, and Assembly                     | [Lecture 3](/assets/slides/spring2026-hardware-design/lecture/Lecture 3 - ISA-Microarchitecture-Assembly.pdf)               | [Tutorial 3](/assets/slides/spring2026-hardware-design/tutorial/Tutorial%203%20Answer.pdf)    |
| Week 4 | Single-Cycle Microarchitecture: build the whole CPU once | [Lecture 4](/assets/slides/spring2026-hardware-design/lecture/Lecture 4 - Single-Cycle-Microarchitecture.pdf)               | [Tutorial 4](/assets/slides/spring2026-hardware-design/tutorial/Tutorial%204%20Answer.pdf)    |
| Week 5 | Multi-Cycle Microarchitecture and Pipelining             | [Lecture 5](/assets/slides/spring2026-hardware-design/lecture/Lecture 5 - Mutli-Cycle-Microarchitecture-and-Pipelining.pdf) | [Tutorial 5](/assets/slides/spring2026-hardware-design/tutorial/Tutorial%205%20Answer.pdf)    |
| Week 6 | Pipelined Processor Design                               | [Lecture 6](/assets/slides/spring2026-hardware-design/lecture/Lecture 6 - Pipelining.pdf)                                   | [Tutorial 6](/assets/slides/spring2026-hardware-design/tutorial/Tutorial%206%20Answer.pdf)    |
| Week 7 | Memory                                                   | [Lecture 7](/assets/slides/spring2026-hardware-design/lecture/Lecture 7 - memory.pdf)                                       | [Tutorial 7](/assets/slides/spring2026-hardware-design/tutorial/Tutorial%207%20Answer.pdf)    |
| Week 8 | Cache                                                    | [Lecture 8](/assets/slides/spring2026-hardware-design/lecture/Lecture 8 - cache.pdf)                                        | [Tutorial 8](/assets/slides/spring2026-hardware-design/tutorial/Tutorial%208%20Answer.pdf)    |
| Week 9 | Cache II and Storage                                     | [Lecture 9](/assets/slides/spring2026-hardware-design/lecture/Lecture 9 - cache 2 and storage .pdf)                         | N/A                                                                                        |

---

# FPGA-based Lab

### RISKing 16: A 16-bit RISC CPU

Project Author: [Zihao Pu](https://sail.kcl.ac.uk/people/)

The RISKing16 is a custom 16-bit Reduced Instruction Set Computer (RISC) processor designed specifically for the HAD26 (Hardware Architecture and Design) course at King's College London. It serves as a pedagogical "playground," allowing students to transition from theoretical concepts to practical engineering by building a fully functional CPU from the ground up.

**Core Design Philosophy**

- Unlike complex industry standards like x86 or ARM, RISKing16 focuses on architectural clarity:
- 16-bit Architecture: Features a compact 16-bit datapath and instruction format, optimized for FPGA implementation (like the Basys3 board).
- Load-Store Architecture: Memory is accessed only via explicit LDR and STR instructions, simplifying the internal datapath.
- Full-Stack Development: Students don't just write Verilog; they develop the entire ecosystem, including the Instruction Set Architecture (ISA) and a custom Assembler.

**Modular Learning**: The project is structured to master individual components—such as the ALU, Register File, and Control Unit—before integrating them into a multi-cycle or pipelined processor.

**Supporting Materials**: You can use the slides as the instruction to build the RISking processor, while the task templates are the prepared Vivado projects to help you get started without spent too much time on managing Vivado. The default version for Vivado is [2025.2](https://www.amd.com/en/support/downloads/adaptive-socs-and-fpgas/development-tools/2025-2.html).


| Component | Weight | Details                         | Slides                                                                        | Template Project |
| --------- | ------ | ------------------------------- | ----------------------------------------------------------------------------- | ---------------- |
| Task 1    | 20%    | Building 16-bit ALU and Shifter | [Task 1 Slides](/assets/slides/spring2026-hardware-design/lab/CW%20Task%201.pdf) | [Task1_Temp](/assets/slides/spring2026-hardware-design/lab/Task1_Student_temp.zip)       |
| Task 2    | 20%    | Building CPU Datapath           | [Task 2 Slides](/assets/slides/spring2026-hardware-design/lab/CW%20Task%202.pdf) |[Task2_Temp](/assets/slides/spring2026-hardware-design/lab/Task2_Student_temp.zip)|
| Task 3    | 20%    | Building CPU FSM                | [Task 3 Slides](/assets/slides/spring2026-hardware-design/lab/CW%20Task%203.pdf) |[Task3_Temp](/assets/slides/spring2026-hardware-design/lab/Task3_Student_temp.zip)|
| Task 4    | 20%    | Supporting Memory               | [Task 4 Slides](/assets/slides/spring2026-hardware-design/lab/CW%20Task%204.pdf) |[Final_Temp](/assets/slides/spring2026-hardware-design/lab/Task_Final_Student_temp.zip)|
| Task 5    | 20%    | Supporting Branching and IO     | [Task 5 Slides](/assets/slides/spring2026-hardware-design/lab/CW%20Task%205.pdf) |This part should be built based on finished task 4|
| Bonus     | 20%    | Pipelining                      | No step-by-step instruction provided for bonus task |                  |

### Practical Skills

To complement the coursework project and facilitate practical FPGA experience, we have developed three introductory lab demonstrations.

| Component | Topic                                | Slides                                                              | Materials                                                                | Instructor         | Lab Video                                              |
| --------- | ------------------------------------ | ------------------------------------------------------------------- | ------------------------------------------------------------------------ | ------------------ | ------------------------------------------------------ |
| Lab 1     | Getting started with FPGA and VIVADO | [Lab 1](/assets/slides/spring2026-hardware-design/lab/Lab1%20Demo.pdf) | [Lab 1 Code](/assets/slides/spring2026-hardware-design/lab/Lab1%20Demo.zip) | Zihao Pu           | [Lab 1](https://youtu.be/4a6D7fwtctE?si=NV7YZWoOJYyxeGOi) |
| Lab 2     | FPGA Debugging: USING VIO AND ILA   | [Lab 2](/assets/slides/spring2026-hardware-design/lab/Lab2%20Demo.pdf) | NA                                                                       | Stefan Johannesson | [Lab 2](https://youtu.be/HB1yorOfAMc?si=WJUBYZgnefTBGNAs) |
| Lab 3     | Writing FSM using SystemVerilog      | [Lab 3](/assets/slides/spring2026-hardware-design/lab/Lab3%20Demo.pdf) | [Lab 3 Code](/assets/slides/spring2026-hardware-design/lab/Lab3_Demo.zip)   | Ali Alsarraf       | [Lab 3](https://youtu.be/hCTE4qvoWRk?si=5nXZ-25UH6331x1E) |

### Useful Tools

| Tool               | Description                                                    | Source                                                                                       |
| ------------------ | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Verilog Autograder | The online simulation platform for the project                 | [Verilog Autograder](https://had26lab.sail-research-group.com/)                                               |
| openFPGALoader     | Download bitstream to FPGA using any platform, including macOS | [openFPGALoader-Document](https://trabucayre.github.io/openFPGALoader/compatibility/board.html) |
| Icarus Verilog |An open source Verilog/System Verilog simulator. It is also the tool we use to build our online simulator| [Icarus Verilog](https://github.com/steveicarus/iverilog)|

### Prerequisites

- Basic programming experience (Python, Verilog)
- Boolean algebra (covered in LOD Logic Design)

---

# Resources

- Recommended text: *Digital Design and Computer Architecture* — Harris & Harris
- Lab recordings:

<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?si=0y5L76wey1tG5l5z&list=PLSxjD_JEbzkwLRZu8DoWHlJN2zbyclPGS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

- Tutorial recordings:

<iframe src='https://www.kaltura.com/p/2368101/embedPlaykitJs/uiconf_id/50869822?iframeembed=true&playlist_id=1_eamm1qut&config[provider]={"widgetId":"1_dnptajz7"}' style='width: 740px;height: 330px' allowfullscreen webkitallowfullscreen mozAllowFullScreen allow='autoplay *; fullscreen *; encrypted-media *' sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder='0' title='' ></iframe>
