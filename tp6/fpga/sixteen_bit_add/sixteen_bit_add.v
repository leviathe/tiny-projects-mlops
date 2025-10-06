module sixteen_bit(e1, e2, cin, s, cout);
	
	input [7:0] e1, e2;
	input cin;
	
	output [7:0] s;
	output cout;

	assign {cout, s} = e1 + e2 + cin;

endmodule
