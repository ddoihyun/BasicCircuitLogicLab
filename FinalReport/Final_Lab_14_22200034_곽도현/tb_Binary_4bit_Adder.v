`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2024/06/04 16:41:46
// Design Name: 
// Module Name: tb_Binary_4bit_Adder
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module tb_Binary_4bit_Adder();

reg [3:0] A_in, B_in;
wire C_out;
wire [3:0] Y_out;

Binary_4bit_Adder DUT(
    .A(A_in),
    .B(B_in),
    .C(C_out),
    .Y(Y_out)
);

initial begin
    A_in = 4'b0011;
    B_in = 4'b0110;
end

endmodule
