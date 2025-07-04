`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2024/06/04 16:27:51
// Design Name: 
// Module Name: Binary_4bit_Adder
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


module Binary_4bit_Adder( A, B, C, Y );

input [3:0] A, B;
output C;
output [3:0] Y;

wire C1, C2, C3;

Full_Adder U0( .x(A[0]), .y(B[0]), .z(1'b0), .C(C1), .S(Y[0]) );
Full_Adder U1( .x(A[1]), .y(B[1]), .z(C1), .C(C2), .S(Y[1]) );
Full_Adder U2( .x(A[2]), .y(B[2]), .z(C2), .C(C3), .S(Y[2]) );
Full_Adder U3( .x(A[3]), .y(B[3]), .z(C3), .C(C), .S(Y[3]) );

endmodule
