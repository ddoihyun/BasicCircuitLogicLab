`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2024/06/04 16:22:07
// Design Name: 
// Module Name: Full_Adder
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


module Full_Adder( x, y, z, C, S);

input x, y, z;
output C, S;

wire net1, net2, net3;

    // Continuous assignment type
    // for HA1
    assign net1 = x^y;  // XOR
    assign net2 = x&y;  // AND
    
    //for HA2
    assign S = net1^z;  // XOR
    assign net3 = net1&z;   // AND
    
    //for C
    assign C = net3 | net2;    // OR
    
endmodule
