module regression(e1,s);

  input [15:0] e1;

  output [32:0] s;

  assign s = 10000 + 5000 * e1;

endmodule
