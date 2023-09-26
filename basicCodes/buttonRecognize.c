#include <stdio.h>
#include <stdlib.h>
#include <bcm2835.h>
#include <unistd.h>

#define LED RPI_GPIO_P1_18
#define BUTTON RPI_GPIO_P1_19

//set inputs e outputs



void setIOS(){
    bcm2835_gpio_fsel(LED, BCM2835_GPIO_FSEL_OUTP);
    bcm2835_gpio_fsel(BUTTON, BCM2835_GPIO_FSEL_INPT);
    bcm2835_gpio_set_pud(BUTTON, BCM2835_GPIO_PUD_UP); //habilitando botao de pull-up
    bcm2835_gpio_len(BUTTON);
}


int main(){

    if(!bcm2835_init()){ //se nao inicializar, retornar 1
    printf("deu pau");
            exit(1);
    }
    
    setIOS();

    while(1){
        if(bcm2835_gpio_eds(BUTTON)){
            printf("Botao apertado!\n");
           // bcm2835_gpio_write(LED, 1);
            bcm2835_gpio_set_eds(BUTTON);

        }else{
            printf("botao nao pressionado\n");
       		bcm2835_gpio_write(LED, HIGH);
		usleep(1000000);
		bcm2835_gpio_write(LED, LOW);
		usleep(1000000);
	 }
    }

 	bcm2835_gpio_write(LED,LOW);
    return 0;
}
