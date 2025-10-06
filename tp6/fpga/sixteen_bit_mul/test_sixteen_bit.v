`timescale 1ns / 1ps
module stimulus;
    reg [15:0] e1;
    reg [15:0] e2;

    wire [31:0] s;

    sixteen_bit_mul uut (
        e1,
        e2,
        s
    );

    initial begin
        $dumpfile("test.vcd");
        $dumpvars(0,stimulus);

        e1 = 16'd0;     e2 = 16'd0;    #20;
        e1 = 16'd1;     e2 = 16'd123;  #20;
        e1 = 16'd10;    e2 = 16'd25;   #20;
        e1 = 16'd255;   e2 = 16'd255;  #20;
        e1 = 16'd1024;  e2 = 16'd2;    #20;
        e1 = 16'd32767; e2 = 16'd2;    #20;
        e1 = 16'd65535; e2 = 16'd1;    #20;
        #40;
    end

    initial begin
        $monitor("t=%3d e1=%d e2=%d => s=%d",
                 $time, e1, e2, s);
    end
endmodule
