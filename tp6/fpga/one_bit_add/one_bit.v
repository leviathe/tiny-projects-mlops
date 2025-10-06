module one_bit(e1, e2, cin, s, cout);
	
	input e1, e2, cin;
	output s, cout;

	assign {cout, s} = e1 + e2 + cin;

endmodule
