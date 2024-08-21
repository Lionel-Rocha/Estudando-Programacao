programa {
  funcao inicio() {
    
    inteiro x, resultado = 0

    para(inteiro i = 0; i < 5; i++){
      escreva("Digite um número: ")
        leia(x)

        se(x > 0){
          resultado++
        }

    }
    escreva(resultado, " números são positivos")
  }
}