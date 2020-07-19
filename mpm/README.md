# mpm 

Calculate the electromagnetic attenuation per frequency accordingly to ITU standard (annex 1). The ITU standard is included in the repo (R-REC-P.676-11-201609.pdf).

This project was initialized with the intention of studing the argp (GNU argument handling library included in gstdlib).

## Compile
To compile use
```
gcc -lm -o mpm mpm.c
```

## TODO List (What I'm planning to do):
- Error handling
- Organize project structure
- Organize options handling
- Re-style code with kernel styling rules
- Split equations to made them readible
- Multiple argument options: utilization of multiple water density option for example.
- Utilization of files for oxygen/water attenuation tables
- Put frequency handling (start/stop/samples) a option flags (args)

The todo list is a not exaustive one and todo entries are not shown in order of priority.

## TODO-priority (what I should be doing now):
- Configuration structure organization: It is set as typedef struct but I don't know if it is a good way of doing this, because the message passing to functions is not optimized.
