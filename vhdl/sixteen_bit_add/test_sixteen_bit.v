`timescale 1ns / 1ps
module stimulus;
    // Inputs
    reg [7:0] e1;
    reg [7:0] e2;
    reg cin;

    // Outputs
    wire [7:0] s;
    wire cout;

    // Instantiate the Unit Under Test (UUT)
    sixteen_bit_add uut (
        e1,
        e2,
        cin,
        s,
        cout
    );

    initial begin
        $dumpfile("test.vcd");
        $dumpvars(0,stimulus);
	
	e1 = 8'b00000000; e2 = 8'b00000000; cin = 0;
	#20 cin = 1;
	#20 e2 = 8'b00000001; cin = 0;
	#20 cin = 1;
	#20 e1 = 8'b00000001; e2 = 8'b00000000; cin = 0;
	#20 cin = 1;
	#20 e2 = 8'b11111111; cin = 0;
	#20 cin = 1;
	#20 e1 = 8'b11111111; e2 = 8'b00000001; cin = 0;
	#20 cin = 1;
	#40;
    end
       

    initial begin
        $monitor("t=%3d e1=%d e2=%d cin=%d => s=%d cout=%d",
                 $time, e1, e2, cin, s, cout);
    end
endmodule
