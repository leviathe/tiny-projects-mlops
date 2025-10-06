`timescale 1ns / 1ps
module stimulus;
    // Inputs
    reg e1;
    reg e2;
    reg cin;

    // Outputs
    wire s;
    wire cout;

    // Instantiate the Unit Under Test (UUT)
    one_bit uut (
        e1,
        e2,
        cin,
        s,
        cout
    );

    initial begin
        $dumpfile("test.vcd");
        $dumpvars(0,stimulus);

        // Initialize Inputs
        e1 = 0; e2 = 0; cin = 0;
        #20 cin = 1;
        #20 e2 = 1; cin = 0;
        #20 cin = 1;
        #20 e1 = 1; e2 = 0; cin = 0;
        #20 cin = 1;
        #20 e2 = 1; cin = 0;
        #20 cin = 1;
        #40;
    end

    initial begin
        $monitor("t=%3d e1=%d e2=%d cin=%d => s=%d cout=%d",
                 $time, e1, e2, cin, s, cout);
    end
endmodule
