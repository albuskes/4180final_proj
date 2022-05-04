#include "mbed.h"
#include "uLCD_4DGL.h"
#include <cmath>  

Serial bluemod(p9,p10);
Serial pc(USBTX, USBRX);
uLCD_4DGL uLCD(p28,p27,p30); 
DigitalOut led(LED1);

int consecShoot = 0;
float x_curr=0;
float y_curr=0;
float z_curr=0;
float x_max=0;
float y_max=0;
float z_max=0;

union f_or_char {
    float f;
    char  c[4];
};

int main()
{    
    pc.baud(115200);
    char bchecksum=0;
    char temp=0;
    union f_or_char x,y,z;
    float xprev, yprev, zprev;
    int numShoot = 0;
    bool firstRun = true;
    bool canShoot = true;
    uLCD.color(BLUE);
    uLCD.locate(0,0);
    uLCD.printf("Stats:\n");
    
    while(1) {
        bchecksum=0;
        // Get input from accelerometer on phone and check it
        if (bluemod.getc()=='!') {
            if (bluemod.getc()=='A') { //Accelerometer data packet
                
                for (int i=0; i<4; i++) {
                    temp = bluemod.getc();
                    x.c[i] = temp;
                    bchecksum = bchecksum + temp;
                }
                for (int i=0; i<4; i++) {
                    temp = bluemod.getc();
                    y.c[i] = temp;
                    bchecksum = bchecksum + temp;
                }
                for (int i=0; i<4; i++) {
                    temp = bluemod.getc();
                    z.c[i] = temp;
                    bchecksum = bchecksum + temp;
                }
                if (bluemod.getc()==char(~('!' + 'A' + bchecksum))) { //checksum OK?
                    x_curr = x.f;
                    y_curr =y.f;
                    z_curr =z.f;
                    
                    // Sending signal for shooting
                    if (canShoot && (abs(z.f - zprev) > 0.3) || (abs(y.f - yprev) > 0.3) || (abs(x.f - xprev) > 0.3) && !firstRun) {
                        pc.printf("1");
                        canShoot = false;
                        numShoot++;
                    } else {
                        pc.printf("0");
                        canShoot = true;
                    }
                    
                    // Testing the max and printing if it changes
                    if(x.f > x_max){
                        uLCD.locate(0,0);
                        uLCD.color(BLACK);
                        uLCD.printf("\nMax X: \n %4f\n", x_max);
                        uLCD.color(RED);
                        uLCD.printf("\nMax X: \n %4f\n", x.f);
                        x_max = x.f;
                    }
                    if(y.f > y_max){
                        uLCD.locate(0,0);
                        uLCD.locate(0,5);
                        uLCD.color(BLACK);
                        uLCD.printf("\nMax Y: \n %5f\n", y_max);
                        uLCD.color(RED);
                        uLCD.printf("\nMax Y: \n %5f\n", y.f);
                        y_max = y.f;
                    }
                    if(z.f > z_max){
                        uLCD.locate(0,0);
                        uLCD.locate(0,10);
                        uLCD.color(BLACK);
                        uLCD.printf("\nMax Z: \n %5f\n", z_max);
                        uLCD.color(RED);
                        uLCD.printf("\nMax Z: \n %5f\n", z.f);
                        
                        z_max = z.f;
                    }
                    
                    // Setting old values from accelerometer
                    xprev = x.f;
                    yprev = y.f;
                    zprev = z.f;
                    firstRun = false;  
                }
            }
        }
    }
}
