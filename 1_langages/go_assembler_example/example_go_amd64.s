//go:build amd64

TEXT ·normalise(SB), $0-16
    MOVQ    data+0(FP), AX      // AX stores pointer to data
    MOVQ    n+8(FP), BX         // BX stores element count (n)

    CMPQ    BX, $0              // if n <= 0
    JLE     end                 // return immediately

    XORPD   X0, X0              // X0 = sum = 0.0
    MOVQ    AX, CX              // CX = reset pointer to start of data
    MOVQ    BX, DX              // DX = loop counter (i)

sum_loop:
    ADDSD   (CX), X0            // sum += *CX (value at pointer)
    ADDQ    $8, CX              // Move pointer to next float64 (8 bytes)
    DECQ    DX                  // i--
    JNZ     sum_loop            // if i != 0 goto sum_loop

    CVTSQ2SD BX, X1             // Convert n (int) to float64 in X1
    DIVSD   X1, X0              // X0 = sum / n (mean)

    MOVQ    AX, CX              // Reset pointer to start of data
    MOVQ    BX, DX              // Reset loop counter (i)

sub_loop:
    MOVSD   (CX), X1            // Load *CX into X1
    SUBSD   X0, X1              // X1 = X1 - mean
    MOVSD   X1, (CX)            // Store result back to *CX
    ADDQ    $8, CX              // Move pointer to next float64 (8 bytes)
    DECQ    DX                  // i--
    JNZ     sub_loop            // if i != 0 goto sub_loop

end:
    RET
