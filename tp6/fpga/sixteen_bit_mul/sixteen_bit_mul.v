module sixteen_bit_mul(e1, e2, s);
	
	input [15:0] e1, e2;
	
	output [31:0] s;

	assign s = e1 * e2;

endmodule
