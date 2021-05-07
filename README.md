# AreaComputation

Implementa métodos para cálculo de áreas de figuras genéricas. 

## Método um 

Consiste em dividir o plano em um grid e calcular quantos dos retângulos dele possuem centro dentro da figura. Ao saber a quantidade relativa de retangulos, podemos calcular multiplicando esse valor pela área total. O código também gera uma figura ilustrando os resultados. Atualmente, ele aproxima a área do circulo unitário a 3.2 dividindo o retângulo \[-2, 2\] x \[-2, 2] em 20 x 20 quadrados. A figura gerada é mostrada abaixo:

![Screenshot](media/graficototal.png)


## Método dois (probabilístico)

Consiste em considerar constante uma distribuição de probabilidade sobre dada região do plano. A área da região que desejamos saber é igual ao produto da área da região dada toda vezes a probabilidade empírica (obtida tomando pontos "aleatórios" do plano e vendo a quantidade relativa dos que estão dentro da figura) obtida. Atualmente, ele gera um gif/vídeo e está configurado para calcular pi usando o primeiro quadrante do circulo unitário e o retângulo [0, 1] x [0, 1].

![](media/MetodoProbabilistico.gif)
