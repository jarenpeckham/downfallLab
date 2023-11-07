section .data
    sse2_flag db 0

section .text
global main

main:
    ; Use CPUID to check for SSE2 support
    mov eax, 1         ; Set EAX to 1 for CPUID function 1
    cpuid              ; Execute CPUID instruction
    test edx, (1 << 26) ; Check if the bit 26 of EDX (SSE2 flag) is set
    jnz sse2_supported  ; Jump to label if SSE2 is supported

sse2_not_supported:
    ; SSE2 is not supported
    mov byte [sse2_flag], 0
    jmp exit_program

sse2_supported:
    ; SSE2 is supported
    mov byte [sse2_flag], 1

exit_program:
    ; Exit the program
    mov eax, 60         ; syscall number for exit
    xor edi, edi        ; status code 0
    syscall

