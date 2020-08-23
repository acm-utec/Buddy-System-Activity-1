#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <fstream>
using namespace std;
int main() {
    ofstream archivo("salida.txt");
    int filas=0;
    cout<<"ingrese numero de paginas web"<<endl;
    cin>>filas;
    srand(time(NULL));
    int random=0;
    int contador_filas[filas];
    for (int i=0;i<filas;i++){
        contador_filas[i]=0;
    }
    double matriz[filas][filas];
    for (int i=0;i<filas;i++) {
        int contador_filas1=0;
        for (int j = 0; j < filas; j++) {
            if (i==j){
                random=0;
                matriz[i][j]=random;
            }else {
                random = rand() % 2;
                matriz[i][j] = random;
            }
            if (random==1){
                contador_filas1+=random;
            }
        }
        contador_filas[i]=contador_filas1;
    }
    for (int i=0;i<filas;i++){
        if (contador_filas[i]==0){
            contador_filas[i]+=1;
            random=rand()%filas;
            matriz[i][random]=1;
        }
        cout<<contador_filas[i]<<endl;
    }
    for (int i=0;i<filas;i++){
        for (int j=0;j<filas;j++){
            matriz[i][j]=matriz[i][j]/contador_filas[j];
        }
    }
    archivo<<"[";
    for (int i=0;i<filas;i++){
        for (int j=0;j<filas;j++){
            archivo<<matriz[i][j]<<", ";
        }
        if (i!=filas-1){
            archivo<<"; ";
        }else{
        archivo<<"]"<<endl;
        }
    }  
    archivo<<"[";
    for (int i=0;i<filas;i++) {
        random = rand() % 2;
        if (i < filas - 1) {
            archivo << random << "; ";
        }else{
            archivo<<random<<"]"<<endl;
        }
    }
}
