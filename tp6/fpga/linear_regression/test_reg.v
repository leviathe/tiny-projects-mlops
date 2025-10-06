`timescale 1ns / 1ps
module stimulus;
    reg [15:0] e1;

    wire [31:0] s;

    regression uut (
        e1,
        s
    );

    initial begin
        $dumpfile("test.vcd");
        $dumpvars(0,stimulus);

        e1 = 16'd0;     #20;
        e1 = 16'd1;     #20;
        e1 = 16'd10;    #20;
        e1 = 16'd255;   #20;
        e1 = 16'd1024;  #20;
        e1 = 16'd32767; #20;
        e1 = 16'd65535; #20;
        #40;
    end

    initial begin
        $monitor("t=%3d e1=%d => s=%d",
                 $time, e1, s);
    end
endmodule
