A=//PEGAR LA MATRIZ GENERADA DEL CPP
x0=//PEGAR EL VECTOR GENERADO DEL CPP
disp(A);
//Despues de 15 iteraciones
for i=[1:15]
y1=A*x0;
[maxi,pos]=max(y1)
lambda1=y1(pos)
x1=y1/lambda1
end
disp(lambda1)
disp(x1)
suma=0
for i=1:length(x0)
 suma=suma+x0(i)
end
disp(suma)
x1=x1/suma
disp(x1)
