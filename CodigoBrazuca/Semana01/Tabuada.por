programa {
  funcao inicio() {
    
    inteiro x, resultado

    escreva("Digite um número para saber a sua tabuada de multiplicação até o 10: ")
      leia(x)
    para(inteiro y = 1; y <= 10; y++){
      resultado = x * y
      escreva(x," * ", y," = ", resultado, "\n")

    }

  }
}