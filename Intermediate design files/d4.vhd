


------------------------------------------------------------------------
--  VHDL
-- 


--
-- 
-- modification, are permitted provided that the following conditions are met:
--    * Redistributions of source code must retain the above copyright
--      notice, this list of conditions and the following disclaimer.
--    * Redistributions in binary form must reproduce the above copyright
--      notice, this list of conditions and the following disclaimer in the
--      documentation and/or other materials provided with the distribution.
--    * Neither the name of the nor the
--      names of its contributors may be used to endorse or promote products
--      derived from this software without specific prior written permission.
--
-- 
-------------------------------------------------------------------------






library IEEE;
use IEEE.STD_LOGIC_1164.ALL;


entity d4 is
port (
      clk : in std_logic;
      data_in : in std_logic_vector(8 downto 0);
      data_out : out std_logic
 );
end d4;
architecture behavioral of d4 is
    signal data : std_logic_vector(8 downto 0);
    
--#pipelined=3
--   signal temp1,temp2,temp3,temp4, temp5,temp6,temp7 : std_logic;
--#pipelined=3

--#pipelined=2
--   signal temp1,temp2,temp3,temp4 : std_logic;
--#pipelined=2

--#pipelined=1
--   signal temp1,temp2,temp3 : std_logic;
--#pipelined=1



begin
-- process for registering data_in
process(clk)
begin
    if(rising_edge(clk)) then
        data <= data_in;
    end if;
end process;
--process for AND gate equation.
process(clk)
begin

--#pipelined=0
 if(rising_edge(clk)) then
 
     data_out <=data(0) and data(1) and data(2) and
                data(3) and data(4)and data(5) and data(6) and
                data(7) and data(8);
 end if;
 --#pipelined=0
 
 

--#pipelined=2
-- if(rising_edge(clk)) then
-- 
--     temp1<= (data(0) and data(1) and data(2);
--     temp2<= (data(3) and data(4) and temp1); 
--     temp3<= (data(5) and data(6) and temp2); 
--     temp4<= (data(7) and data(8) and temp3); 
-- end if;
 --#pipelined=2



--#pipelined=1
-- if(rising_edge(clk)) then
-- 
--     temp1<= (data(0) and data(1) and data(2) and data (3);
--     temp2<= (data(4) and data(5) and data(6) and temp1); 
--     temp3<= (data(7) and data(8) and temp2); 

-- end if;
 --#pipelined=1


 
   
--#pipelined=3
--  if(rising_edge(clk)) then
--     temp1 <= (data(0) and data(1)) ;
--     temp2 <= ( data(2) and temp1);
--     temp3 <= (data (3) and temp2);
--     temp4 <= (data(4) and temp3);
--     temp5<= ( data(5) and temp4);
--     temp6 <= (data (6) and temp5);
--     temp7<=(data(7) and temp6);
--     data_out<=(data(8) and temp7);
--  end if;
--#pipelined=3


--#dsp=0
-- 
--
--
--#dsp=0


--#bram=0
--
--
--
--
--#bram=0


--#bram=1
--
--
--
--
--#bram=1


--#dsp=1
--
--
--
--#dsp=1


end process;


end behavioral;


   
