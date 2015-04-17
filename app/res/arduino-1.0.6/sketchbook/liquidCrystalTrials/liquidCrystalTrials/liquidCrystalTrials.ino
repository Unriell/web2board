/*
 Demonstration sketch for Adafruit i2c/SPI LCD backpack
 using MCP23008 I2C expander
 ( http://www.ladyada.net/products/i2cspilcdbackpack/index.html )

 This sketch prints "Hello World!" to the LCD
 and shows the time.
 
  The circuit:
 * 5V to Arduino 5V pin
 * GND to Arduino GND pin
 * CLK to Analog #5
 * DAT to Analog #4
*/

// include the library code:
#include <Wire.h>
#include <LiquidCrystal.h>

// Connect via i2c, default address #0 (A0-A2 not jumpered)
LiquidCrystal lcd(0);

void setup() {
  // set up the LCD's number of rows and columns: 
  lcd.begin(20, 4);
  
  // Print a message to the LCD.
//  lcd.print("hello, world!");
//  delay(500); 
  lcd.clear(); 
}

void loop() {
  // set the cursor to column 0, line 1
  // (note: line 1 is the second row, since counting begins with 0):
  lcd.setCursor(0, 0);
  lcd.setBacklight(HIGH);
  // print the number of seconds since reset:
  lcd.print("A");
  while (1){
    delay(1000);
    lcd.noDisplay(); 
    delay(1000); 
    lcd.display();
  }
}

